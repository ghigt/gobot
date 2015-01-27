package main

import (
	"encoding/xml"
	"log"
	"net/http"
	"net/url"

	"github.com/gorilla/mux"
)

type Book struct {
	Pid         int    `xml:"id" json:"pid"`
	Title       string `xml:"best_book>title" json:"title"`
	ImageUrl    string `xml:"best_book>image_url" json:"imageurl"`
	Description string `xml:"best_book>description" json:"description"`
	Type        string `json:"type"`
}

func getBook(w http.ResponseWriter, r *http.Request) {
	pid := mux.Vars(r)["pid"]
	res, err := http.Get("http://www.goodreads.com/book/show.xml?key=1ED3NcURFpQFZvnMxM4ZNA&id=" + pid)
	if err != nil {
		log.Println("getBook Error:", err)
		return
	}
	defer res.Body.Close()

	var d struct {
		Book struct {
			Id          int    `xml:"id"`
			Title       string `xml:"title"`
			ImageUrl    string `xml:"image_url"`
			Description string `xml:"description"`
		} `xml:"book"`
	}
	err = xml.NewDecoder(res.Body).Decode(&d)
	if err != nil {
		log.Println("getBook Error:", err)
		return
	}
	sendJSON(&Book{
		Pid:         d.Book.Id,
		Title:       d.Book.Title,
		ImageUrl:    d.Book.ImageUrl,
		Description: d.Book.Description,
		Type:        "Book",
	}, w)
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

func handleBooks(w http.ResponseWriter, r *http.Request) {
	data := fetchBooks(getSearch(r))
	if data == nil {
		data = []*Book{}
	}
	sendJSON(data, w)
}
