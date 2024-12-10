import matplotlib.pyplot as plt
import numpy as np

my_dict = {"A" : 1,
           "B" : 2,
           "C" : 3,
           "D" : 4,
           "E" : 5,
           "F" : 6}

plt.style.use('_mpl-gallery')

fig, ax = plt.subplots()

for words, count in my_dict.items():
    ax.bar(words, count, width=1, edgecolor="white", linewidth=0.7)

plt.show()