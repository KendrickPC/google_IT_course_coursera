#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ~/data/list.txt | cut -d' ' -f3 | cut -d'/' -f3)

for file in $files; do
  if test -e ~/data/$file; then
    echo $HOME/data/$file >> oldFiles.txt
  fi
done

# Running the script will give you the following output for oldFiles.txt:
# /home/student-00-db02c07a809b/data/jane_profile_07272018.doc
# /home/student-00-db02c07a809b/data/jane_contact_07292018.csv

