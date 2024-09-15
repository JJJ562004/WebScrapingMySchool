from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://daotao.ute.udn.vn/viewlhpdksv.asp")

row_data_list_class = [row.text for row in driver.find_elements(By.XPATH, value='//*[@id="inner-column-container"]/div[2]/div[2]/table/tbody/tr')]
row_data_list_class_removed = [r.split(' ') for r in [row.replace('\n', ' ') for row in row_data_list_class[1:]]]
for r in row_data_list_class_removed:
    r[len(r)-1] = r[len(r)-1].replace('-', '')

df = pd.DataFrame(
    {
        'Mã học phần': [row[1] for row in row_data_list_class_removed],
        'Tên lớp học phần': [row[2] for row in row_data_list_class_removed],
        'Phòng': [row[len(row) - 5] for row in row_data_list_class_removed],
        'Max': [row[len(row) - 4] for row in row_data_list_class_removed],
        'Min': [row[len(row) - 3] for row in row_data_list_class_removed],
        'Ngày': [row[len(row) - 1] for row in row_data_list_class_removed],

    }
)

df.to_csv('out.csv')