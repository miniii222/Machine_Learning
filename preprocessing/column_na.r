library(dplyr)

df %>% select(everything()) %>%  # select every columns
summarise_all(funs(sum(is.na(.))))