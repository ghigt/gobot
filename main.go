package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

type Interests struct {
	Series []*Serie `json:"series"`
	Musics []*Music `json:"musics"`
	Movies []*Movie `json:"movies"`
	Books  []*Book  `json:"books"`
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
	r.HandleFunc("/api/books/{pid:[0-9]+}", getBook)
	r.HandleFunc("/api/series", handleSeries)
	r.HandleFunc("/api/series/{pid:[0-9]+}", getSerie)
	r.HandleFunc("/api/musics", handleMusics)
	r.HandleFunc("/api/movies", handleMovies)
	r.HandleFunc("/api/movies/{pid:[0-9]+}", getMovie)
	http.ListenAndServe(":8000", r)
}
