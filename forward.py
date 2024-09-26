import torch


checkpoint = torch.load('dht_r50_nkl_d97b97138.pth', map_location=torch.device('cpu'))
