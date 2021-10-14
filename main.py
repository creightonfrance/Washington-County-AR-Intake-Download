import requests

resp = requests.get('https://sheriff.washingtoncountyar.gov/res/DIntakeRoster.aspx')

print(resp.text)