import requests

from bs4 import BeautifulSoup
'''
Beautiful soup is a python library for parsing structured data
'''

'''
Performs a http request to the given URL
The website being scraped in this case serves static HTML content
'''

URL='https://www.monster.com/jobs/search/?q=Software-Developer&where=Nashville__2C-TN'

page=requests.get(URL)

parseddata=BeautifulSoup(page.content, 'html.parser')

# print(parseddata)

'''
Finding a specific element by ID
For easier viewing you can use .prettify()
'''
results=parseddata.find(id='ResultsContainer')

# print(results.prettify())

'''
Printing the displayed job listings from the results 
'''
jobslisted=results.find_all('section', class_='card-content')

for singlejob in jobslisted:
    

    title=singlejob.find('h2', class_='title')
    company=singlejob.find('div', class_='company')
    location=singlejob.find('div',class_='location')

    # print( end='\n'*2)

    '''
    .text returns only the text content of the HTML elements that the object contains
    .strip() removes the whitespace
    '''

    if None in (title,company,location):
        continue

    # print(title.text.strip())
    # print(company.text.strip())
    # print(location.text.strip())

'''
Finding all the java developer openings
Lambda function looks at the text of each h2 element converts it to lowercase 
and checks whether the substring is java
'''
javadevs=results.find_all('h2', string=lambda text: 'java' in text.lower())

print(f"{len(javadevs)} java jobs found \n")

for java in javadevs:
    url=java.find('a')['href']
    print(java.text.strip())
    print(f"Apply for this job at:{url}\n")
    









