import math
import xlrd
import xlsxwriter
import pandas as pd
import numpy as np
import mixed
confidence = 0.95
ca= 0
vd = np.zeros((1,10))


data = np.array(pd.read_excel('pige2.xls',header=None))
print(data.shape)
for j in range(0,9):
    ca= 0
    for m in range(0,9):
     
        MI = mixed.Mixed_KSG(data[:,j],data[:,m])
        ca = np.hstack((ca,MI));
        print(ca)
    
    vd = np.vstack((vd,ca));


vd = np.delete(vd,(0),axis = 1);
vd = np.delete(vd,(0),axis = 0);


workbook = xlsxwriter.Workbook('MI.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for col, data in enumerate(vd.T):
    worksheet.write_column(row, col, data)
workbook.close()
