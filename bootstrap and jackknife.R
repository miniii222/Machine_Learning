x <-c(8.26, 6.33, 10.4, 5.27, 5.35, 5.61, 6.12, 6.19, 5.2,
      7.01, 8.74, 7.78, 7.02, 6, 6.5, 5.8, 5.12, 7.41, 6.52, 6.21,
      12.28, 5.6, 5.38, 6.6, 8.74)

fun1 <- function(x) sqrt(var(x))/mean(x) #target function
fun1(x)

#######bootsampling
N = 10000 #bootsampling size
boot <-numeric(N)
for (i in 1:N) boot[i] <- fun1(sample(x,replace=T))

mean(boot)
hist(boot)

#95% CI
c(quantile(boot, 0.975), quantile(boot, 0.025))

bias <- mean(boot) - fun1(x)  


#######jacknife
jack <- numeric(length(x)-1)
pseudo <- numeric(length(x))

for (i in 1:length(x)){
  for (j in 1:length(x)){
    
    if(j < i) jack[j] <- x[j]
    else if(j > i) jack[j-1] <- x[j]
    
    pseudo[i] <- length(x)*fun1(x) -(length(x)-1)*fun1(jack)
}
}

mean(pseudo)
hist(pseudo)
