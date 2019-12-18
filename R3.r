smooth <- function(x) {
  m <- mean(x)
  return (ifelse(x > m * 3, m, x))
}

print(smooth(c(1, 1, 5, 8, 13, 21, 15, 52, 7, 5, 3, 93)))
print(smooth(c(3,1,5,7,3,5,1,35,1,7,5,61,9)))
print(smooth(c(2,3,1,4,7,2,80,293)))
print(smooth(c(1,2,3,7,4,9,7,5,6)))