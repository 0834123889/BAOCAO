import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://automationteststore.com/index.php?rt=product/category&path=58")
    driver.maximize_window()
    yield driver
    driver.quit()


# TC01 Kiểm tra thêm sản phẩm thành công vào giỏ hàng và xóa giỏ hàng
def test_click_add_to_cart(driver: WebDriver):
    # Chờ và tìm thẻ <a> có class là 'productcart'
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "productcart"))
    )
    add_to_cart_button.click()
    
    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=checkout/cart']"))
    )
    cart_link.click()
    td_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//td[@class='align_left' and text()='DMBW0013']"))
    )
    assert td_element.is_displayed(), "The <td> element with text 'DMBW0013' is not displayed."
    
    
#TC002 
def test_add_and_remove_product_from_cart(driver: WebDriver):
    # Bước 1: Chờ và click vào nút 'Add to Cart'
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "productcart"))
    )
    add_to_cart_button.click()
    
    # Bước 2: Chờ và click vào liên kết giỏ hàng để mở trang giỏ hàng
    cart_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='https://automationteststore.com/index.php?rt=checkout/cart']"))
    )
    cart_link.click()

    # Bước 3: Xóa sản phẩm khỏi giỏ hàng
    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[@class='align_center']//a[contains(@href, 'remove=76')]"))
    )
    remove_button.click()
    
    # Bước 4:Tìm phần tử có class 'contentpanel' và lấy văn bản của nó
    content_text = driver.find_element(By.CLASS_NAME, "contentpanel").text

    # Kiểm tra xem văn bản có chứa "Your shopping cart is empty!" không
    assert "Your shopping cart is empty!" in content_text, "Không tìm thấy thông báo giỏ hàng trống!"
