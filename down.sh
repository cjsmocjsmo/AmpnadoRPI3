#!/bin/sh

docker-compose down;
sudo rm -rf ../Thumbnails;
touch ../Thumbnails;
docker image ls;
