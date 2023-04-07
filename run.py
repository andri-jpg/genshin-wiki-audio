import pandas as pd
import csv
import os
import argparse
import wget
from selenium import webdriver
from selenium.webdriver.common.by import By

p = argparse.ArgumentParser()
p.add_argument('--char', '-c', type=str)
p.add_argument('--language', '-l', type=str)
args = p.parse_args()

#use capital on first letter
char = args.char.title()
language=args.language.title()

driver = webdriver.Chrome()
page = "https://genshin-impact.fandom.com/wiki/{}/Voice-Overs/{}".format(char, language)
driver.get(page)
lnks=driver.find_elements(By.TAG_NAME, 'audio')
print(len(lnks))
data = []
for lnk in lnks:
    link = lnk.get_attribute('src')
    data.append(link)

driver.close()

os.system('mkdir ' + char)
os.chdir(char)

for links in data:
    wget.download(links)
