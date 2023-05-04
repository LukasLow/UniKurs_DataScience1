#!/bin/bash

args=("$@")

num_args=${#args[@]}

# mehr als 2 abbruch
if [ $((num_args > 2)) -ne 0 ]; then
  exit 1
fi


# Iteriert über jedes Argumentenpaar im Array
for ((i=0; i<num_args; i+=2)); do
  arg1="${args[$i]}"
  arg2="${args[$i+1]}"
  echo "Wenn nix kommt is nix da"
  # Führen Sie hier die gewünschten Aktionen für jedes Argumentenpaar aus
  while true; do
    ps | grep ^"$arg1"
    sleep $arg2
  done
done
