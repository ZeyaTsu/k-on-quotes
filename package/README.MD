# K-ON Quotes
Get quotes from the K-ON anime in the most easiest way possible<br/>
<img src="https://i.imgur.com/0qVCV8Z.jpeg" alt="Mio Akiyama" width="46%"/>

# Table of contents
* Content
* Usage
* Splitting the quote from the author
* Fixing UnicodeError whe using local file

# Content
Currently the file contains 213 quotes, however, more quotes are going to come in the future. <br/>
You can ask to add quotes by opening either an issue or a pull request

# Usage
## 0 - With python package
`pip install kon_quotes`
```py
from kon_quotes import GETquote

quote = GETquote(character_you_want) # mio, yui, azusa, tsumugi, ritsu, sawako, jun, general, all
quote_author = quote.GETauthor()
print(f"{quote} - {quote_author}")
```

## 1 - With .txt file (online)
```py
import requests, random

file_url = "https://zeyatsu.github.io/k-on-quotes/quotes.json" # No need to download the txt file.
response = requests.get(file_url)

if response.status_code == 200:
  lines = response.text.splitlines()
  random_line = random.choice(lines)
  print(random_line)
else:
  print("Error: ", response.status_code)
```
## 2 - With API (.json file (online))
```py
import random
import requests

json_url = "https://zeyatsu.github.io/k-on-quotes/quotes.json" # No need to download the json file.

response = requests.get(json_url)

if response.status_code == 200:
    data = response.json()
    random_author = random.choice(list(data["authors"].keys()))
    random_quote = random.choice(data["authors"][random_author])

    print(f"{random_quote} by {random_author}")
```

For characters replace "k-on-quotes/quotes.json" by "k-on-quotes/characters/the_character_you_want.json"

# Splitting the quote from the author
```py
quote, author = random_quote.strip().split(" / ")
print(f"Quote: {quote} by {author}")
```

# Fixing UnicodeError when using local file
If you download the quotes.txt file instead of using the url, it is possible to get a UnicodeError. In this case, you will have to add a encoding parameter </br>
```py
with open('quotes.txt', 'r', encoding='utf-8') as f:
```

# Credits
<table>
  <tr>
    <td style="align:center;">
      <a href="https://github.com/ZeyaTsu"> 
        <img src="https://avatars.githubusercontent.com/u/43354103?v=4" alt="Author: ZeyaTsu" width="100" height="100"/>
        <br/>
        <span>ZeyaTsu</span>
      </a>
    </td>
  </tr>
</table>
