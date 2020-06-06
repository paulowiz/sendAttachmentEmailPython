from PIL import Image
import io,os
import pandas as pd
import numpy as np

class funcoes:
    def __init__(self): 
        funcoes = 0 
    
    def convertToBinaryData(self,filename):
        image = Image.open(filename)
        buf = io.BytesIO()
        image.save(buf, format='PDF',save_all=True)
        byte_im = buf.getvalue()
        return byte_im
    
    def insereDf(self,df,row):  
        insert_loc = df.index.max()
        columns = df.shape
        i = 0
        for reg in row:
            i = i +1
        for r in range(columns[1]-i):
            row.append('')    
        if np.isnan(insert_loc):
           df.loc[0] = row
        else:
           df.loc[insert_loc + 1] = row
           
    def geraExcel(self,df,nomeXls,pasta):
        if not os.path.isdir(pasta):
           os.makedirs(pasta)
        df.to_excel(r'%s/%s.xls'%(pasta,nomeXls), index = False)
        
pass
        