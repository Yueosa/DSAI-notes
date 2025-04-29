import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm


x = torch.tensor([[1.0], [1.0], [3.0], [4.0]])
y = torch.tensor([[5.0], [7.0], [9.0], [11.0]])

model = nn.Linear(1, 1)

loss_fn = nn.MSELoss()

optimizer = optim.SGD(model.parameters(), lr = 0.01)

for epoch in tqdm(range(300), desc='训练进度'):
    y_pred = model(x)

    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        tqdm.write(f"Epoch {epoch + 1}: loss = {loss.item():.4f}")

print(f"Learned weight: {model.weight.item():.4f}")
print(f"Learned bias: {model.bias.item():.4f}")
