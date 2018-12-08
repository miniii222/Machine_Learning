import numpy as np

np.array([1,2,3,4])
np.arange(2*2).reshape(2,2)


#1
def n_size_ndarray_creation(n, dtype=np.int):
    X=np.arange(n*n).reshape(n,n)
    return X

n_size_ndarray_creation(3)


#2
def zero_or_one_or_empty_ndarray(shape, type, dtype=np.int):
    if type == 0 :
        X = np.zeros(shape = shape)
        return X
    elif type == 1 :
        X = np.ones(shape = shape)
        return X
    elif type == 99 :
        X = np.empty(shape = shape)
        return X
    else :
        print("error")
        
zero_or_one_or_empty_ndarray((2,2),0)
zero_or_one_or_empty_ndarray((3,3),1)
zero_or_one_or_empty_ndarray((4,4),99)
zero_or_one_or_empty_ndarray((3,3),87)


#3
X = np.ones((4,4), dtype = np.int)

def change_shape_of_ndarray(X, n_row):
    return X.flatten() if n_row==1 else X.reshape(n_row,-1)

change_shape_of_ndarray(X, 1)
change_shape_of_ndarray(X, 8)


#4
def concat_ndarray(X_1, X_2, axis):
    try :
        if X_1.ndim==1 :
            X_1 = X_1.reshape(1,-1)#1차원 배열을 2차원으로 변형
        if X_2.ndim==1 :
            X_2 = X_2.reshape(1,-1)

        return np.concatenate((X_1,X_2), axis = axis)

    except ValueError :
        return False
"""
나는 이렇게 짬.. concatenate로 한 번에!
    if axis ==0 :
        if X_1.shape[1]==X_2.shape[1] :
            return np.vstack([X_1, X_2])
        else :
            print("Fasle")
    elif axis ==1 :
        if X_1.shape[0]==X_2.shape[0] :
            return np.hstack([X_1, X_2])
        else :
            print("False")
if - print로 하지 말고, try - except로!
"""


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
concat_ndarray(a, b, 0)
concat_ndarray(a, b, 1)

a = np.array([1, 2])
b = np.array([5, 6, 7])

concat_ndarray(a, b, 1)
concat_ndarray(a, b, 0)


#5
X = np.arange(12, dtype=np.float32).reshape(6,2)
X

def normalize_ndarray(X,axis, dtype=np.float32):
    if axis == 99 :
        return (X-np.mean(X))/np.std(X)
    elif axis == 0 :
        return (X-np.mean(X, axis=0))/np.std(X, axis=0)
    elif axis == 1 :
        return (X-np.mean(X, axis=1).reshape(X.shape[0],1))/np.std(X, axis=1).reshape(X.shape[0],1)

#n_row, n_col = X.shape

normalize_ndarray(X,99)
normalize_ndarray(X,1)
normalize_ndarray(X,0)


#6

X = np.arange(32, dtype=np.float32).reshape(4, -1)
X
def save_ndarray(X, filename):
    np.save(filename,X)
    
save_ndarray(X, "test.npy")

X2=np.load("test.npy") #다시 불러오기
X2


#7
X = np.arange(32, dtype=np.float32).reshape(4, -1)

def boolean_index(X, condition):
   #eval : string타입으로 넣어주면, 코드로 리턴
   condition = eval(str("X")+condition)
   return np.where(condition) #np.where(조건) : 조건을 만족시키는 index 리턴
   
boolean_index(X, "== 3")
boolean_index(X, "> 6")


#8
X = np.random.uniform(0, 1, 100)

def find_nearest_value(X, target_value):
    abs_X = np.abs(X-target_value)
    print(X[abs_X == min(abs_X)])
    
find_nearest_value(X, 0.5)


#9

X = np.random.uniform(0, 1, 5)
np.argsort(X) #작은 수의 index부터
np.argsort(X)[::-1] #거꾸로 배열

def get_n_largest_values(X, n):
    return X[np.argsort(X[::-1])[:n]]

#numpy에서 arg가 붙으면, 해당 조건을 만족시키는 index 리턴

    
"""    
내가 짠 코드
    sorted_X = -np.sort(-X)
    print(sorted_X[:n])
"""    
get_n_largest_values(X, 10)
