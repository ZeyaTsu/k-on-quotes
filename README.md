# K-ON Quotes
Get quotes from the K-ON anime in the most easiest way possible

# Table of contents
* Content
* Usage
* Splitting the quote from the author
* Fixing UnicodeError whe using local file

# Content
Currently the file contains 137 quotes, however, more quotes are going to come in the future. <br/>
You can ask to add quotes in the file by opening either an issue or a pull request

# Usage
As you can see, this is a .txt file and not a .json file. Here's how to get a random quote from it. <br/>
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
# Splitting the quote from the author
```py
# Taking our previous code
quote, author = random_line.strip().split(" / ")
print(f"Quote: {quote} by {author}")
```
# Fixing UnicodeError when using local file
If you download the quotes.txt file instead of using the url, it is possible to get a UnicodeError. In this case, you will have to add a encoding parameter </br>
```py
with open('quotes.txt', 'r', encoding='utf-8') as f:
```
