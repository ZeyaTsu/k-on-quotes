# K-ON Quotes
Get quotes from the K-ON anime in the most easiest way possible<br/>
<img src="https://i.imgur.com/0qVCV8Z.jpeg" alt="Mio Akiyama" width="46%"/>

# Table of contents
* Content
* Usage
* Splitting the quote from the author
* Fixing UnicodeError whe using local file

# Content
Currently the file contains 137 quotes, however, more quotes are going to come in the future. <br/>
You can ask to add quotes in the file by opening either an issue or a pull request

# Usage
## 1 - With .txt file (online)
Example to print a random quote from the online file
```py
import requests, random

file_url = "https://raw.githubusercontent.com/ZeyaTsu/k-on-quotes/main/quotes.txt" # No need to download the txt file.
response = requests.get(file_url)

if response.status_code == 200:
  lines = response.text.splitlines()
  random_line = random.choice(lines)
  print(random_line)
else:
  print("Error: ", response.status_code)
```
## 2 - With .json file (online)
```py
import random
import requests

json_url = "https://raw.githubusercontent.com/ZeyaTsu/k-on-quotes/main/quotes.json"

# Fetch JSON data from the URL
response = requests.get(json_url)
quotes_data = response.json()

# Choose a random quote from the fetched JSON data
random_quote = random.choice(quotes_data)

# Print the random quote and its author
print("Quote:", random_quote["quote"])
print("Author:", random_quote["author"])
```

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
        <h2>ZeyaTsu</h2>
      </a>
    </td>
  </tr>
</table>
