import requests
from bs4 import BeautifulSoup
import time
import urllib

link = 'https://service2.diplo.de/rktermin/extern/appointment_showMonth.do?locationCode=shan&realmId=96&categoryId=560'
header = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
          }


i = 3001
while i <= 4000:
    start = time.process_time()
    result = requests.get(link, headers=header)
    result1 = BeautifulSoup(result.text, 'lxml')
    number = result1.find('captcha')
    image_link = number.div['style'].split(' ')[1][5:-2]
    urllib.request.urlretrieve(image_link, 'foto/{}.png'.format(i + 1))
    i = i + 1
    end = time.process_time()
    print(i, 'time consuming: ', end - start)
    time.sleep(1.5)
