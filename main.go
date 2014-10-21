package main

import (
	"encoding/json"
	"encoding/xml"
	"io/ioutil"
	"log"
	"net/http"
)

type Serie struct {
	Title    string `xml:"SeriesName" json:"title"`
	ImageUrl string `xml:"banner" json:"imageurl"`
	Summary  string `xml:"Overview" json:"summary"`
	Type     string `json:"type"`
}

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
	Title     string `xml:"search>results>work>best_book>title" json:"title"`
	Author    string `xml:"search>results>work>best_book>author>name" json:"author"`
	Image_url string `xml:"search>results>work>best_book>image_url" json:"image_url"`
	Type      string `json:"type"`
}

func fetchBooks(s string) []*Book {
	res, err := http.Get("https://www.goodreads.com/search.xml?key=1ED3NcURFpQFZvnMxM4ZNA&field=title&q=" + s)
	if err != nil {
		log.Println("Error:", err)
		return nil
	}
	body, err := ioutil.ReadAll(res.Body)
	defer res.Body.Close()
	if err != nil {
		log.Fatal(err)
	}

	var d struct {
		b []*Book
	}

	err = xml.Unmarshal([]byte(body), &d.b)
	if err != nil {
		log.Fatal(err)
	}
	for i := range d.b {
		d.b[i].Type = "Book"
	}
	return d.b
}

func fetchSeries(s string) []*Serie {
	res, err := http.Get("http://thetvdb.com/api/GetSeries.php?seriesname=" + s)
	if err != nil {
		log.Println("Error:", err)
		return nil
	}
	defer res.Body.Close()

	var d struct {
		Data struct {
			Series []*Serie
		}
	}
	err = xml.NewDecoder(res.Body).Decode(&d.Data)
	if err != nil {
		log.Println("Error:", err)
		return nil
	}
	for i := range d.Data.Series {
		d.Data.Series[i].Type = "Serie"
	}
	return d.Data.Series
}

func fetchMusics(s string) []*Music {
	res, err := http.Get("http://api.deezer.com/search?q=" + s)
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
	res, err := http.Get("https://api.betaseries.com/movies/search?key=3e803b0b5556&nbpp=100&title=" + s)
	if err != nil {
		log.Println("Error:", err)
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
		log.Println("Error:", err)
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
		log.Println("Error:", err)
		return
	}
	w.Header().Set("content-type", "application/json; charset=utf-8")
	_, err = w.Write(data)
}

func main() {
	http.HandleFunc("/api/interests", handleInterests)
	http.ListenAndServe(":8000", nil)
}
