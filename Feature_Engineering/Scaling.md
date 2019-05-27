# Why Scaling
대부분의 경우 데이터에 크기, 단위 및 범위가 매우 다양한 feature들이 포함하게 된다. 대부분의 알고리즘들은 Euclidean거리를 사용하기 때문에 문제가 될 수 있다. 알고리즘들은 단위를 무시하고, 각각의 값들의 크기만 고려하기 때문이다. 따라서, 모든 피쳐들을 동일한 수준으로 가져와야 한다.

# How Scaling
1. Standardization
    - feature들을 평균=0이고, 표준편차=1로 만들어준다.
$$ x-\bar{x} \over \sigma$$
    
2. Normalization
    - 평균이 0이고, -1과 1사이로
$$ x-mean(x) \over max(x) - min(x)$$

3. Min-MAx Scaling
    - 0과 1사이의 값으로
$$ x - min(x) \over max(x) - min(x) $$

4. Unit Vector
$$ x \over \lVert x \rVert $$

# When to Scale
- KNN, PCA 필수!
- gradient descent를 빠르게 계산할 수 있게 해준다.
- Tree base model은 거리기반이 아니기 때문에 필요하지 않다.
- LDA, Naive Bayes은 피쳐들에 가중치를 주므로 그렇게 필요하지는 않다
