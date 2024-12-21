# Analysis of the Lord of the Rings Dataset

## 2. Dataset Overview
The dataset (`lotr_scripts.csv`) contains dialog data from the Lord of the Rings movies. Below are the main fields included:

- **film**: The name of the movie (*The Fellowship of the Ring*, *The Two Towers*, or *The Return of the King*).
- **chapter**: The chapter from which the dialog is extracted.
- **char**: The character speaking the line.
- **dialog**: The spoken dialog by the character.

---
## 3. Dirty Data
### Scripts:
- $ head -n 10 lotr_scripts.csv
- ,char,dialog,movie
- 0,DEAGOL,"Oh Smeagol Ive got one! , Ive got a fish Smeagol, Smeagol!    ",The Return of the King
- 1,SMEAGOL,"Pull it in! Go on, go on, go on, pull it in!  ",The Return of the King
- 2,DEAGOL,Arrghh! ,The Return of the King
- 3,SMEAGOL,Deagol!  ,The Return of the King
- 4,SMEAGOL,Deagol!  ,The Return of the King
- 5,SMEAGOL,Deagol!  ,The Return of the King
- 6,SMEAGOL,Give us that! Deagol my love  ,The Return of the King
- 7,DEAGOL,Why?  ,The Return of the King
- 8,SMEAGOL,"Because' , it's my birthday and I wants it.  ",The Return of the King
### Characters:
- $ head -n 10 lotr_characters.csv
- birth,death,gender,hair,height,name,race,realm,spouse
- ,,Female,,,Adanel,Men,,Belemir
- TA 2978,"February 26 ,3019",Male,Dark (book) Light brown (movie),,Boromir,Men,,
- ,"March ,3019",Male,,,Lagduf,Orcs,,
- TA 280,TA 515,Male,,,Tarcil,Men,Arnor,Unnamed wife
- ,,Male,,,Fire-drake of Gondolin,Dragon,,
- SA 2709,SA 2962,Male,,,Ar-Adûnakhôr,Men,Númenor,Unnamed wife
- ,,Male,,,Annael,Elves,,
- YT,FA 455,Male,Golden,,Angrod,Elves,,Eldalótë
- ,,,,,Angrim,,,
### Remove rows with empty fields:
- $ sed '/^$/d' lotr_scripts.csv > cleaned_lotr_scripts.csv
### Standardize character names to title case:
- $ sed -E 's/char,([a-z]+)/\U\1/' cleaned_lotr_scripts.csv > temp.csv && mv temp.csv cleaned_lotr_scripts.csv
### Remove special characters in dialog:
- $ sed -E 's/[^a-zA-Z0-9 .,!?'\''"]//g' cleaned_lotr_scripts.csv > temp.csv && mv temp.csv cleaned_lotr_scripts.csv

--- 

## 5. Analysis the Dataset
### Find the total number of lines and unique words used in the dialogs.
$ awk -F, 'NR>1 {print $3}' cleaned_lotr_scripts.csv | wc -l
- 2390

### What is the distribution on the three different films?
### What are the top 5 characters in the char column?
$ awk -F, 'NR>1 {print $2}' cleaned_lotr_scripts.csv | sort | uniq -c | sort -nr | head -5
- 225 FRODO
- 216 SAM
- 205 GANDALF
- 185 ARAGORN
- 163 PIPPIN

### What are the top 5 characters in the dialogues?
$ awk -F, 'NR>1 {print $2, NF-1}' cleaned_lotr_scripts.csv | awk '{arr[$1]+=$2} END {for (i in arr) print arr[i], i}' | sort -nr | head -5
- 785 GANDALF
- 782 SAM
- 764 FRODO
- 627 ARAGORN
- 563 PIPPIN
