import requests
from bs4 import BeautifulSoup
import re

# URL you want to fetch
url = "https://ingenieria.uncuyo.edu.ar/direccion-de-relaciones-internacionales"

# Send GET request
response = requests.get(url)

# Print status code (200 means OK)
print("Status Code:", response.status_code)

# Convert the raw HTML into a structure we can navigate
soup = BeautifulSoup(response.text, "html.parser")

# 3. Get all text from the page
page_text = soup.get_text()

# 4. Use regex to find email addresses
emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", page_text)

# 5. Print found emails
print("Emails found on the page:")
if not emails:
    print("There are no emails")
else:
    for email in emails:
        print(emails)
