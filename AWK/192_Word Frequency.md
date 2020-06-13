###Question
Write a bash script to calculate the frequency of each word in a text file words.txt.

For simplicity sake, you may assume:

words.txt contains only lowercase characters and space ' ' characters.
Each word must consist of lowercase characters only.
Words are separated by one or more whitespace characters.
Example:

Assume that words.txt has the following content:
```
the day is sunny the the
the sunny is is
```
Your script should output the following, sorted by descending frequency:
```
the 4
is 3
sunny 2
day 1
Note:
```
Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
Could you write it in one-line using Unix pipes?
###cat solution

```
cat 192.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'
```
tr -s: truncate the string with target string, but only remaining one instance (e.g. multiple whitespaces)

sort: To make the same string successive so that uniq could count the same string fully and correctly.

uniq -c: uniq is used to filter out the repeated lines which are successive, -c means counting

sort -r: -r means sorting in descending order

awk '{ print $2, $1 }': To format the output, see here.
###awk solution
I should count the words. So I chose the awk command.
I use a dictionary in awk. For every line I count every word in the dictionary.
After deal with all lines. At the END, use for (item in Dict) { #do someting# } to print every words and its frequency.
Now the printed words are unsorted. Then I use a | pipes and sort it by sort
sort -n means "compare according to string numerical value".
sort -r means "reverse the result of comparisons".
sort -k 2 means "sort by the second word"

```
awk '\
{ for (i=1; i<=NF; i++) { ++D[$i]; } }\
END { for (i in D) { print i, D[i] } }\
' 192.txt | sort -nr -k 2
```