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
filterbyid=parseddata.find(id='ResultsContainer')

# print(filterbyid.prettify())

'''
Printing the displayed job listings from the filterbyid results 
'''
jobslisted=filterbyid.find_all('section', class_='card-content')

for singlejob in jobslisted:
    

    title=singlejob.find('h2', class_='title')
    company=singlejob.find('div', class_='company')
    location=singlejob.find('div',class_='location')

    # print(singlejob, end='\n'*2)

    '''
    .text returns only the text content of the HTML elements that the object contains
    '''

    print(title.text)
    print(company.text)
    print(location.text)



