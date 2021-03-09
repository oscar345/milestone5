# milestone5

## Getting the text from wikipedia
The text of the wikipedia page was not copied and pasted into a text file. Using urllib.request from python 3.9.2 I downloaded the contents of the webpage. By using the inspector in the Firefox browser I found in which tags the content of the file was stored. I opened the file with the Unicode-8 encoding. Using regelar expressions also coming from python 3.9.2, I cleaned the HTML file by first removing all HTML that was not part of the content, removing comments and tables, and all HTML tags. Because regular expression work by line, I removed all newline characters and replaced them with "qqqqq" and at the end placed the newline characters back again. This does mean that when "qqqqq" will become part of the original HTML, which is very unlikely, this python script won't provide a correct text file.

## Storing the text
The text that was used with the bash script is stored as "used_wikipedia_text". All new output of the "get_wiki_page" python script will be stored in "wikipedia_text". 

## Counting the "de"'s 
This was done with a bash script. There are two functions in this script. The first is for counting the "de"'s. The words are tokenized excluding all characters that are not alphanumerical. Each is played on a new line. Using another grep command each whole word that is "de" is counted and placed in a text file called "final_output.txt". Also with that other function all tokens are displayed.

## The data
The data in which the "de"'s are counted, the tokens are also displayed, so it is possible for other to see in which set of words i was looking for "de". 

## Systems and data used
- Operating system: MacOS Big Sur 11.2.2
- Programming languages: Python version 3.9.2, shell script (coming with MacOS)
- Wikipedia page: Rijksuniversiteit Groningen, Dutch, from 8 march 2021 (so (this version)[https://nl.wikipedia.org/w/index.php?title=Rijksuniversiteit_Groningen&oldid=57576769]
