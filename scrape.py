import requests

'''
Performs a http request to the given URL
'''
URL='https://www.monster.com/jobs/search/?q=Software-Developer&where=Nashville__2C-TN'

page=requests.get(URL)

print(page.content)