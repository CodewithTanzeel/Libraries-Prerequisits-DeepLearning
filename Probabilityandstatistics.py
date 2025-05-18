# Random sampling
samples = np.random.normal(0, 1, 1000)  # 1000 samples from N(0,1)

# Basic statistics
mean = np.mean(samples)
std = np.std(samples)
percentile = np.percentile(samples, 95)  # 95th percentile

# Probability distributions
from scipy.stats import norm
x = np.linspace(-4, 4, 100)
pdf = norm.pdf(x, 0, 1)  # PDF of N(0,1)
cdf = norm.cdf(x, 0, 1)  # CDF of N(0,1)

# Hypothesis testing
from scipy.stats import ttest_ind
group1 = np.random.normal(0, 1, 100)
group2 = np.random.normal(0.5, 1, 100)
t_stat, p_value = ttest_ind(group1, group2)