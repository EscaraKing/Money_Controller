import numpy as np
import pandas as pd

money_list = []

adding_list = input("추가할 리스트를 입력하세요\n")
goal_money = input("목표금액을 입력하세요\n")
explaing_text = input("추가설명을 입력하세요\n")

temp_element = (adding_list, int(goal_money), explaing_text)
print(temp_element)
df = pd.DataFrame(temp_element)
df.to_csv("data.csv", index=False, encoding='utf-8')
print(df, df.shape)