import torch
from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure, morphology
import numpy as np
import scipy.ndimage
import cv2
#from matplotlib import pyplot
from torchvision.transforms import transforms
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
ToTensor=transforms.ToTensor()


if __name__ =="__main__":
	path='./train/'
	move_cnt=0
	last_sum=100000
	image=[]
	for i in range(2000):
		now_slice=(ToTensor(Image.open(path+('%05d'%i)+'_mask.png'))[0])
		now_sum = int(torch.sum(now_slice.int()))
		if not(last_sum-now_sum<1 and last_sum-now_sum>-1):
			last_sum=now_sum



			img_gen=np.zeros((80,80))
			sx = 0
			sy = 0
			for h in range(80):
				for w in range(80):
					if(now_slice[h][w] == 1):
						sx = h
						break
			for w in range(80):
				for h in range(80):
					if(now_slice[h][w] == 1):
						sy = w
						break
			print(sx,sy)
			for h in range(-40, 40):
				for w in range(-40, 40):
					if sx +h < 0 or sy + w < 0 or sx + h >79 or sy + w >79 :
						img_gen[40+h][40+w] = 0
					else :
						#print([sx+h-20],[sy+w-20])
						# print([sx+h-20],[sy+w-20])
						# print(img_gen.shape)
						img_gen[40+h][40+ w] = now_slice[sx+h][sy+w]*255
			path_gen='/fdisk/22/modset/'+str(move_cnt).zfill(5)+'_mask.png'

			cv2.imwrite(path_gen,img_gen)
			move_cnt+=1
		else :
			continue
	print(move_cnt,len(img_set))
	img_set.sort()
	image= (torch.stack([one,one,one],dim=0)*255).numpy()
