import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time

@pytest.fixture(scope="module")
def streamlit_app():
    # Start the Streamlit app in the background
    process = subprocess.Popen(["streamlit", "run", "main.py"])
    time.sleep(5)  # Give the app some time to start
    yield process
    # Teardown: close the app
    process.terminate()

@pytest.fixture(scope="module")
def driver(streamlit_app):
    # Initialize a headless Chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10) # Implicit wait for elements
    yield driver
    driver.quit()

def test_basic_addition(driver):
    driver.get("http://localhost:8501")
    wait = WebDriverWait(driver, 10)

    # Enter numbers
    num1_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='number' and @aria-label='Enter first number']")))
    num1_input.clear()
    num1_input.send_keys("5")

    num2_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='number' and @aria-label='Enter second number']")))
    num2_input.clear()
    num2_input.send_keys("3")

    # Click Add button (assuming first operation button is Add)
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_button.click()

    # Click Equals button
    equals_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Equals']")))
    equals_button.click()

    # Verify result
    result_display = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='stText']//h2[normalize-space()='Result']/following-sibling::div[1]")))
    assert result_display.text == "8.0"

def test_clear_functionality(driver):
    driver.get("http://localhost:8501")
    wait = WebDriverWait(driver, 10)

    # Perform an operation first
    num1_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='number' and @aria-label='Enter first number']")))
    num1_input.clear()
    num1_input.send_keys("10")

    num2_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='number' and @aria-label='Enter second number']")))
    num2_input.clear()
    num2_input.send_keys("2")

    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']")))
    add_button.click()

    equals_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Equals']")))
    equals_button.click()

    # Click Clear button
    clear_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Clear']")))
    clear_button.click()

    # Verify inputs are reset (this might be tricky with Streamlit session state)
    # For now, we'll just check if the result display is cleared or not present.
    # More robust checks would require inspecting Streamlit's internal state or refreshing the page.
    with pytest.raises(TimeoutException): # Expect the result display to disappear
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='stText']//h2[normalize-space()='Result']")))

class TimeoutException(Exception):
    pass
