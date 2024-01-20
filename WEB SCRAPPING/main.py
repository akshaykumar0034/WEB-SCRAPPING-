import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

name = input("Enter Here : ")
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys(name)
driver.find_element(By.ID, "nav-search-submit-button").click()

products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

product_name = []
product_price = []
no_reviews = []
product_discount = []
final_list = []

for product in products:

    names = product.find_elements(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    for name in names:
        product_name.append(name.text)

    try:
        if len(product.find_elements(By.XPATH, ".//span[@class='a-price-whole']")) > 0:
            prices = product.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
            for price in prices:
                # print('the lenght is ===>',len(price.text))
                product_price.append(price.text)
        else:
            product_price.append("0")
    except:
        pass

    try:
        if len(product.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")) > 0:
            reviews = product.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")
            for review in reviews:
                no_reviews.append(review.text)
        else:
            no_reviews.append("0")
    except:
        pass

print('Number of Products==>', len(product_name))
print('Number of prices==>', len(product_price))
print('Number of reviews==>', len(no_reviews))

existing_df = pd.read_excel(r"E:\SEM 3\laptop.xlsx")
new_data = pd.DataFrame(zip(product_name, product_price, no_reviews), columns=['Product_Name','Product_Price', 'Reviews'])
combined_df = pd.concat([existing_df,new_data],ignore_index=True)

combined_df.to_excel(r"E:\SEM 3\laptop.xlsx", index=False)

driver.quit()





