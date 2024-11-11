import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://automationteststore.com/index.php?rt=account/login")
    driver.maximize_window()
    yield driver
    driver.quit()

driver = webdriver.Chrome()

# Khởi tạo WebDriver
driver = webdriver.Chrome()  # Đảm bảo WebDriver được khởi tạo đúng

# Hàm kiểm tra responsive cho từng kích thước
def test_check_responsive():
    url = "https://automationteststore.com/"
    
    # Mở trang web
    driver.get(url)
    time.sleep(2)  # Đợi trang tải

    # Kích thước desktop (1280x1024)
    driver.set_window_size(1280, 1024)
    time.sleep(1)
    assert "practice your automation skills" in driver.title, "Title does not match for desktop size"
    
    # Kích thước tablet (768x1024)
    driver.set_window_size(768, 1024)
    time.sleep(1)
    assert "practice your automation skills" in driver.title, "Title does not match for tablet size"

    # Kích thước mobile (375x667)
    driver.set_window_size(375, 667)
    time.sleep(1)
    assert "practice your automation skills" in driver.title, "Title does not match for mobile size"
  