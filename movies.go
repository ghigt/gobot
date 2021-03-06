package main

import (
	"encoding/json"
	"log"
	"net/http"
	"net/url"
	"strconv"

	"github.com/gorilla/mux"
)

type Movie struct {
	Pid         int    `json:"pid"`
	Title       string `json:"title"`
	ImageUrl    string `json:"imageurl,omitempty"`
	Description string `json:"description"`
	Type        string `json:"type"`
	Info
}

func getMovie(w http.ResponseWriter, r *http.Request) {
	pid := mux.Vars(r)["pid"]
	res, err := http.Get("https://api.betaseries.com/movies/movie?key=3e803b0b5556&nbpp=100&id=" + pid)
	if err != nil {
		log.Println("getMovie Error:", err)
		return
	}
	defer res.Body.Close()

	var d struct {
		Movie struct {
			Id          int    `json:"id"`
			Title       string `json:"title"`
			Description string `json:"synopsis"`
			ImageUrl    string `json:"poster"`
			Imdb        string `json:"imdb_id"`
		} `json:"movie"`
	}
	err = json.NewDecoder(res.Body).Decode(&d)
	if err != nil {
		log.Println("getMovie Error:", err)
		return
	}
	res, err = http.Get("http://www.omdbapi.com/?i=" + d.Movie.Imdb + "&plot=full&r=json")
	if err != nil {
		log.Println("omdapi Error:", err)
		return
	}
	defer res.Body.Close()

	var omd struct {
		Info
	}
	err = json.NewDecoder(res.Body).Decode(&omd)
	if err != nil {
		log.Println("fetchSeries Error:", err)
		return
	}
	sendJSON(&Movie{
		Pid:         d.Movie.Id,
		Title:       d.Movie.Title,
		Description: d.Movie.Description,
		ImageUrl:    d.Movie.ImageUrl,
		Info:        omd.Info,
		Type:        "Movie",
	}, w)
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
			Id          int    `json:"id"`
			Title       string `json:"title"`
			Poster      string `json:"poster"`
			Director    string `json:"director"`
			Description string `json:"synopsis"`
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
			Pid:         data.Id,
			Title:       data.Title,
			Description: data.Description,
			ImageUrl:    "https://api.betaseries.com/pictures/movies?key=3e803b0b5556&nbpp=100&id=" + strconv.Itoa(data.Id),
			Type:        "Movie",
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
