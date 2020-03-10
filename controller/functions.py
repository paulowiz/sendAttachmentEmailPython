from PIL import Image
import io

class funcoes:
    def __init__(self): 
        funcoes = 0 
    
    def convertToBinaryData(self,filename):
        image = Image.open(filename)
        buf = io.BytesIO()
        image.save(buf, format='PDF',save_all=True)
        byte_im = buf.getvalue()
        return byte_im
        
pass
        