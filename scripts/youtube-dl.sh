#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
		    youtube-dl "$line"
			echo "Text read from file: $line"
	done < "$1"
