#!/bin/bash

docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"
docker push jaimeviloria/scraper:$TRAVIS_TAG
docker push jaimeviloria/scraper:latest
