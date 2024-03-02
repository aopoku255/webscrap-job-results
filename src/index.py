from bs4 import BeautifulSoup
import requests
import pandas as pd
htmls_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(htmls_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
count = 0
job_results = []
for job in jobs:
    company_name = job.find('h3', class_='joblist-comp-name')
    skills = job.find('span', class_='srp-skills')
    published_date = job.find('span', class_='sim-posted').span.text
    more_info = job.find('a', href=True)
    if 'few' in published_date:
        count = count + 1
        job_results.append([count, company_name.text.strip(), skills.text.strip().replace(' ', ''), more_info['href']])
        # print(f'''
        # {count}
        # company name: {company_name.text.strip()}
        # required skills: {skills.text.strip().replace(' ', '')}
        # more info: {more_info['href']}
        # ''')

df = pd.DataFrame(job_results, columns=['count', 'company_name', 'skils', 'more_info'])
df.to_csv('jobs_results.csv')