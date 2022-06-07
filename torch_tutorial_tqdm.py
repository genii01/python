import torch
from torch import nn
import torch.nn.functional as F

class Perceptron(nn.Module):
 def __init__(self):
     super().__init__()
     self.dropout2 = nn.Dropout(0.5)
     self.fc1 = nn.Linear(28 * 28, 128)  # 9216
     self.fc2 = nn.Linear(128, 10)

 def forward(self, x):
     x = torch.flatten(x, 1)
     x = self.fc1(x)
     x = F.relu(x)
     x = self.dropout2(x)
     x = self.fc2(x)
     output = F.log_softmax(x, dim=1)
     return output


import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.optim import Adam
from torch import nn

transform=transforms.Compose([
 transforms.ToTensor(),
 transforms.Normalize((0.1307,), (0.3081,))
])
train_data = datasets.MNIST('./mnist_data', train=True, download=True,
                      transform=transform)

test_data = datasets.MNIST('./mnist_data', train=False, download=True,
                      transform=transform)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = Perceptron().to(device)

optimizer = Adam(model.parameters())
criterion = nn.CrossEntropyLoss()
batch_size = 64

train_loader = DataLoader(train_data,
                       batch_size=batch_size,
                       pin_memory=True,
                       shuffle=True,
                       drop_last=True)

test_loader = DataLoader(test_data,
                        batch_size=batch_size,
                        pin_memory = True,
                        shuffle = True,
                        drop_last =True)


# initialization loss_fct & optimizer

loss_fct = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 2e-2)

device = 'cuda' if torch.cuda.is_available() else 'cpu'

from tqdm import tqdm

def train_loop(data_loader, model, loss_fct, optimizer, epoch):
    with tqdm(data_loader, unit = 'batch') as tepoch:
        for X, y in tepoch:
            tepoch.set_description(f'epoch : {epoch}')
            
            X, y =X.to(device), y.to(device)
            pred = model(X)

            loss = loss_fct(pred, y)
            correct = (pred.argmax(dim=1).squeeze() == y).sum().item()
            accuracy = correct/ batch_size

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            tepoch.set_postfix(loss = loss.item(), accuracy = 100*accuracy)

for epoch in range(1,5):
    train_loop(train_loader, model, loss_fct, optimizer, epoch)