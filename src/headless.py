from selenium import webdriver

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument("--headless")

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=options.to_capabilities(),
    options=options,
)

# Selenium 経由でブラウザを操作する
driver.get("https://qiita.com")
print(driver.current_url)

# スクリーンショットの取得
FILENAME = "qiita.png"
w = driver.execute_script("return document.body.scrollWidth;")
h = driver.execute_script("return document.body.scrollHeight;")
driver.set_window_size(w, h)

result_screenshot = driver.save_screenshot(FILENAME)
if result_screenshot is False:
    print("An error has occurred while getting screenshot.")

# ページの一番下までスクロール
driver.execute_script('scroll(0, document.body.scrollHeight)')
    
# ブラウザを終了する
driver.quit()
