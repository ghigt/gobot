package main

import (
	"encoding/xml"
	"log"
	"net/http"
	"net/url"
)

type Book struct {
	Pid       int    `xml:"id" json:"id"`
	Title     string `xml:"best_book>title" json:"title"`
	Author    string `xml:"best_book>author>name" json:"author"`
	Image_url string `xml:"best_book>image_url" json:"imageurl"`
	Type      string `json:"type"`
}

//func getBook(w http.ResponseWriter, r *http.Request) {
//	pid := mux.Vars(r)["pid"]
//	res, err := http.Get("https://api.betaseries.com/shows/pictures?key=3e803b0b5556&nbpp=100&id=" + pid)
//	if err != nil {
//		log.Println("getBook Error:", err)
//		return
//	}
//	defer res.Body.Close()
//
//	var d struct {
//		Books []*Book `xml:"book"`
//	}
//	err = json.NewDecoder(res.Body).Decode(&d)
//	if err != nil {
//		log.Println("getBook Error:", err)
//		return
//	}
//	sendJSON(&Book{
//		Pid:         s.Show.Id,
//		Title:       s.Show.Title,
//		Description: s.Show.Description,
//		ImageUrl:    pic.Pictures[0].Url,
//		Type:        "Serie",
//	}, w)
//}

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

func handleBooks(w http.ResponseWriter, r *http.Request) {
	data := fetchBooks(getSearch(r))
	if data == nil {
		data = []*Book{}
	}
	sendJSON(data, w)
}
