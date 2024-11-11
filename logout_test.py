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

# TC01: Kiểm tra đăng xuất thành công.
def test_01(driver):
    driver.find_element(By.ID, "loginFrm_loginname").send_keys("chikhang")
    driver.find_element(By.ID, "loginFrm_password").send_keys("123123")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-orange[title='Login']")
    login_button.click()
    time.sleep(2)   
    driver.find_element(By.XPATH, "//a[text()='Logoff']").click()

    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@title='Continue']").click()
    login_register_link = driver.find_element(By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=account/login' and text()='Login or register']")
    
    assert login_register_link.is_displayed(), "Link 'Login or register' not found on the page."