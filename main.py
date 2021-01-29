# import matplotlib for plotting
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.colors for mapping numbers with colors
from matplotlib.colors import LogNorm

#declare two variable for changing x and y coordinates
dx, dy=0.015, 0.05


x=np.arange(-4.0, 4.0,dx)
y=np.arange(-4.0, 4.0,dy)

x,y = np.meshgrid(x,y)  #meshgrid used to import rectangular grid

extent=np.min(x), np.max(x), np.min(y), np.max(y)

Z1=np.add.outer(range(8),range(8))%2

plt.imshow(Z1, cmap="binary_r", interpolation='nearest',
           extent=extent,alpha=1)

def plot(x,y):
    return(1 - x/2 + x**5  +y  **6)* np.exp(-(x**2 + y**2))


Z2=plot(x,y)

plt.imshow(Z2,alpha=0.7, interpolation='bilinear', extent=extent) #Matplotlib allows you to adjust the transparency of a graph plot using the alpha attribute.

#for plotting
plt.cool()

plt.title('matplotlib.pyplot.cool function Example',fontweight="bold")
plt.show() #showing the plotted graph