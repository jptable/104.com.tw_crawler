# 104.com_crawler

* <h3> 適用需求：104 人力銀行使用者
    <h6> 想將所有工作瀏覽過一遍，加上點進求職連結閱覽技能需求，肯定肯定得花上數十小時。
    <h6> 使用爬蟲並匯入 excel 會是一個更有效率的方式。利用 excel 的篩選、資料清理等功能可以更快找到可以投遞的工作。
    
* <h3> 環境建置：
    <h6> python 需下載 "selenium"  
    <h6> 於此處 https://chromedriver.chromium.org/downloads 下載 chromedriver。
    <h6> 備註：chromedriver 有許多版本。自己的電腦適用哪個版本可以開啟電腦上的 chrome 瀏覽器，右上角「⋮」 > 說明 > 關於 google，裡面有自身適用的版本。可以依據該版本下載適合的 chromedriver 版本。
    
* <h3> 使用方法：
    <h6> 將 <grabbing.py> 以 python 編譯器開啟，並執行。
    <h6> 執行後編譯器會要求輸入要搜尋的頁面的網址，只要在後面輸入要抓資料的頁面網址，按下 enter 就可以跑了喔！
    <h6> 跑完會自動存在該專案所處的資料夾，內含「職缺名稱」、「所屬公司」、「公司地點」、「職缺敘述」。
