from PIL import Image
from pylab import *

im = array(Image.open('capture.jpg').convert('L'))
figure()
gray()
contour(im, origin='image')
show()
