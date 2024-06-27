import torch
import  numpy as np

## Numpy에서 Reshape,  PyTorch에서는 View

a = np.arange(24)
print(a)

# 2행 4열
# -1 자동으로 배치한다.
a = a.reshape(-1,2,4)
print(a)
print("-" * 100)

# 3차원 2행 4열
print(a.shape) # (3,2,4)
print("-" * 100)

b = np.arange(24)
c = torch.FloatTensor(b)
print(c)
print("-" * 100)

print(c.view([-1, 4]))
print("-" * 100)