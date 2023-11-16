# -*- coding: utf-8 -*-
"""Another copy of MLOE_code1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oly7uPLwYdFjjweHBzIFySfrBdxGVzcB
"""

import torch
import torch.nn as nn
import sklearn.model_selection as sk
import pandas as pd
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
from sklearn.metrics import mean_absolute_error

meta_data = pd.read_csv('/content/copy_mloe_data - mloe_data.csv')
data = meta_data[['b','c','d','i','j','k']]
print(data.head())

data['l'] = 0.610
data.loc[:99,'l'] = 0.0

train,test = sk.train_test_split(data,train_size = 0.8,shuffle=False)

train1 = train[['b','c','d','l']]
out_train1 = train[['i','j','k']]
test1 =test[['b','c','d','l']]
out_test1= test[['i','j','k']]

import numpy as np
train1arr=np.array(train1)
out_train1arr=np.array(out_train1)
test1arr=np.array(test1)
out_test1arr=np.array(out_test1)
print(out_train1arr)

import torch
import torch.nn as nn
import numpy as np
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.input_layer = nn.Linear(4, 8)
        self.hidden_layer = nn.Linear(8, 8)
        self.hidden_layer = nn.Linear(8, 8)
        self.hidden_layer = nn.Linear(8, 3)

    def forward(self, x):
        x = torch.tanh(self.input_layer(x))
        x = self.hidden_layer(x)
        return x
model = SimpleNN()
num_samples = 8000
input_data = torch.from_numpy(train1arr).float()
output_array = torch.from_numpy(out_train1arr).float()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
num_epochs = 1000
for epoch in range(num_epochs):
    predictions = model(input_data)
    loss = criterion(predictions, output_array)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
num_test_samples = 2001
input_data_test = torch.from_numpy(test1arr).float()

with torch.no_grad():
    predictions = model(input_data_test)
output_array_test = torch.from_numpy(out_test1arr).float()
test_loss = criterion(predictions, output_array_test)

print("Predictions:", predictions)
print("MSE Loss (Test):", test_loss.item())
print("Absolute error Loss (Test):", mean_absolute_error(predictions, output_array_test))

predictions

time1=np.array(meta_data['a'])[8000:]

import matplotlib.pyplot as plt

def graphu(vel,t):
  plt.plot(t, vel)
  plt.xlabel('Time(t)')
  plt.ylabel('U Velocity')
  plt.title('Line Plot of U vs. Time(t)')
  plt.show()

graphu(predictions[:,0],time1)

graphu(test1arr[:,0],time1)

def graphv(vel,t):
  plt.plot(t, vel)
  plt.xlabel('Time(t)')
  plt.ylabel('V Velocity')
  plt.title('Line Plot of V vs. Time(t)')
  plt.show()

graphv(predictions[:,1],time1)

graphv(test1arr[:,1],time1)







"""## ZIG-ZAG"""

zig_data= pd.read_csv('/content/Copy of zig - zig.csv',header=None)
column_names=["a","b","c","d","e","f","g","h","i"]
zig_data.columns = column_names
zig_data

train_zig1=np.array(zig_data[['b','c','d','e']])
train_zig=train_zig1[:8000,:]
test_zig=train_zig1[8000:,:]

out_train_zig1=np.array(zig_data[['g','h','i']])
out_train_zig=out_train_zig1[:8000,:]
out_test_zig=out_train_zig1[8000:,:]

num_samples = 8000
input_data = torch.from_numpy(train_zig).float()
output_array = torch.from_numpy(out_train_zig).float()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
num_epochs = 1000
for epoch in range(num_epochs):
    predictions = model(input_data)
    loss = criterion(predictions, output_array)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
num_test_samples = 2001
input_data_test = torch.from_numpy(test1arr).float()

with torch.no_grad():
    predictions = model(input_data_test)
output_array_test = torch.from_numpy(out_test1arr).float()
test_loss = criterion(predictions, output_array_test)

print("Predictions:", predictions)
print("MSE Loss (Test):", test_loss.item())
print("Absolute error Loss (Test):", mean_absolute_error(predictions, output_array_test))

