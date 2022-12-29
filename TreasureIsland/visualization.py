# Importing the required modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio.v3 as iio
  
# Generating data for the heat map
map = []#[["0","0","4","4","4"],["0","1T","4M","4","4"],["1","1M","3M","3","5"],["2","1","1","3","5"],["2","2","0","3","5"]]
data = [[0,0,4,4,4],[0,1,4,4,4],[1,1,3,3,5],[2,1,1,3,5],[2,2,0,3,5]]
fig = plt.figure()
# Function to show the heat map
fig, ax = plt.subplots()
im = ax.imshow(data)

texts=[]
for i in range(len(data)):
    text=[]
    for j in range(len(data[0])):
        text.append(ax.text(j, i, "0",ha="center", va="center", color="w"))
    texts.append(text)

def displayText(map):
    for i in range(len(data)):
        for j in range(len(data[0])):
            texts[i][j].remove()
            texts[i][j] = ax.text(j, i, map[i][j],ha="center", va="center", color="w")
    # Used to return the plot as an image rray
    fig.canvas.draw()       # draw the canvas, cache the renderer
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return image

ims=[]
map.append( [["0","0","4A","4","4"],["0","1T","4M","4","4"],["1","1M","3M","3","5"],["2","1","1","3","5"],["2","2","0","3","5"]])
map.append ([["0","0","4","4A","4"],["0","1T","4M","4","4"],["1","1M","3M","3","5"],["2","1","1","3","5"],["2","2","0","3","5"]])
kwargs_write = {'fps':1.0, 'quantizer':'nq'}
iio.imwrite("./powers.gif", [displayText(i) for i in map], duration=1000)
# Displaying the plot
fig.tight_layout()
