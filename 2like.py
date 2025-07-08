from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Minta input link video
video_url = input("🎯 Masukkan link video YouTube: ").strip()

# Setup headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.get(video_url)

print("🔄 Membuka video...")
time.sleep(5)

try:
    if "/shorts/" in video_url:
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[contains(@aria-label, "Like")]'))
        )
    else:
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//ytd-toggle-button-renderer)[1]//button'))
        )
    like_button.click()
    print("✅ Like berhasil dikirim!")
except Exception as e:
    print("❌ Gagal Like:", e)

driver.quit()
