from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

video_url = "https://www.youtube.com/shorts/dQw4w9WgXcQ"  # YouTube Shorts

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get(video_url)
time.sleep(5)

try:
    if "/shorts/" in video_url:
        like_button = driver.find_element("xpath", '//button[@aria-label="Like this video"]')
    else:
        like_button = driver.find_element("xpath", '(//ytd-toggle-button-renderer)[1]//button')

    like_button.click()
    print("✅ Like berhasil dikirim!")
except Exception as e:
    print("❌ Gagal Like:", e)

driver.quit()
