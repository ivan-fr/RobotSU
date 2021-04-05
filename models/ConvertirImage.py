from PIL import Image
import numpy

class ConvertirImage(object):
    def __init__(self, lienImage):
        """passer le lien de limage en str"""
        self.image = lienImage
    
    def convertirImageToArray(self):
        im_1 = Image.open(self.image)
        ar = numpy.array(im_1)
        return ar