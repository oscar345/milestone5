# milestone5

## Getting the text from wikipedia
The text was not copied and pasted into a text file. Using urllib.request from python 3.9.2 I downloaded the contents of the webpage. By using the inspector in the Firefox browser I found in which tags the content of the file was stored. I opened the file with the Unicode-8 encoding. Using regelar expressions also coming from python 3.9.2, I cleaned the HTML file by first removing all HTML that was not part of the content, removing comments and tables, and all HTML tags. Because regular expression work by line, i removed all newline characters and replaced them with "qqqqq" and at the end placed the newline characters back again.
