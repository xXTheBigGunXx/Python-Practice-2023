import matplotlib.pyplot as plt

x = list(range(0, 10))
y = list(range(-10, 0))

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
plt.show()