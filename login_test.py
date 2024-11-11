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

# TC01: Kiểm tra đăng nhập thành công.
def test_01(driver):
    driver.find_element(By.ID, "loginFrm_loginname").send_keys("chikhang")
    driver.find_element(By.ID, "loginFrm_password").send_keys("123123")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-orange[title='Login']")
    login_button.click()

    time.sleep(2)   
    element = driver.find_element(By.XPATH, "//span[@class='maintext' and contains(text(), 'My Account')]")
    assert element.text == "MY ACCOUNT"


def test_02(driver):
    driver.find_element(By.ID, "loginFrm_password").send_keys("123123")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-orange[title='Login']")
    login_button.click()
    time.sleep(2)    

    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger')]")
    assert error_message.text.strip() == "×\nError: Incorrect login or password provided."
    
def test_03(driver):
    driver.find_element(By.ID, "loginFrm_loginname").send_keys("chikhang")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-orange[title='Login']")
    login_button.click()
    time.sleep(2)    

    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger')]")
    assert error_message.text.strip() == "×\nError: Incorrect login or password provided."

#Kiểm tra đăng nhập sai tài khoản và mật khẩu
def test_04(driver):
    driver.find_element(By.ID, "loginFrm_loginname").send_keys("ákjdhhaisd")
    driver.find_element(By.ID, "loginFrm_password").send_keys("ándkjansd")
    login_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-orange[title='Login']")
    login_button.click()
    time.sleep(2)       
    error_message = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger')]")
    assert error_message.text.strip() == "×\nError: Incorrect login or password provided."