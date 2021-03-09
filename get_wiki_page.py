import urllib.request, re


def get_page(url):
    """
    This function will get the text from wikipedia and clean the file
    from unnecesary html tags and comments. Also text not part of the
    content is removed. This will be stored in a file called
    "wikipedia_page.txt"
    """
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8').replace("\n", "qqqqq")
    pattern = re.compile('<div id="content".*')
    match = pattern.search(html)
    html = match.group()
    html = re.sub("<div id='mw-data-after-content'>.*", "", html)
    html = re.sub("<!--.*?-->", "", html)
    html = re.sub("<table.*?</table>", "", html)
    html = re.sub("<td.*?</td>|<tr.*?</tr>", "", html) 
    html = re.sub("<.*?>", "", html).replace("qqqqq", "\n")
    html = re.sub("\n+", "\n", html)
    
    with open("output.txt", "w") as file:
        file.write(html)


def main():
    get_page("https://nl.wikipedia.org/wiki/Rijksuniversiteit_Groningen")
    # the link of the most recent version of the wikipedia page


if __name__ == "__main__":
    main()
