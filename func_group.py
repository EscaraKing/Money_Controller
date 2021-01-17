#데이터저장

import numpy as np
import pandas as pd
import csv
from bs4 import BeautifulSoup
import urllib
import webbrowser

URL = 'file:///C:/Users/%EA%B9%80%EC%84%9D%EC%A4%91/Desktop/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/Money_Control/interface_code.html'
VERSION = 1.0

def data_save(adding_list, goal_money, explaing_text):

    data_file = open('data.csv', 'a', encoding='utf-8', newline='')
    money_list = []

    temp_element = (adding_list, int(goal_money), explaing_text)

    wr = csv.writer(data_file)
    wr.writerow(temp_element)

    data_file.close()

def data_ques():
    adding_list = input("추가할 리스트를 입력하세요\n")
    goal_money = input("목표금액을 입력하세요\n")
    explaing_text = input("추가설명을 입력하세요\n")
    return (adding_list, goal_money, explaing_text)


def interface_home():
    print("장부정리 프로그램 %s \n"%VERSION)
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(URL)

