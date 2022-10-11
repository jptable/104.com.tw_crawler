# 104.com_crawler

## 適用需求：使用 104 人力銀行的求職者
想將所有工作瀏覽過一遍，加上點進求職連結閱覽技能需求，肯定肯定得花上數十小時。<br>
使用爬蟲並匯入 excel 會是一個更有效率的方式。利用 excel 的篩選、資料清理等功能可以更快找到可以投遞的工作。

## 環境建置：
1. python 需下載 "selenium" <br><br>
2. 於此處 https://chromedriver.chromium.org/downloads 下載 chromedriver。<br><br>
備註：chromedriver 有許多版本。自己的電腦適用哪個版本可以開啟電腦上的 chrome 瀏覽器，右上角「⋮」　＞　說明　＞　關於 google，裡面有自身適用的版本。可以依據該版本下載適合的 chromedriver 版本。<br>
    
## 使用方法：<br>
* 將 <grabbing.py> 以 python 編譯器開啟，並執行。<br><br>
* 執行後編譯器會要求輸入要搜尋的頁面的網址，只要在後面輸入要抓資料的頁面網址，按下 enter 就可以跑囉！<br><br>
* 跑完的資料會以 .xlsx 的形式儲存在該專案所處的資料夾。<br><br>
* 內含「職缺名稱」、「所屬公司」、「公司地點」、「職缺敘述」。<br><br>

## 已知問題：<br>
該網頁自動下拉17頁之後會出現「手動載入」的按鈕，其 xpath 一處 div[] 每天不同。<br>
如：div[18] -> div[19]<br>
        
### 解決方法<br>
1. 右鍵點選「手動載入」按鈕　＞　檢查　＞　複製該行的完整 xpath。<br>
2. 找到該區程式碼<br>
          
```python
for i in range(19, 283, 2):
    driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[2]/div[4]/div[%d]/button" % i).click()
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```
        
3. 在空白處貼上複製的 xpath <br>
4. 找到上述 /html/body/main/div[3]/div/div[2]/div[4]/div[%d]/button"，應該只有 div[%d] 與不同 <br>
5. 將不同的那一個數字填入 "for i in range(19, 283, 2)" 中的 "19" 的位置。 <br>
