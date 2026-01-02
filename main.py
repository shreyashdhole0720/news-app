import requests  # pip install requests

query = input("What type of news are you interested in today? ")

api = "16a9f0ba71d94e1193c2002c012a556d"

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api}"

r = requests.get(url)

data = r.json()

# Debug check (important for beginners)
if data["status"] != "ok":
    print("Error:", data)
    exit()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1)
    print(article["title"])
    print(article["url"])
    print("\n****************************************\n")

    