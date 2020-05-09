import torch
from PIL import Image
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure, morphology
import numpy as np
import scipy.ndimage
import cv2


import time

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
		if(now_sum<20):
			print('point<20',i)
			continue
		if not(last_sum-now_sum<1 and last_sum-now_sum>-1):
			last_sum=now_sum



			img_gen=np.zeros((80,80))
			sx = 0
			sy = 0



			point_cnt=0
			sum_h=0
			sum_w=0
			for h in range(80):
				for w in range(80):
					if(now_slice[h][w] == 1):
						point_cnt+=1
						sum_w+=w
						sum_h+=h

			sx=sum_w//point_cnt
			sy=sum_h//point_cnt
				# if(find==1):
				# 	break

				# if(find==1):
				# 	break

			# print(sx,sy)
			# plt.imshow(now_slice,cmap='Greys_r')
			# plt.show()
			# time.sleep(1)
			for h in range(-40, 40):
				for w in range(-40, 40):
					if sx +w < 0 or sy + h < 0 or sx + w >79 or sy + h >79 :
						img_gen[40+h][40+w] = 0
					else :
						#print([sx+h-20],[sy+w-20])
						# print([sx+h-20],[sy+w-20])
						# print(img_gen.shape)
						img_gen[40+h][40+w] = now_slice[sy+h][sx+w]*255
			path_gen='/fdisk/22/modset2/'+str(move_cnt).zfill(5)+'_mask.png'
			print(i)

			cv2.imwrite(path_gen,img_gen)
			move_cnt+=1
		else :
			continue
	print(move_cnt)
