minimum <- function(m) {
  return(c(min(m), which(m == min(m), arr.ind = TRUE)))
}

# prints
print(minimum(matrix(c(3,5,7,1,2,5,7,3), nrow=2)))
print(minimum(matrix(c(4,1,7,3,5,7,2,3), nrow=4)))