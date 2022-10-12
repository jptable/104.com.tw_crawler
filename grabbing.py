import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re

# chromedriver 路徑
service = Service(executable_path="D:/selenium/chromedriver")

# get URL
driver = webdriver.Chrome(service= service)
driver.get("https://www.104.com.tw/jobs/search/?cat=2011000000&jobsource=2018indexpoc&ro=0")

# 模擬滑鼠滾輪
# 104 網頁 前17頁動態載入
# 之後都手動載入
for i in range(1,18):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

for i in range(19,283,2):
    driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[4]/div[%d]/button" % i).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 抓職缺名稱

job_name = driver.find_elements(By.XPATH, '/html/body/main/div[3]/div/div[2]/div[4]/article/div[1]/h2/a')

print("職位名稱共%d筆" % len(job_name))

for i in range(0,len(job_name)):
    print(job_name[i].text)
    job_name[i] = job_name[i].text


# 抓公司名稱
company = driver.find_elements(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[4]/article/div[1]/ul[1]/li[2]/a")
print("公司名稱共%d筆" % len(company))

for i in range(0, len(company)):
    print(company[i].text)
    company[i] = company[i].text


# 抓公司位置
location = driver.find_elements(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[4]/article/div[1]/ul[2]/li[1]")
print("職缺位置共%d筆" % len(location))

for i in range(0, len(location)):
    print(location[i].text)
    location[i] = location[i].text


# 抓職缺簡介
knowledge = driver.find_elements(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[4]/article/div[1]/p")
print("簡介共%d筆" % len(knowledge))

for i in range(0, len(knowledge)):
    print(knowledge[i].text)
    knowledge[i] = knowledge[i].text


# 存入excel

filename = time.time() # 檔案名稱

# zip multi list to a list
df = pd.DataFrame(list(zip(job_name, company, location, knowledge)),
                  columns=['jobs', 'company', 'location', 'knowledge'])

print('\n', '\n', df)

writer = pd.ExcelWriter("%d.xlsx" %filename, engine='xlsxwriter')
df.to_excel(writer, sheet_name='worksheet', index=False)
writer.save()

driver.quit()
