# Bayesian Optimizaiton

## Hyperparameter Optimizaiton 이란?
- hyperparameter의 최적값을 탐색하는 문제.
- 기존에는 주로 manual search, grid search, random search 이용.
[image](https://i.stack.imgur.com/cIDuR.png)
- 기존의 방법들은 다음 후보 hyperparameter를 선정하는데 있어, 이전까지 조사했던 값들은 반영되지 않음.
- `Bayesian Optimization`은 간단히 말해, 매 회 새로운 hyperparameter선정 시, 사전 지식을 반영하여 수행하는 방법

## Bayesian Optimization
- 어느 입력값 x를 받는 objective fucntion f를 상정하여, 그 함수값 f(x)를 최대로 만드는 최적해 x*를 찾는 것을 목적으로 한다.
- 가능한 적은 수의 입력값 후보들에 대하여 그 함수값을 순차적으로 조사하여 빠르고 순차적으로 최적해를 찾아준다.
- `Surrogate Model`과 `Acquisition Function`이용하여 최적의 값을 찾아준다.

### Alogorithm
![image](http://research.sualab.com/assets/images/bayesian-optimization-overview-1/bayesian-optimization-algorithm.png)

### Surrogate Model
- 현재까지 조사된 입력값-함숫값 점들을 바탕으로 미지의 목적 함수의 대략적인 형태에 대한 확률적인 추정을 수행
- 가장 많이 사용되는 확률 모델이 `Gaussian Process(GP)`
![image](http://research.sualab.com/assets/images/bayesian-optimization-overview-1/bayesian-optimization-procedure-example.png)

  - 검은색 실선 : x위치 별 평균
  - 파란색 구간 : 표준편차
  - 조사된 점에서 가까운 위치에 있으면 분산이 작고(불확실성이 작고), 멀 수록 분산이 크다(불확실성이 크다)
  
 
### Acquisition Function
- Surrogate Model이 확률적으로 추정한 현재까지의 결과를 바탕으로, 다음 번에 함숫값을 조사할 후보 x_(t+1)를 추천해주는 함수
![image](http://research.sualab.com/assets/images/bayesian-optimization-overview-1/bayesian-optimization-procedure-example-teq2.png)
- x_(t+1)는 x*를 찾는 데 있어 가장 유용할 만한 것
#### Exploitation(착취)
- 함숫값이 더 큰 점 근방에서 실제 최적 입력값 x*를 찾을 가능성이 높을 것이다
- 함숫값이 최대인 점 근방에서 탐색
#### Exploration(탐색)
- 불확실한 영역에 optimal value x*가 있을 수 있으므로, 추가로 탐색해야 한다.

- Exploration과 Exploitation은 trade-off


### 참고 자료
- 한글 blog [link](http://research.sualab.com/introduction/practice/2019/02/19/bayesian-optimization-overview-1.html)
- Lancaster University [pdf](http://gpss.cc/gpmc17/slides/LancasterMasterclass_1.pdf)
- towarddatascience [link](https://towardsdatascience.com/the-intuitions-behind-bayesian-optimization-with-gaussian-processes-7e00fcc898a0)
- 논문
