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

def get_pixels_hu(slices):

    image = np.stack(slices)
    print(image.sum())
    # 转换为int16，int16是ok的，因为所有的数值都应该 <32k
    image = image.astype(np.int16)

    # 设置边界外的元素为0
    #image[image == -2000] = 0

    print(image.shape)
    # 转换为HU单位
    for slice_number in range(len(slices)):

        # intercept = slices[slice_number].RescaleIntercept
        # slope = slices[slice_number].RescaleSlope

        intercept = 25500
        slope = 25500


        if slope != 1:
            image[slice_number] = slope * image[slice_number].astype(np.float64)
            image[slice_number] = image[slice_number].astype(np.int16)

        image[slice_number] += np.int16(intercept)
    print('hu',image.shape)
    print(image.sum())
    return np.array(image, dtype=np.int16)
def resample(image, scan, new_spacing=[1,1,1]):
    # Determine current pixel spacing
    #SliceThickness=0.1
    #PixelSpacing=1
    #spacing = np.array([scan[0].SliceThickness] + scan[0].PixelSpacing, dtype=np.float32)
    spacing = np.array(np.array([2,10,10]), dtype=np.float32)
    
    print('spacing',spacing)

    resize_factor = spacing / new_spacing
    new_real_shape = image.shape * resize_factor
    new_shape = np.round(new_real_shape)
    real_resize_factor = new_shape / image.shape
    new_spacing = spacing / real_resize_factor

    image = scipy.ndimage.interpolation.zoom(image, real_resize_factor, mode='nearest')


    print('re',image.shape,new_spacing)
    return image, new_spacing



def plot_3d(image, threshold=-300):

    # Position the scan upright, 
    # so the head of the patient would be at the top facing the camera
    p = image.transpose(2,1,0)
    print(p.sum())
    verts, faces = measure.marching_cubes_classic(p, threshold)

    #fig = plt.figure(figsize=(10, 10))
    #ax = fig.add_subplot(111, projection='3d')

    fig = plt.figure()
    ax = Axes3D(fig)
    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    print(faces.shape)
    print(verts.shape)
    print(verts[faces].shape)
    print(p.sum())

    mesh = Poly3DCollection(verts[faces], alpha=1)
    face_color = [0.45, 0.45, 0.75]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])

    plt.show()

if __name__ =="__main__":
	path='./modset/'



	last_sum=0
	image=[]
	g=0
	for i in range(g,g+20):
		now_slice=(ToTensor(Image.open(path+('%05d'%i)+'_mask.png'))[0])
		sum = torch.sum(now_slice)
		now_slice=now_slice.numpy().tolist()
		if(last_sum!=sum) or True:
			print(i,sum)
			last_sum=sum
			image.append(now_slice)
		else :
			continue

	#image= (torch.stack([one,one,one],dim=0)*255).numpy()
	print('orin')
	#print(torch.sum(image))
	first_patient = image
	first_patient_pixels = get_pixels_hu(first_patient )
	pix_resampled, spacing = resample(first_patient_pixels, first_patient, [1,1,1])


	print('pix_resampled',pix_resampled.sum())
	plot_3d(pix_resampled, threshold=-300)
# if __name__ =="__main__":
# 	path='./train/'
# 	move_cnt=0
# 	last_sum=100000
# 	img_set=[]
# 	image=[]
# 	for i in range(2000):

# 		now_slice=(ToTensor(Image.open(path+('%05d'%i)+'_mask.png'))[0])
# 		now_sum = int(torch.sum(now_slice.int()))
# 		if not(last_sum-now_sum<5 and last_sum-now_sum>-5):
# 			last_sum=now_sum
# 			img_gen=np.array(torch.stack([now_slice*255],dim=0))
# 			img_path='/fdisk/22/modset/'+str(move_cnt).zfill(5)+'_mask.png'
			
# 			if(now_sum in img_set):
# 				print(i,now_sum,'weioghuioghqeoigqeio')
# 			img_set.append(now_sum)#int(now_sum))
# 			#cv2.imwrite(img_path,img_gen[0]) 
# 			move_cnt+=1
# 		else :
# 			continue
# 	print(move_cnt,len(img_set))
# 	img_set.sort()
# 	print(img_set)
	#image= (torch.stack([one,one,one],dim=0)*255).numpy()
# if __name__ =="__main__" and False:
# 	path='/fdisk/liver/train/'

# 	last_sum=0
# 	image=[]
# 	for i in range(5):
# 		now_slice=(ToTensor(Image.open(path+('%03d'%i)+'_mask.png'))[0]*255)
# 		sum = torch.sum(now_slice)/255

# 		now_slice=(ToTensor(cv2.resize(np.array(now_slice),(80,80)))>125).int()*255

# 		now_slice=now_slice.numpy().tolist()[0]
		
# 		print(135135)
# 		print(len(now_slice))


# 		if(last_sum!=sum):
# 			print(i,sum)
# 			last_sum=sum
# 			image.append(now_slice)
# 		else :
# 			continue

# 	#image= (torch.stack([one,one,one],dim=0)*255).numpy()

# 	first_patient = image
# 	first_patient_pixels = get_pixels_hu(image)

# 	pix_resampled, spacing = resample(first_patient_pixels, first_patient, [0.1,1,1])
# 	plot_3d(pix_resampled, threshold=-300)
