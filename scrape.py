import requests

'''
Performs a http request to the given URL
The website being scraped in this case serves static HTML content
'''

URL='https://www.monster.com/jobs/search/?q=Software-Developer&where=Nashville__2C-TN'

page=requests.get(URL)

print(page.content)