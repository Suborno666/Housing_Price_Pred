import numpy as np

n_samples = 5
n = np.random.normal(2, 3, n_samples)

# Format the array as a comma-separated string
formatted_n = ', '.join([str(x) for x in n])

# Print the formatted string
print("Formatted values:", formatted_n)

mean = sum(n)/n_samples

print("Mean:", mean)

print("SD: ",np.std(n))
