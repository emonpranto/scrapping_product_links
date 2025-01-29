import re 
import selenium
import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.daraz.com.bd/routers/')

# product = driver.find_element(By.CSS_SELECTOR,'''#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(1) > div > div > div.buTCk > div.RfADt > a''' )

# link = product.get_attribute('href')
# print(link)

text = driver.find_element(By.CSS_SELECTOR,'''#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div.xYcXp > div > div.Ck3Nt > div > div > span:nth-child(1)''').text
print(text)

count = re.findall(r'\d+',text)
pages = round(int(count[0])/40)
print(pages)

dic = {}
for page in range(1,pages+1):
    driver.get(f'https://www.daraz.com.bd/routers/?page={str(page)}')
    links = []
    for j in range(1,41):
        try:
            product = driver.find_element(By.CSS_SELECTOR,f'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child({str(j)}) > div > div > div.buTCk > div.RfADt > a')
            link = product.get_attribute('href')
            links.append(link)
        except Exception as e:
            print(f"Error processing product {j} on page {page} and the exception is {e} or all of the product is been scrapped.")
            continue
    
    dic[f'page{page}']=links

print(dic)
driver.quit()