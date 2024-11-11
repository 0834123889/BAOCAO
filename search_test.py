import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://automationteststore.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

#Kiểm tra tìm kiếm đúng kết quả
def test_01(driver):
    # Nhập từ khóa tìm kiếm vào ô tìm kiếm
    driver.find_element(By.ID, "filter_keyword").send_keys("abcd") 
    
    search_button = driver.find_element(By.CLASS_NAME, "button-in-search")
    search_button.click()
    
    # Đợi trang tải kết quả (nếu cần)
    time.sleep(2)  

    # Kiểm tra thông báo "There is no product that matches the search criteria"
    message = driver.find_element(By.XPATH, "//*[contains(text(), 'There is no product that matches the search criteria.')]")
    assert message.is_displayed()

#Kiểm tra tìm kiếm sai kết quả
def test_02(driver):
    # Nhập từ khóa tìm kiếm vào ô tìm kiếm
    driver.find_element(By.ID, "filter_keyword").send_keys("skin") 
    
    search_button = driver.find_element(By.CLASS_NAME, "button-in-search")
    search_button.click()
    
    # Đợi trang tải kết quả (nếu cần)
    time.sleep(2)  

    # Kiểm tra thông báo "There is no product that matches the search criteria"
    product = driver.find_element(By.XPATH, "//a[@class='prdocutname' and text()='Skinsheen Bronzer Stick']")
    assert product.is_displayed()
