import numpy as np
import torch
from PIL import Image

a = np.random.randint(0,10)
s = np.random.randint(a,10)
b = s - a

def create_new():
    global a, b, s
    a = np.random.randint(0,10)
    s = np.random.randint(a,10)
    b = s - a

def create_tensor(arr):
    # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    device = torch.device("cpu")
    img = Image.fromarray(np.uint8(arr[:,:,3]))
    img_arr = np.asarray(img.resize((28,28)))
    img_arr_tensor = torch.from_numpy(img_arr).type(torch.FloatTensor)
    img_arr_tensor = img_arr_tensor.view(-1,1,28,28)
    img_arr_tensor = img_arr_tensor.to(device)

    return img_arr_tensor