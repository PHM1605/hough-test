import torch 
import numpy as np
import torch.nn as nn

class Net(nn.Module):
  def __init__(self, numAngle, numRho, backbone):
    super(Net, self).__init__()
    if backbone == 'resnet50':
      self.backbone = FPN50