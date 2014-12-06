package main

import (
	"encoding/json"
	"encoding/xml"
	"fmt"
	"log"
	"net/http"
	"net/url"

	"github.com/gorilla/mux"
)

type Music struct {
	Title  string `json:"title"`
	Artist string `json:"artist"`
	Album  string `json:"album"`
	Type   string `json:"type"`
}

type Interests struct {
	Series []*Serie `json:"series"`
	Musics []*Music `json:"musics"`
	Movies []*Movie `json:"movies"`
	Books  []*Book  `json:"books"`
}

type Movie struct {
	Title    string `json:"title"`
	Poster   string `json:"poster"`
	Director string `json:"director"`
	Synopsis string `json:"synopsis"`
	Type     string `json:"type"`
}

type Book struct {
	Title     string `xml:"best_book>title" json:"title"`
	Author    string `xml:"best_book>author>name" json:"author"`
	Image_url string `xml:"best_book>image_url" json:"imageurl"`
	Type      string `json:"type"`
}

type Serie struct {
	Pid         int    `json:"pid"`
	Title       string `json:"title"`
	Description string `json:"description"`
	ImageUrl    string `json:"imageurl"`
	Type        string `json:"type"`
}

func getSerie(w http.ResponseWriter, r *http.Request) {
	pid := mux.Vars(r)["pid"]
	res, err := http.Get("https://api.betaseries.com/shows/pictures?key=3e803b0b5556&nbpp=100&id=" + pid)
	if err != nil {
		log.Println("fetchSeries Error:", err)
		return
	}
	defer res.Body.Close()

	var pic struct {
		Pictures []struct {
			Url string `json:"url"`
		} `json:"pictures"`
	}
	err = json.NewDecoder(res.Body).Decode(&pic)
	if err != nil {
		log.Println("fetchSeries Error:", err)
		return
	}
	res, err = http.Get("https://api.betaseries.com/shows/display?key=3e803b0b5556&nbpp=100&id=" + pid)
	if err != nil {
		log.Println("fetchSeries Error:", err)
		return
	}
	defer res.Body.Close()

	var s struct {
		Show struct {
			Id          int    `json:"id"`
			Title       string `json:"title"`
			Description string `json:"description"`
		} `json:"show"`
	}
	err = json.NewDecoder(res.Body).Decode(&s)
	if err != nil {
		log.Println("fetchSeries Error:", err)
		return
	}
	fmt.Printf("%+v\n", s)
	sendJSON(&Serie{
		Pid:         s.Show.Id,
		Title:       s.Show.Title,
		Description: s.Show.Description,
		ImageUrl:    pic.Pictures[0].Url,
		Type:        "Serie",
	}, w)
}

func fetchSeries(s string) []*Serie {
	res, err := http.Get("https://api.betaseries.com/shows/search?key=3e803b0b5556&nbpp=100&title=" + url.QueryEscape(s))
	if err != nil {
		log.Println("fetchSeries Error:", err)
		return nil
	}
	defer res.Body.Close()

	var d struct {
		Shows []struct {
			Id          int    `json:"id"`
			Title       string `json:"title"`
			Description string `json:"description"`
		} `json:"shows"`
	}

	err = json.NewDecoder(res.Body).Decode(&d)
	if err != nil {
		log.Println("FetchSeries Error:", err)
		return nil
	}
	ss := []*Serie{}
	for _, data := range d.Shows {
		s := &Serie{
			Pid:         data.Id,
			Title:       data.Title,
			Description: data.Description,
			Type:        "Serie",
		}
		ss = append(ss, s)
	}
	return ss
}

func fetchBooks(s string) []*Book {
	res, err := http.Get("https://www.goodreads.com/search.xml?key=1ED3NcURFpQFZvnMxM4ZNA&field=title&q=" + url.QueryEscape(s))
	if err != nil {
		log.Println("Error:", err)
		return nil
	}
	defer res.Body.Close()

	var d struct {
		Books []*Book `xml:"search>results>work"`
	}

	err = xml.NewDecoder(res.Body).Decode(&d)
	if err != nil {
		log.Println("Error:", err)
		return nil
	}
	for i := range d.Books {
		d.Books[i].Type = "Book"
	}
	return d.Books
}

