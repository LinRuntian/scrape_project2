from urllib.request import urlopen

url = "https://www.bbcgoodfood.com/recipes/category/christmas"

from urllib.request import FancyURLopener


class AppURLopener(FancyURLopener):
  version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open(url)

data = response.read()
text = data.decode("utf-8")

with open('html_text.txt', 'w') as f:
    f.write(text)
