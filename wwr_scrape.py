import requests
from bs4 import BeautifulSoup

job_list = []


def scrape_page(url):
  print("Scraping page: " + url)
  response = requests.get(url)
  soup = BeautifulSoup(
      response.content,
      "html.parser",
  )
  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_="title").text
    company, time, region = job.find_all("span", class_="company")
    company = company.text
    time = time.text
    region = region.text

    try:
      url = job.find("div", class_="tooltip").next_sibling["href"]
    except:
      url = "No URL"

    job_list.append({
        "Title": title,
        "Company": company,
        "Time": time,
        "Region": region,
        "url": f"https://weworkremotely.com{url}"
    })


def get_pages(url):
  response = requests.get(
      "https://weworkremotely.com/remote-full-time-jobs?page=1")
  soup = BeautifulSoup(response.content, "html.parser")
  return len(
      soup.find("div", class_="pagination").find_all("span", class_="page"))


for i in range(
    get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")):
  scrape_page(f"https://weworkremotely.com/remote-full-time-jobs?page={i+1}")
print(len(job_list))
