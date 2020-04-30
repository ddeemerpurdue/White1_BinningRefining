#!/bin/bash

while IFS= read -r line
do
	echo "$line"
	$
done < $1

SS=$(echo $f | cut -d'_' -f 2,3)
