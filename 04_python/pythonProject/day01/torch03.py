## PyTorch에서의 회귀 분석

# 라이브러리 불러오기
import torch
import torch.nn as nn              # 신경망 클래스 호출
import torch.nn.functional as F    # 신경망 클래스 내의 손실함수, 활성화 함수등 을 가지고 는 패키지
import torch.optim as optim        # 최적화 알고리즘을 위한 패키지

## PyTorch를 사용하여 간단한 인공 신경만을 정의한 예제

## nn.Module클래스를 상속 받은 클래스
class Model(nn.Module):
    # 생성자 함수
    def __init__(self):
        # 부모클래스 생성자 호출
        super().__init__()
        # 입력차원 3 이고, 출력 1인 선형 레이어 => 3개 받아서 1출력
        self.linear = nn.Linear(3,1)


    def forward(self, x):
        return self.linear(x)

