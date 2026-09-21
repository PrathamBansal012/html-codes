import scipy.stats as stats
prob=1-stats.binom.cdf(6,10,0.5)
print("probability of getting heads in a row is",prob)