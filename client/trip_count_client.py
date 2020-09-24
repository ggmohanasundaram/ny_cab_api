import requests

if __name__ == '__main__':
    #URLs
    #For all available medallion 'http://127.0.0.1:5000/api/v1/trips'
    #For a medallion for all date 'http://127.0.0.1:5000/api/v1/trips?medallion=<medallionId>
    #For a medallion a date 'http://127.0.0.1:5000/api/v1/trips?medallion=<medallionId>&date='2013-12-01'
    url = 'http://127.0.0.1:5000/api/v1/trips?medallion=D7D598CD99978BD012A87A76A7C891B7' # API for Single
    response = requests.get(url)
    print(response.json())
    url = 'http://127.0.0.1:5000/api/v1/trips'
    response = requests.get(url)
    print(response.json())
    url = 'http://127.0.0.1:5000/api/v1/trips?medallion=D7D598CD99978BD012A87A76A7C891B7&date=2013-12-01'
    response = requests.get(url)
    print(response.json())