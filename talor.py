import math

def erf_taylor(x, terms=5):
    result = 0
    for n in range(terms):
        result += ((-1)*n) * (x*(2*n + 1)) / (math.factorial(n) * (2*n + 1))
    return result * (2 / math.sqrt(math.pi))

def cdf_taylor(mean, std_dev, x, terms=5):
    z = (x - mean) / (std_dev * math.sqrt(2))
    erf_value = erf_taylor(z, terms)
    return 0.5 * (1 + erf_value)

means = [10, 11, 12, 33, 14]
std_devs = [1, 2, 5]

x_value = 26 

for mean in means:
    for std_dev in std_devs:
        cdf_value = cdf_taylor(mean, std_dev, x_value)
        print(f"Mean: {mean}, Std Dev: {std_dev}, CDF({x_value}): {cdf_value:.6f}")