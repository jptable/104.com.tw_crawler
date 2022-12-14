import datetime
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re

def del_emoji(text):
    emoji = re.compile('["\U00010000-\U0010ffff""●❒★▎■※↗↙•√！*▲◆【】"]', re.U)
    return (re.sub(emoji, '', text))


# 取得網址
_url = input('請輸入待搜尋頁面網址：')

# chromedriver 路徑
service = Service(executable_path="D:/selenium/chromedriver")

# get URL
driver = webdriver.Chrome(service= service)
driver.get(_url)

"""
 模擬滑鼠滾輪，
 104 網頁 前17頁動態載入，
 之後都手動載入
"""


for i in range(1,10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

for i in range(17,280,2):
    driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[4]/div[%d]/button" % i).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


"""取得網頁資料"""
jobs = driver.find_elements(By.XPATH, '/html/body/main/div[3]/div/div[2]/div[4]/article')
for i in range(0, len(jobs)):
    jobs[i] = jobs[i].text
jobs = '||工作名稱:'.join(jobs)


"""資料清理"""
jobs = del_emoji(jobs)
jobs = re.sub('儲存\n應徵', '', jobs)
jobs = re.sub('[0-9]+~[0-9]+人應徵', '', jobs)
jobs = re.sub('大於30人應徵', '', jobs)
jobs = re.sub('[-]', '', jobs)

jobs = jobs.split('||')
df = pd.DataFrame(jobs)
print(jobs)
print(df)

filename = datetime.date.today()

df.to_csv(f'{filename}.csv')

driver.quit()