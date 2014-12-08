package main

import (
	"encoding/json"
	"log"
	"net/http"
	"net/url"

	"github.com/gorilla/mux"
)

type Music struct {
	Pid    int    `json:"pid"`
	Title  string `json:"title"`
	Artist string `json:"artist"`
	Album  string `json:"album"`
	Type   string `json:"type"`
}

func getMusic(w http.ResponseWriter, r *http.Request) {
	pid := mux.Vars(r)["pid"]
	res, err := http.Get("http://api.deezer.com/track/" + pid)
	if err != nil {
		log.Println("getMusic Error:", err)
		return
	}
	defer res.Body.Close()

	var d struct {
		Id     int    `json:"id"`
		Title  string `json:"title"`
		Artist struct {
			Name string `json:"name"`
		} `json:"artist"`
		Album struct {
			Title string `json:title`
		} `json:"album"`
	}
	err = json.NewDecoder(res.Body).Decode(&d)
	if err != nil {
		log.Println("getMusic Error:", err)
		return
	}
	sendJSON(&Music{
		Pid:    d.Id,
		Title:  d.Title,
		Artist: d.Artist.Name,
		Album:  d.Album.Title,
		Type:   "Music",
	}, w)
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
			Id     int    `json:"id"`
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
			Pid:    data.Id,
			Title:  data.Title,
			Artist: data.Artist.Name,
			Album:  data.Album.Title,
			Type:   "Music",
		}
		ms = append(ms, m)
	}

	return ms
}

func handleMusics(w http.ResponseWriter, r *http.Request) {
	data := fetchMusics(getSearch(r))
	if data == nil {
		data = []*Music{}
	}
	sendJSON(data, w)
}
