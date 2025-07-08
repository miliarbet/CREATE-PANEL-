from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Ganti dengan link video YouTube target
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Setup headless Chrome
options = Options()
options.add_argument("--headless")  # Hapus ini kalau mau lihat browsernya
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")

# Jalankan driver
driver = webdriver.Chrome(options=options)
driver.get(video_url)

print("🔄 Membuka video...")
time.sleep(5)

try:
    # Klik tombol Like
    like_button = driver.find_element("xpath", '(//ytd-toggle-button-renderer)[1]//button')
    like_button.click()
    print("✅ Like berhasil dikirim!")
except Exception as e:
    print("❌ Gagal Like:", e)

driver.quit()
