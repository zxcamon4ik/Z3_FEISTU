#!/bin/bash

# skript na konverziu PNG obrazkov z 'input_folder' do TXT formatu do 'output_folder'
# $1 - prvy CMD argument
# $2 - druhy CMD argument
input_folder="$1"
output_folder="$2"
i=1
j=$(ls -l "$input_folder"/*.png | wc -l) # pocet PNG suborov v adresari
for file in "$input_folder"/*.png; do
    python img2txt.py "$file" "$output_folder"
    echo "$i / $j" # print progress
    if [ $i -eq 1000 ]; then # konvertuje prvych 1000 obrazkov, potom skonci
        echo "Done"
        break
    fi
    i=$((i + 1)) # poradove cislo suboru
done