func fetchMusics(s string) []*Music {
	res, err := http.Get("http://api.deezer.com/search?q=" + url.QueryEscape(s))
	if err != nil {
		log.Println("Error:", err)
		return nil
	}
	defer res.Body.Close()

	var d struct {
		Data []struct {
			Title  string `json:"title"`
			Artist struct {
				Name string `json:"name"`
			} `json:"artist"`
			Album struct {
				Title string `json:title`
			} `json:"album"`
		} `json:"data"`
	}

	err = json.NewDecoder(res.Body).Decode(&d)
	if err != nil {
		log.Println("Error:", err)
		return nil
	}

	ms := []*Music{}
	for _, data := range d.Data {
		m := &Music{
			Title:  data.Title,
			Artist: data.Artist.Name,
			Album:  data.Album.Title,
			Type:   "Music",
		}
		ms = append(ms, m)
	}

	return ms
}

func fetchMovies(s string) []*Movie {
	res, err := http.Get("https://api.betaseries.com/movies/search?key=3e803b0b5556&nbpp=100&title=" + url.QueryEscape(s))
	if err != nil {
		log.Println("FetchMovies Error:", err)
		return nil
	}
	defer res.Body.Close()

	var d struct {
		Data []struct {
			Title    string `json:"title"`
			Poster   string `json:"poster"`
			Director string `json:"director"`
			Synopsis string `json:"synopsis"`
		} `json:"movies"`
	}

	err = json.NewDecoder(res.Body).Decode(&d)
	if err != nil {
		log.Println("FetchMovies Error:", err)
		return nil
	}

	ms := []*Movie{}
	for _, data := range d.Data {
		m := &Movie{
			Title:    data.Title,
			Poster:   data.Poster,
			Director: data.Director,
			Synopsis: data.Synopsis,
			Type:     "Movie",
		}
		ms = append(ms, m)
	}

	return ms
}

func getSearch(r *http.Request) string {
	s := r.URL.Query().Get("search")
	if s == "" {
		log.Println("Nothing to search")
		return ""
	}
	return s
}

func sendJSON(f interface{}, w http.ResponseWriter) {
	data, err := json.Marshal(f)
	if err != nil {
		log.Println("handler Error:", err)
		return
	}
	w.Header().Set("content-type", "application/json; charset=utf-8")
	_, err = w.Write(data)
}

func handleMovies(w http.ResponseWriter, r *http.Request) {
	data := fetchMovies(getSearch(r))
	if data == nil {
		data = []*Movie{}
	}
	sendJSON(data, w)
}
func handleBooks(w http.ResponseWriter, r *http.Request) {
	data := fetchBooks(getSearch(r))
	if data == nil {
		data = []*Book{}
	}
	sendJSON(data, w)
}
func handleMusics(w http.ResponseWriter, r *http.Request) {
	data := fetchMusics(getSearch(r))
	if data == nil {
		data = []*Music{}
	}
	sendJSON(data, w)
}
func handleSeries(w http.ResponseWriter, r *http.Request) {
	data := fetchSeries(getSearch(r))
	if data == nil {
		data = []*Serie{}
	}
	sendJSON(data, w)
}

func handleInterests(w http.ResponseWriter, r *http.Request) {
	s := r.URL.Query().Get("search")
	if s == "" {
		log.Println("Nothing to search")
		return
	}
	series := fetchSeries(s)
	if series == nil {
		series = []*Serie{}
	}
	musics := fetchMusics(s)
	if musics == nil {
		musics = []*Music{}
	}
	movies := fetchMovies(s)
	if movies == nil {
		movies = []*Movie{}
	}
	books := fetchBooks(s)
	if books == nil {
		books = []*Book{}
	}
	ints := &Interests{
		Series: series,
		Musics: musics,
		Movies: movies,
		Books:  books,
	}
	data, err := json.Marshal(ints)
	if err != nil {
		log.Println("handler Error:", err)
		return
	}
	w.Header().Set("content-type", "application/json; charset=utf-8")
	_, err = w.Write(data)
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/api/interests", handleInterests)
	r.HandleFunc("/api/books", handleBooks)
	r.HandleFunc("/api/series", handleSeries)
	r.HandleFunc("/api/series/{pid:[0-9]+}", getSerie)
	r.HandleFunc("/api/musics", handleMusics)
	r.HandleFunc("/api/movies", handleMovies)
	http.ListenAndServe(":8000", r)
}
