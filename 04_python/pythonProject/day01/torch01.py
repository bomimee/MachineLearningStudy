# 파이토치
# facebook 에서 개발
# 오픈 소스 딥러닝 라이브러리
# 강력한 GPU 가속화를 통한 Tensor 계산
# 설치 : 아나콘다에서 설치 :터미널에서 conda install pytorch torchvision torchaudio -c pytorch
#        pip를 이용해서 설치 : pip install torch
import torch
import numpy as np

# a.shape : 모양확인
# a.dim() : 차원확인
# a.size() : 크기 확인
# print(a[:5],a[3:]) : 슬라이싱 가능
a = torch.tensor(np.arange(10)) #numpy를 통한 생성
b = torch.FloatTensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) #tensor 자체 생성

print(a.shape, b.shape)
print(a.size(), b.size())
print("-" * 100)

print(a.dim(), b.dim())
print("-" * 100)

# 슬라이싱
print(a[:5]) # 0-4
print(a[3:]) # 3-9
print("-" * 100)

# torch.FloatTensor 는 PyTorch에서 사용되는 데이터 타입 중 하나 , 딥러닝 모델을 구현할 때 주로 사용
# torch.FloatTensor 는 실수로 이루어진 텐서를 의미한다.
# torch.FloatTensor 는 다차원 배열로써, Numpy의 배열과 유사
# 다차원배열 : 1차원(벡터), 2차원(행렬), 3차원(텐서)

# 1차원 텐서 생성
tensor1d = torch.FloatTensor([1.0,2.0,3.0])
print(tensor1d, tensor1d.shape, tensor1d.size())
print("-" * 100)

# 2차원 텐서 생성
tensor2d = torch.FloatTensor([[1.0, 2.0],[3.0,4.0]])
print(tensor2d, tensor2d.shape, tensor2d.size())
print("-" * 100)

# 3차원 텐서 생성
tensor3d = torch.FloatTensor([[[1.0,2.0],[3.0,4.0]],[[5.0,6.0],[7.0,8.0]]])
print(tensor3d, tensor3d.shape, tensor3d.size())
print("-" * 100)

a = torch.FloatTensor([[1,1]])
b = torch.FloatTensor([[6,6]])
print(a+b)  # tensor([[7., 7.]]) => index에 맞춰서 연산이 이루어짐
print("-" * 100)

a = torch.FloatTensor([[1,10]])
b = torch.FloatTensor([[6]])
print(a+b)  # tensor([[7., 16.]]) => 벡터의 모든 index에 스칼라를 더함
print("-" * 100)

# a = 1 * 2,  b = 2 * 1
# 브로드 캐스팅 : 작은 텐서의 크기를 자동으로 큰 텐서의 크긱와 맞추는 것
a = torch.FloatTensor([[1,7]])
b = torch.FloatTensor([[5], [6]])

# a = [[1,7], [1,7]]
# b = [[5,5], [6,6]]

# [[1,7],  +   [[5,5],
# [1,7]]      [6,6]]
# ==================
#  [[1+5, 7+5 ],
#   [1+6, 7+6]]
print(a + b)
print("-" * 100)

## 행렬 곱셈
a = torch.FloatTensor([[1,2], [3,4]])
b = torch.FloatTensor([[1], [2]])

# a의 첫번째 행과 b의 첫번째 열
# 1 * 1 + 2 * 2 = 5

# a의 두번째 행과 b의 첫번째 열
# 3*1 + 4*2 = 11
## 행렬곱셈
print(a.matmul(b))
print("-" * 100)

# 브로드 캐스팅 후 같은 위치에 있는 것 끼리 계산
#  [[1,2],   * [[1,1]
#   [3,4]]      [2,2]]
# ===========
#  [[1*1, 2*1], [3*2, 4*2]] = [[1,2], [6,8]]

## 곱셈
print(a*b)
print("-" * 100)

print(a.mul(b))
print("-" * 100)
