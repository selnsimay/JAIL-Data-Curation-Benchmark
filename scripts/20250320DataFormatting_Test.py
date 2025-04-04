#imports 
import sys
import os
import transformers
from transformers import pipeline
import json
import torch
import numpy as np
from torch.utils.data import DataLoader , Dataset

sys.path.append("../")

#loading the data 
data = json.load(open("../data/geneset_dict.json"))
