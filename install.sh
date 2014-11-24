#!/bin/sh

echo ">> compilation into linux architecture..."
GOOS=linux GOARCH=amd64 go build -o bot

echo ">> docker building..."
docker build -t ghigt-bot .

echo ">> done"
echo ">> you can now run \`docker run -d -p 7890:8000 --name ghigt-bot ghigt-bot\`"
