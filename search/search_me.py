import requests, sys, webbrowser, bs4

if(len(sys.argv) > 1):
    resp = requests.get('https://www.google.com/search?q='+''.join(sys.argv[1:]))
else:
    resp = requests.get('https://www.google.com/search?q='+input('Search for: '))
resp.raise_for_status()

soup = bs4.BeautifulSoup(resp.text, "html.parser")
link_elements = soup.select('.r a')
links_to_open = min(5, len(link_elements))

for i in range(links_to_open):
    print('https://www.google.com'+link_elements[i].get('href'))
    webbrowser.open('https://www.google.com'+link_elements[i].get('href'))
    