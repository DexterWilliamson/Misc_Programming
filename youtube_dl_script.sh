#!/bin/bash

linenum=1

echo "Hello, $(whoami), this is the youtube-dl script to download multiple things at once of varying types";
read -p "Let's begin";
currenttime=$(date +"%H%M")
echo "$currenttime"
clear;
read -p "Give me the text file location: " filePath;

numoflines=$(wc -l < "$filePath")

while [[ "$linenum" -lt "$numoflines" ]]
do

  if [[ $(date +"%T") > '05:00:00' ]] && [[ $(date +"%T") < '22:30:00' ]];
  then

    line="$(sed "${linenum}q;d" "$filePath")"
    echo "slowdown time"

    if [[ "$line" != *"playlist"* ]]; then

      youtube-dl -i -f 137+140 -w --limit-rate=2.5m -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "$line"

    elif [[ "$line" == *"playlist"* ]]; then

      youtube-dl -i -f 137+140 -w --limit-rate=2.5m --yes-playlist -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "$line"

    else
      echo "Bad input"
    fi

  else

    line="$(sed "${linenum}q;d" "$filePath")"
    echo "not slowdown time"

    if [[ "$line" != *"playlist"* ]]; then

      youtube-dl -i -f 137+140 -w -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "$line"

    elif [[ "$line" == *"playlist"* ]]; then

      youtube-dl -i -f 137+140 -w --yes-playlist -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "$line"

    else
      echo "Bad input"
    fi

  fi

  ((linenum++))

done
