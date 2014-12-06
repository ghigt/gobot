package main

import (
	"encoding/json"
	"log"
	"net/http"
	"net/url"

	"github.com/gorilla/mux"
)

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

func handleSeries(w http.ResponseWriter, r *http.Request) {
	data := fetchSeries(getSearch(r))
	if data == nil {
		data = []*Serie{}
	}
	sendJSON(data, w)
}
