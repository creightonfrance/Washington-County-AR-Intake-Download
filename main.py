# Written by Creighton France

# Import statements
import requests
from bs4 import BeautifulSoup

# Open file to write raw data
rawDataFile = open('raw3daydata.txt', 'w')
sortedData = open('3daydata.txt', 'w')

# Pull information from the site
resp = requests.get('https://sheriff.washingtoncountyar.gov/res/DIntakeRoster.aspx')
soup = BeautifulSoup(resp.text, 'html.parser')

# Write a pretty copy to the raw data file
#rawDataFile.write(soup.body.div.table.prettify())
for i, element in enumerate(soup.body.div.table.find_all('tr')):
    if (i != 0):
        sortedData.write("---------------\n")
        print("\n" + str(i))
        print(element.contents[1].a['href'])
        print(element.contents[1].get_text())
        print(element.contents[3].get_text())
        print(element.contents[5].get_text())
        print(element.contents[7].get_text())
        print(element.contents[9].get_text())
        print(element.contents[11].get_text())
        print(element.contents[13].get_text())
        print(element.contents[15].get_text())
        sortedData.write(element.contents[1].get_text() + "\n")
        sortedData.write(element.contents[3].get_text() + "\n")
        sortedData.write(element.contents[5].get_text() + "\n")
        sortedData.write(element.contents[7].get_text() + "\n")
        sortedData.write(element.contents[9].get_text() + "\n")
        sortedData.write(element.contents[11].get_text() + "\n")
        sortedData.write(element.contents[13].get_text() + "\n")
        sortedData.write(element.contents[15].get_text() + "\n")

rawDataFile.write(soup.prettify())

# Close data files
rawDataFile.close()
sortedData.close()