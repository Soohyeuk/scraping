import requests
from bs4 import BeautifulSoup

keywords = ["python", "golang", "flutter"]
all_jobs = {"python" : [], "golang" : [], "flutter" : []}

def scrape(url, keyword):
  r = requests.get(url, headers={
      "User-Agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
  })
  soup = BeautifulSoup(r.content, "html.parser")
  jobs = soup.find_all("tr", class_="job")

  for job in jobs: 
    title = job.find("h2", itemprop="title").text
    location = job.find("div", class_="location")
    location = location.text

    try: 
      link = job.find("a", class_="preventLink")["href"]
    except:
      link = "No URL"
  
    all_jobs[keyword].append({
      "title": title,
      "location": location,
      "link": f"https://remoteok.com/remote-{keyword}-jobs{link}"
    })

def doing(): 
  for word in keywords: 
    scrape(f"https://remoteok.com/remote-{word}-jobs",word)
    print(word, all_jobs[word])

doing()