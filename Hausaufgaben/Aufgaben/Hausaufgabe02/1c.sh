#!/bin/bash

num_chapters=13  

Kapitelnummer=("I" "II" "III" "IV" "IVa" "V" "VI" "VII" "VIII" "IX" "X" "Xa" "XI")  # Liste der Kapitelnummern

for ((i=0; i<Kapitelnummer; i++))
do
  # Define the chapter range using the chapter and subchapter numbers
  start="^${Kapitelnummer[$i]}[[:space:]]*$"
  if [ $((i+1)) -eq $Kapitelnummer ]
  then
    end="^${Kapitelnummer[$i]}[[:space:]]+[[:upper:]]"
  else
    end="^${Kapitelnummer[$((i+1))]}[[:space:]]*$"
  fi

  # Extract the chapter and save to file
  sed -n "/$start/,/$end/p" grundgesetz.txt | tac | tail -n +2 | tac > "Kapitel_${Kapitelnummer[$i]}"
done
