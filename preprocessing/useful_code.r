#1.column na 한번에 보여주기
library(dplyr)

df %>% select(everything()) %>%  # select every columns

summarise_all(funs(sum(is.na(.))))

colSums(is.na(df))

#2.변수 이름 그대로 적용하기
##ex
a=5
print(a) #5출력
print(deparse(substitute(a)) #a출력
