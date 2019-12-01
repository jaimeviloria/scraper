# scraper

[![Build Status](https://travis-ci.org/jaimeviloria/scraper.svg)](https://travis-ci.org/jaimeviloria/scraper)

## Installation

docker run --rm -p 8080:8080 jaimeviloria/scraper

## Usage

the api will be available on localhost:8080 when run via the installation command above

* GET	/v1/snippets

retrieves all snippets currently added

* POST	/v1/snippets	text

adds a new snippet, retrieving all urls starting with http or https

* GET	/v1/snippets/:id

retrieve a snippet by ID

* DELETE	/v1/snippets/:id

delete a snippet by ID
