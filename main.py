import requests
from bs4 import BeautifulSoup

rawDataFile = open('raw3daydata.txt', 'w')

resp = requests.get('https://sheriff.washingtoncountyar.gov/res/DIntakeRoster.aspx')
soup = BeautifulSoup(resp.text, 'html.parser')

rawDataFile.write(soup.prettify())
rawDataFile.close()