#!/usr/bin/env bash

url="example.com/?q="
for i in $(cat pages_with_node_ids_raw); do
    content="$(curl -s "$url/$i")"
    echo "$content" >> output.txt
done