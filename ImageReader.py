import numpy as np
import os
import scipy.misc as misc
#####################################################################################################################################
def LoadImages(ImageName,Im_Hight,Im_Width,SamplingRate): # load image and return image and sparsely sample image
    Img=misc.imread(ImageName)
    if (Img.ndim==2):
        Img=np.expand_dims(Img,3)
        Img = np.concatenate([Img, Img, Img], axis=2)
    if Im_Hight>0 and Im_Width>0:
        Img = misc.imresize(Img, [Im_Hight,Im_Width], interp='bilinear')
    Img=Img[:,:,0:3]
    SampledImage=CreateSampledImage(Img,SamplingRate)
    Img= np.expand_dims(Img, axis=0)
    SampledImage = np.expand_dims(SampledImage, axis=0)
    return Img,SampledImage

#############################################################################################################################################
def CreateSampledImage(I,SamplingRate): #Sparsely sample pixels from image I for training
    Sy, Sx, t = I.shape
    SampleMap = (np.random.rand(Sy, Sx,1) < SamplingRate)
    ii = np.concatenate([SampleMap, SampleMap, SampleMap], axis=2)
    SparseIm=I.copy()
    SparseIm[ii==False]=0
    return SparseIm
#
