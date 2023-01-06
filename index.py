from PIL import Image
from utils import in_file,out_file

# Imagem = Image.open(in_file("baloes.jpg"))
# Imagem.show()

# def quadro(size,color):
#     fundo = Image.new("RGB",(size,size),"green")
#     metade = size//2
#     for x in range(size):
#         if(x <= metade):
#             for y in range(size):
#                 fundo.putpixel((x,y),color)
#     fundo.show()

# quadro(200,(255,255,255))

# ===============================

def Encontrando(corEncontrada,corTrocada):
    Imagem = Image.open(in_file("baloes.jpg"))
    w,h = Imagem.size
    quantidade = 0
    local = []
    for x in range(w):
        for y in range(h):
            pa = Imagem.getpixel((x,y))
            if(pa == corEncontrada):
                Imagem.putpixel((x,y),corTrocada)
                quantidade += 1
                local.append((x,y))
    Imagem.save(out_file("Baloes-PretosEncontrados.jpg"))
    print("Da cor {} foi encontrado {}  nos pixels: {}".format(corEncontrada,quantidade,local))
    Imagem.show()

Encontrando((0,0,0),(255,255,0))