import math 
import torch.nn as nn
import torch.utils.model_zoo as model_zoo

class Bottleneck(nn.Module):
  expansion = 4
  def __init__(self, inplanes)

class ResNet(nn.Module):
  def __init__(self, arch, block, layers, )

def FPN50(output_stride, BatchNorm=nn.BatchNorm2d, pretrained=True):
  """
  Construct a ResNet-50 model.
  Args:
    pretrained (bool): If True, returns a model pre-trained on ImageNet
  """
  model = ResNet('resnet50', Bottleneck, [3,4,6,3], output_stride, BatchNorm, pretrained=pretrained)