num_test_samples = 2001
input_data_test = torch.from_numpy(test_zig).float()

with torch.no_grad():
    predictionsz = model(input_data_test)
output_array_test = torch.from_numpy(out_test_zig).float()
test_loss = criterion(predictionsz, output_array_test)

print("Predictions:", predictionsz)
print("MSE Loss (Test):", test_loss.item())
print("Absolute error Loss (Test):", mean_absolute_error(predictionsz, output_array_test))

graphu(predictionsz[:,0],time1)

graphu(out_test_zig[:,0],time1)

graphv(predictionsz[:,1],time1)

graphv(out_test_zig[:,1],time1)

"""## SPIRAL"""

spiral_data= pd.read_csv('/content/spiral_data.csv',header=None)
column_names=["a","b","c","d","e","f","g","h","i","j","k","l"]
spiral_data.columns = column_names
spiral_data

train_spiral1=np.array(spiral_data[['b','c','d','i']])
train_spiral=train_spiral1[:8000,:]
test_spiral=train_spiral1[8000:,:]

out_train_spiral1=np.array(spiral_data[['j','k','l']])
out_train_spiral=out_train_spiral1[:8000,:]
out_test_spiral=out_train_spiral1[8000:,:]

num_samples = 8000
input_data = torch.from_numpy(train_spiral).float()
output_array = torch.from_numpy(out_train_spiral).float()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
num_epochs = 1000
for epoch in range(num_epochs):
    predictions = model(input_data)
    loss = criterion(predictions, output_array)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')
num_test_samples = 2001
input_data_test = torch.from_numpy(test1arr).float()

with torch.no_grad():
    predictions = model(input_data_test)
output_array_test = torch.from_numpy(out_test1arr).float()
test_loss = criterion(predictions, output_array_test)

print("Predictions:", predictions)
print("MSE Loss (Test):", test_loss.item())
print("Absolute error Loss (Test):", mean_absolute_error(predictions, output_array_test))

num_test_samples = 2001
input_data_test = torch.from_numpy(test_spiral).float()

with torch.no_grad():
    predictionssp = model(input_data_test)
output_array_test = torch.from_numpy(out_test_spiral).float()
test_loss = criterion(predictionssp, output_array_test)

print("Predictions:", predictionssp)
print("MSE Loss (Test):", test_loss.item())
print("Absolute error Loss (Test):", mean_absolute_error(predictionssp, output_array_test))

graph(predictionssp[:,0],time1)

graphu(out_test_spiral[:,0],time1)

graphv(predictionssp[:,1],time1)

graphv(out_test_spiral[:,1],time1)



"""## VALIDATION"""

val_data= pd.read_csv('/content/inoutspir.csv',header=None)
column_names=["a","b","c","d","e","f","g","h","i"]
val_data.columns = column_names
val_data

val_data1=np.array(val_data[["b","c","d","i"]])
out_val_data1=np.array(val_data[["b","c","d"]])

res=np.zeros((val_data1.shape[0]+1,3))
res1=torch.from_numpy(res).float()
res1

ini=val_data1[0]
ini=torch.from_numpy(ini).float()
ini

delt=val_data1[:,3]
delt

res[0]=ini[:3]
res1[0]=ini[:3]
res1[0]

for i in range(delt.size):
    res_2d = np.expand_dims(np.append(res[i],delt[i]), axis=0)
    res_2d=torch.from_numpy(res_2d).float()
    with torch.no_grad():
      res1[i+1]=model(res_2d)
    res[i+1]=res1[i+1]

output_array_test = torch.from_numpy(out_val_data1).float()
test_loss = criterion(res1[:10001,:], output_array_test)

print("Predictions:", res1[:10001,:])
print("MSE Loss (Test):", test_loss.item())
print("Absolute error Loss (Test):", mean_absolute_error(res1[:10001,:], output_array_test))

time1=np.array(val_data['a'])

graphu(res1[:10001,0],time1)

graphu(out_val_data1[:10001,0],time1)

graphv(res1[:10001,1],time1)

graphv(out_val_data1[:10001,1],time1)