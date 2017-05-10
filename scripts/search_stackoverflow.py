import requests
import bs4
import webbrowser
url = "http://www.stackoverflow.com/search?q="
base_url = "http://www.stackoverflow.com"

query = raw_input("Enter your query: ")
query = query.replace(" ","+")

link = url + query

r = requests.get(link)
d = r.text

soup = bs4.BeautifulSoup(d,"html.parser")
a = soup.select("div.result-link > span > a[href]")
num = min(5,len(a))

if len(a) != 0:
    for i in range(num):
        webbrowser.open( base_url + a[i].get("href"))
else:
    print "NO Result to display for your search."
