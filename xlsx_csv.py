import os
import pandas as pd


IN_dirPath = r"C:\Users\Raywang\Desktop\new"   #輸入檔案路徑
OUT_dirPath = r"C:\Users\Raywang\Desktop\output"   #輸出檔案路徑




FILES_NAME=os.listdir(IN_dirPath)
print(FILES_NAME)
data_xls = pd.read_excel(os.path.join(IN_dirPath,FILES_NAME[0]), index_col=None)
FILES_NAME_OUT=FILES_NAME[0][:5]+'.csv'
print(FILES_NAME_OUT)
data_xls.to_csv(os.path.join(OUT_dirPath,FILES_NAME_OUT),encoding='utf-8')

