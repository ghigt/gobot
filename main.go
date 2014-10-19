package main

import (
	"encoding/json"
	"encoding/xml"
	"log"
	"net/http"
	"net/url"
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
}

type Movie struct {
	Title    string `json:"title"`
	Poster   string `json:"poster"`
	Director string `json:"director"`
	Synopsis string `json:"synopsis"`
	Type     string `json:"type"`
}

func fetchSeries(s string) []*Serie {
	res, err := http.Get("http://thetvdb.com/api/GetSeries.php?seriesname=" + url.QueryEscape(s))
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
	ints := &Interests{
		Series: series,
		Musics: musics,
		Movies: movies,
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
	http.HandleFunc("/api/interests", handleInterests)
	http.ListenAndServe(":8000", nil)
}
