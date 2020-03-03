#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:42:07 2020

@author: xingwenpeng
"""
import csv
import pandas as pd

filePath="/Users/xingwenpeng/Desktop/nlp/csvdata/dfbeforeSG.csv"
filePath2="/Users/xingwenpeng/Desktop/nlp/results/deleted text.csv"
filePath3="/Users/xingwenpeng/Desktop/nlp/results/deletedText2.csv"
fh = open(filePath, encoding='utf-8')   # 要检测文章的路径
data = csv.reader(fh)  # 打开文章


fh2 = open(filePath2, encoding='utf-8')   # 要检测文章的路径
data2 = csv.reader(fh2)  # 打开文章

fh3 = open(filePath3, encoding='utf-8')   # 要检测文章的路径
data3 = csv.reader(fh3)  # 打开文章




date = list([row[7] for row in data])

dt1= list([row[0] for row in data2])

dt2= list([row[0] for row in data3])

i=0

result=[]

for row in date:
    i=i+1
    print(i)
    if str(i) not in dt1 and str(i) not in dt2:
       result.append(row)
    
    
df = pd.DataFrame(result)
excel_out_put_path="/Users/xingwenpeng/Desktop/nlp/results/dateAfterDL.xlsx"
df.to_excel(excel_out_put_path, index=False)
