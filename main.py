import requests

rawDataFile = open('raw3daydata.txt', 'w')

resp = requests.get('https://sheriff.washingtoncountyar.gov/res/DIntakeRoster.aspx')

rawDataFile.write(resp.text)

rawDataFile.close()