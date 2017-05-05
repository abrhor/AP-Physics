import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

intra = np.array([
        353,
        737,
        492,
        1284,
        379,
        568,
        505,
        711,
        2041,
        294,
        1326,
        302,
        903,
        304,
        1152,
        616,
        366,
        2039])
intra = np.array([float(i) for i in intra])

inter = np.array([
        739,
        268,
        399,
        954,
        583,
        169,
        949,
        1382,
        855,
        586,
        907,
        366,
        1585,
        1182,
        276,
        616,
        169,
        386,
        1732,
        351,
        292,
        526,
        62,
        256,
        218])

inter = np.array([float(i) for i in inter])

plt.hist(intra)
plt.xlabel("Final Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Final Scores of Players with Intrapersonal Personalities")

plt.hist(inter)
plt.xlabel("Final Scores")
plt.ylabel("Frequency")
plt.title("Distribution of Final Scores of Players with Interpersonal Personalities")
