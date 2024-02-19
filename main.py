# heroku profitcentr
from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github import Github
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from bs4 import BeautifulSoup
import os
from flask import Flask
import threading
import random
import re
import sys
from io import StringIO

MAX_LOG_MESSAGES = 10  # Maximum number of log messages to display
MAX_PRINT_STATEMENTS = 10  # Maximum number of print statements to display
log_messages = []
stdout_capture = StringIO()
sys.stdout = stdout_capture
import yt_dlp
def check_video_privacy(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        # Create a yt_dlp options object
        options = {
            'quiet': True,
            'extract_flat': True,
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            video_info = ydl.extract_info(url, download=False)

            # Check the privacy status
            if video_info.get('age_limit') is not None:
                return "Private"
            else:
                return "Not Private"
    except Exception as e:
        return f"Error: {e}"


account_number = os.getenv("ACCOUNT_NUMBER")
app = Flask(__name__)

@app.route('/')
def hello():
    return f"{'<br>'.join(log_messages[-MAX_LOG_MESSAGES:])}<br>{'<br>'.join(stdout_capture.getvalue().splitlines()[-MAX_PRINT_STATEMENTS:])}"

port = int(os.environ.get("PORT", 5000))

def flask_thread():
    app.run(host="0.0.0.0", port=port)

def running():
    # your existing running() function
    # Use ChromeOptions directly
    
    chrome_options = Options()
    #chrome_options.add_argument(f'--proxy-server={proxy_with_port}')
    #chrome_options.add_argument(f'--user-agent={test_ua}')
    chrome_options.add_argument('--headless')
    
    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Use context manager to handle the WebDriver instance
    with webdriver.Chrome(options=chrome_options) as driver1:
        driver1.get("https://seo-fast.ru/")
        #driver1.maximize_window()
        driver1.set_window_size(1280, 675)
        print("Please wait...")
        
        # Load cookies from file
        with open(f'account_{account_number}.json', 'r') as f:
            cookies = json.load(f)
        #time.sleep(2)
        # Add cookies to the browser session
        for cookie in cookies:
            driver1.add_cookie(cookie)
        #time.sleep(2)
        # Refresh the page to apply cookies
        #driver1.get("https://seo-fast.ru/")
        
        driver1.get("https://seo-fast.ru/work_youtube?youtube_video_simple")
        #driver1.save_screenshot("screenshot1.png")
        coin  = WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[1]/div[1]/nav/div[2]/ul/li/a[1]/div/div[3]/span'))).text
        print(coin)
        time.sleep(2)
        try:
            WebDriverWait(driver1, 1).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/div[5]/div/a'))).click()
            time.sleep(0.2)
        except:
            pass
        

        while True:
            try:
                
                WebDriverWait(driver1, 1).until(               
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/div[2]/form/div/label[1]"))).click()
                time.sleep(0.7)
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/div[2]/form/a"))).click()
                time.sleep(0.7)
                WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "fa-refresh"))).click()
                print("starting1")
                time.sleep(0.7)

               
            except:
                break
        
       
        #input()
        v=15
        d=1
        while d < v:
            driver1.execute_script("window.scrollBy(0, 60);")
            time.sleep(0.01)
            d=d+1
        
        
        #driver1.save_screenshot("screenshot2.png")
        
   
        window_before = driver1.window_handles[0]

        time.sleep(1)
        
        #checking video
        WebDriverWait(driver1, 2).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[2]/td[1]/a/span'))).click()
        iddf =  WebDriverWait(driver1, 2).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, 'val')))
        value = iddf.get_attribute("value")
        pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
        match = re.search(pattern, value)
        value1 = match.group(1)
        print(value1)
        result1 = check_video_privacy(value1)
        if "ERROR" in result1:
            print("yes")
            WebDriverWait(driver1, 2).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[2]/td[1]/a/span'))).click()
            WebDriverWait(driver1, 2).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[2]/td[3]/span[4]'))).click()
            
        


        WebDriverWait(driver1, 2).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody/tr[2]/td[1]/a/span'))).click()
       

        idd = WebDriverWait(driver1, 2).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div/table[2]/tbody/tr/td[2]/div[15]/div/div/table/tbody'))).text
       
        match = re.search(r'ID: (\d+)', idd)
        first_id = match.group(1)
        print("First ID:", first_id)

        result_string = "".join(first_id.split())
        print("First ID:", result_string)
        

        
        fdfgdf = f"//*[@id='res_views{result_string}']/div/a"
    
        WebDriverWait(driver1, 120).until(
                        EC.element_to_be_clickable((By.XPATH, fdfgdf))).click()
         
        time.sleep(2)
        window_after = driver1.window_handles[1]
        driver1.switch_to.window(window_after)
        #driver1.save_screenshot("screenshot4.png")
        time.sleep(2)

        
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)
        #driver1.save_screenshot("screenshot6.png")
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(0.5)
       # driver1.save_screenshot("screenshot3.png")
        time.sleep(17)
   

        print("Cookies copied successfully..")

        driver1.quit()

def sdsf():
    while True:
        try:
            running()
        except:
            continue





# Start Flask in a separate thread
flask_thread = threading.Thread(target=flask_thread)
flask_thread.start()



flask_thread1 = threading.Thread(target=sdsf)
flask_thread1.start()






if __name__ == '__main__':
    # This block will only be executed when the script is run directly, not when imported
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        scheduler.shutdown()


sys.stdout = sys.__stdout__