#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


# In[2]:


path = "C:\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(path)
url = "https://healthdata.gov/National/School-Learning-Modalities-2021-2022/aitj-yx37/explore/query/SELECT%0A%20%20%60district_nces_id%60%2C%0A%20%20%60district_name%60%2C%0A%20%20%60week%60%2C%0A%20%20%60learning_modality%60%2C%0A%20%20%60operational_schools%60%2C%0A%20%20%60student_count%60%2C%0A%20%20%60city%60%2C%0A%20%20%60state%60%2C%0A%20%20%60zip_code%60/page/filter"
browser.get(url)

District_code=[]
District_name=[]
Week=[]
Learning_Modality=[]
Operational_Schools=[]
Student_Count=[]
City=[]
State=[]
ZIP_Code=[]
for j in range(1,1001):
    sleep(5)
    for i in range(1,21):
        District_code.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[1]/div").text)
        District_name.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[2]/div").text)
        Week.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[3]/div").text)
        Learning_Modality.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[4]/div").text)
        Operational_Schools.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[5]/div").text)
        Student_Count.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[6]/div").text)
        City.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[7]/div").text)
        State.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[8]/div").text)
        ZIP_Code.append(browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[2]/div/div/table/tbody/tr[" + str(i) + "]/td[9]/div").text)

    search=browser.find_element(By.XPATH,"//*[@id='explore-grid-app']/div/div/div[1]/div[3]/div/div/a[3]/span[1]")
    search.click()


# In[3]:


pd.set_option("max_rows",None)


# In[4]:


df=pd.DataFrame({"District_code":District_code,"District_name":District_name,"Week":Week,"Learning_Modality":Learning_Modality,"Operational_Schools":Operational_Schools,"Student_Count":Student_Count,"City":City,"State":State,"ZIP_Code":ZIP_Code})


# In[5]:


df


# In[6]:


df.shape


# In[8]:


df.to_csv("School_Learning_Modalities.csv", index = False)


# In[ ]:




