import matplotlib.image as mpimg
import matplotlib.pyplot as plt

path_to_file = '0c5aeb7dd48a110b822c4286325183b2.jpg'
img = mpimg.imread(path_to_file)

plt.imshow(img)
