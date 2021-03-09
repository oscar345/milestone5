import urllib.request, re


def get_page(url):
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


if __name__ == "__main__":
    main()
