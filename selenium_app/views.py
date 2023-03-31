from rest_framework.decorators import api_view
from .serializers import SearchSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


@api_view(['POST'])
def search(request):
    serializer = SearchSerializer(data=request.data)
    serializer.is_valid()
    data1= request.data
    input = data1['customername']
    
    __name__=='__main__'

    PATH= "C:\Program Files (x86)\folder_chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.linkedin.com/home")

    # print(driver.title)
    time.sleep(3)
    driver.maximize_window()
    user_name = driver.find_element(By.XPATH,'//*[@id="session_key"]').send_keys("guystez@gmail.com")
    time.sleep(2)
    password = driver.find_element(By.XPATH,'//*[@id="session_password"]').send_keys("sims1000")
    driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form[1]/div[2]/button').click()
    time.sleep(6)
    # input = ['Amit Kochman']
    search_button = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    search_button.send_keys(input)
    time.sleep(6)
    search_button.send_keys(Keys.RETURN)
    time.sleep(4)     
    view_profile = driver.find_element(By.CSS_SELECTOR, ".app-aware-link.artdeco-button.artdeco-button--default.artdeco-button--2.artdeco-button--muted.artdeco-button--secondary")
    view_profile.click()
    time.sleep(7) 
    driver.execute_script("window.scrollBy(0, 300)","")                 
    time.sleep(7) 
    # see more button:
    # loop through the section elements
    for div_num in range(10):
        for section_num in range(10):
            xpath = f"/html/body/div[{div_num}]/div[3]/div/div/div[2]/div/div/main/section[{section_num}]/div[3]/div/div/div/span[3]/button"
            
            try:
                # wait for the element to be present and click on it
                see_more = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, xpath)))
                see_more.click()
                print(f"Clicked on button in div {div_num}, section {section_num}.")
                break
            except:
                print(f"Button with XPath {xpath} not found.")
        else:
            continue
        break
    time.sleep(7)

    #About 
    # loop through the section elements
    for div_num in range(10):
        for section_num in range(10):
            xpath = f"/html/body/div[{div_num}]/div[3]/div/div/div[2]/div/div/main/section[{section_num}]/div[3]/div/div/div/span[2]"
            try:
                # wait for the element to be present and click on it
                about = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))        
                print(f"try to click on {div_num} , section {section_num}.")
                text= about.text
                break
            except:
                print(f"try to click on {xpath} not found.")
        else:
            continue
        break
    time.sleep(3)

    print ('DONE')
    response_data = {
        'input': input,
        'serializer_data': serializer.data,
        'text':text
    }
    return Response( response_data, status=status.HTTP_201_CREATED)

