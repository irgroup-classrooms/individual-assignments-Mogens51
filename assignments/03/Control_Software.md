
## 1. How do you get the first three lines of the file 2014-01_JA.tsv? 
$ head -3 2014-01_JA.tsv  
- File    Creator Issue   Volume  Journal ISSN    ID      Citation        Title Place Labe       Language        Publisher       Date
- History_1a-rdf.tsv      Doolittle, W. E.        1       59      KIVA -ARIZONA-0023-1940        (Uk)RN001571862 KIVA -ARIZONA- 59(1), 7-26. (1993)      A Method for Distinguishing between Prehistoric and Recent Water and Soil Control Features    xxu     eng     ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY   1993
- History_1a-rdf.tsv      Nelson, M. C.   1       59      KIVA -ARIZONA-  0023-1940      (Uk)RN001571874 KIVA -ARIZONA- 59(1), 27-48. (1993)     Classic Mimbres Land Use in the Eastern Mimbres Region, Southwestern New Mexico        xxu   eng      ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY   1993

---

## 2. How do you get the total number of lines in each of the *.tsvfiles?
$ wc -l *.tsv  
- 13712 2014-01-31_JA-africa.tsv
- 27392 2014-01-31_JA-america.tsv
- 507732 2014-01_JA.tsv
- 5375 2014-02-02_JA-britain.tsv
- 554211 total

---

## 3.How do you get the file with the highest number of lines and how many does it have? Can you get the output with a single command line call?
$ wc -l *.tsv | sort -nr | head -n 2 | tail -n 1  
- 507732 2014-01_JA.tsv
