package main

import (
	"encoding/json"
	"log"
	"net/http"
	"net/url"
)

type Movie struct {
	Title    string `json:"title"`
	Poster   string `json:"poster"`
	Director string `json:"director"`
	Synopsis string `json:"synopsis"`
	Type     string `json:"type"`
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

func handleMovies(w http.ResponseWriter, r *http.Request) {
	data := fetchMovies(getSearch(r))
	if data == nil {
		data = []*Movie{}
	}
	sendJSON(data, w)
}
