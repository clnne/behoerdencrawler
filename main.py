import requests
from bs4 import BeautifulSoup
import json

# ohne useragent gibt der bund nen 403 forbidden zurück
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

def crawlJobDetails(job_url):
    response = requests.get(job_url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # extrahierung <title>-element
    title = soup.find('title').get_text(strip=True)

    # der beschreibungstext befindet sich vermutlich in einem spezifischen abschnitt
    description_element = soup.find_all('section')[4]
    description = description_element.get_text(separator='\n', strip=True)

    return title, description

def crawlJobList(url):
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    job_links = soup.find_all('a', href=True)

    jobs_data = []

    for link in job_links:
        if "IMPORTE/Stellenangebote" in link['href']:
            job_url = 'https://www.service.bund.de/' + link['href']
            print(f"Abrufen von Informationen von: {job_url}")
            title, description = crawlJobDetails(job_url)
            jobs_data.append({'title': title, 'description': description})

    return jobs_data

all_jobs = []

for page in range(1, 9):
    url = f'https://www.service.bund.de/Content/DE/Stellen/Suche/Formular.html?nn=4642046&cl2Categories_Taetigkeitsfeld=taetigkeitsfeld-itundtelekommunikation&gtp=4642266_list%253D{page}&type=0&searchResult=true&resultsPerPage=100'
    jobs = crawlJobList(url)
    all_jobs.extend(jobs)

with open('jobs_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_jobs, f, ensure_ascii=False, indent=4)