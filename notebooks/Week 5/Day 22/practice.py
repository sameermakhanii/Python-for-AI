import pandas as pd
import torch
from torch import nn
import matplotlib.pyplot as plt





students = pd.read_csv("students_100.csv")

x = torch.tensor(
    students[{"study_hours" , "phone_hours"}].value,
    dtype = torch.float32,
)
y = torch.tensor(
    students[{"maths"}].values,
    dtype = torch.float32

)

print("X Shape" , x.shape, "y shape" , y.shape)

torch .manual_seed(42)
model = nn.sequential()