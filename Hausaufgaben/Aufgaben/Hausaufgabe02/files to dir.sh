input_file="./Kapitel_I.txt"

while IFS= read -r line; do
  # Führen Sie hier die gewünschten Aktionen für jede Zeile aus

  echo "$line"
done < "$input_file"