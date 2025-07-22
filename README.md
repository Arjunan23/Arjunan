# 📡 Signal Analysis Prank Script
# 🎯 Objective: Calculate the probability that a signal > 240μV,
#              given it is already > 210μV
# Signal is modeled as: X ~ N(μ = 200, σ² = 256)

import scipy.stats as stats

# Step 1: Define mean and standard deviation
mu = 200               # Mean of the signal in microvolts
sigma = 16             # Standard deviation (sqrt of variance 256)

# Step 2: Define conditional values
x1 = 240               # Target value to exceed
x2 = 210               # Given it's already more than this

# Step 3: Convert to Z-scores (standard normal)
z1 = (x1 - mu) / sigma     # Z for 240
z2 = (x2 - mu) / sigma     # Z for 210

# Step 4: Get probabilities from standard normal table
p_x_gt_240 = 1 - stats.norm.cdf(z1)    # P(X > 240)
p_x_gt_210 = 1 - stats.norm.cdf(z2)    # P(X > 210)

# Step 5: Apply conditional probability formula
# P(X > 240 | X > 210) = P(X > 240) / P(X > 210)
p_conditional = p_x_gt_240 / p_x_gt_210

# Step 6: Print final result
print("📈 Conditional Probability:")
print(f"P(X > 240 | X > 210) = {p_conditional:.4f} or {p_conditional*100:.2f}%")

# 👻 Bonus prank line (for the video)
print("\n😲 OMG! There's only a {:.2f}% chance the signal exceeds 240μV —".format(p_conditional*100))
print("     ...if it's already a MONSTER over 210μV! 😱📶")
