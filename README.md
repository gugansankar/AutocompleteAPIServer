# Simple Autocomplete API Server

### About
This is a simple autocomplete API server(Python Flask) which uses Redis as a backend. Here used Redis SortedSet along with zrank/zrange to accomplise this.

Ref - http://oldblog.antirez.com/post/autocomplete-with-redis.html
### Requirements
- Docker
- Docker-compose
### Install

Clone this repository and run the below command 

``docker-compose up -d``

### Usage
* To add new word

``curl http://localhost:5000/add_word?word=foo``

* To check autocomplete

``curl http://localhost:5000/autocomplete?query=fo``
