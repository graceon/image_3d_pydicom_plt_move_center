import pydicom

from pydicom.dataset import Dataset, FileDataset
from pydicom.uid import ExplicitVRLittleEndian
import pydicom._storage_sopclass_uids
import os
import matplotlib.pyplot as plt
import numpy as np
import torch
from torchvision.transforms import transforms
from PIL import Image
ToTensor=transforms.ToTensor()
import time


# path='./train/'
# i=1
# now_slice=(ToTensor(Image.open(path+('%05d'%i)+'_mask.png'))[0]*255)

# image2d=now_slice.numpy().astype(np.uint16)

# print("Setting file meta information...")
# # Populate required values for file meta information

# meta = pydicom.Dataset()
# meta.MediaStorageSOPClassUID = pydicom._storage_sopclass_uids.MRImageStorage
# meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
# meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian  

# ds = Dataset()
# ds.file_meta = meta








# ds.is_little_endian = True
# ds.is_implicit_VR = False

# ds.SOPClassUID = pydicom._storage_sopclass_uids.MRImageStorage
# ds.PatientName = "Test^Firstname"
# ds.PatientID = "123456"

# ds.Modality = "MR"
# ds.SeriesInstanceUID = pydicom.uid.generate_uid()
# ds.StudyInstanceUID = pydicom.uid.generate_uid()
# ds.FrameOfReferenceUID = pydicom.uid.generate_uid()

# ds.BitsStored = 16
# ds.BitsAllocated = 16
# ds.SamplesPerPixel = 1
# ds.HighBit = 15

# ds.ImagesInAcquisition = "1"

# ds.Rows = image2d.shape[0]
# ds.Columns = image2d.shape[1]
# ds.InstanceNumber = 1

# ds.ImagePositionPatient = r"0\0\1"
# ds.ImageOrientationPatient = r"1\0\0\0\-1\0"
# ds.ImageType = r"ORIGINAL\PRIMARY\AXIAL"

# ds.RescaleIntercept = "0"
# ds.RescaleSlope = "1"
# ds.PixelSpacing = r"1\1"
# ds.PhotometricInterpretation = "MONOCHROME2"
# ds.PixelRepresentation = 1

# pydicom.dataset.validate_file_meta(ds.file_meta, enforce_standard=True)



# print("Setting pixel data...")
# #ds.PixelData = image2d.tobytes()


# ds.PixelData = newimg.tobytes() 

# ds.__setattr__("Rows", newrow)    # 设置新矩阵的row，row是newimg的row
# ds.__setattr__("Columns", newcol)    # 设置新矩阵的column，col是newimg的col
# ds.__setattr__("WindowCenter", int(factor / 2))    # 可重设窗位，或者不重设
# ds.__setattr__("WindowWidth", factor - 1)    # 可设窗宽，或者不重设

# ds.save_as(r"out.dcm")

INPUT_FOLDER = '/fdisk/22/10079566'
path=INPUT_FOLDER
patients = os.listdir(INPUT_FOLDER)
patients.sort()
if True:
    slices = [pydicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: float(x.ImagePositionPatient[2]))
#print(slices[0])


print("Pixel Spacing                       DS: [0.7813, 0.7813]")
ds=slices[0]
# data1=[];
# data2=[];
# for data in slices[0]:
# 	data1.append(str(data))
# for data in slices[45]:
# 	data2.append(str(data))	
# for i in range(len(data2)):
# 	if(data1[i]!=data2[i]):
# 		print(data1[i])
# 		print(data2[i])





# plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
# plt.show()



rand=torch.ones((128,128))
sign=1
for h in range(128):
	for w in range(128):
		rand[h][w]=sign
		sign=-sign
	sign=-sign

# rand=rand*300
# ds=slices[50]
# plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
# plt.show()
# print(ds)
# print('i#################################')
for i in range(55,56):
	# now_slice=(ToTensor(Image.open('/fdisk/22/patient1/'+'Patient_01_%05d'%i+'.bmp'))[0])

	# now_slice=now_slice*400+1000
	# now_mask=(ToTensor(Image.open('/fdisk/22/patient1mask/'+"Patient_01_%05d_label.png"%i))[0])/0.00392
	now_slice=(ToTensor(Image.open('/fdisk/22/patient10/'+'Patient_10_%05d'%i+'.bmp'))[0])
	now_mask=(ToTensor(Image.open('/fdisk/22/patient10/'+"Patient_10_%05d.png"%i))[0])/0.00392
	now_slice=now_slice*400+900
	now_slice=now_mask*now_slice

	# ones=(now_slice<0.0001)

	# high=ones
	# high_rand=ones*rand

	# med=(now_slice<0.90)*(now_slice>0.4)

	# final=high*1000+high_rand

	plt.imshow(now_mask*now_slice,cmap=plt.cm.bone)
	#plt.imshow(final)
	plt.show()



# ds=slices[78]
# print(ds)
# print('i#################################')
# ds=slices[79]
# print(ds)
# print('i#################################')
# ds=slices[45]
# plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
# plt.show()
# print(ds.Rows)
# ds.Rows=128
# print(ds.Rows)
("""
Pixel Spacing                       DS: [0.7813, 0.7813]
(0008, 0018) SOP Instance UID                    UI: 1.2.840.113619.2.382.14436926.6891088.15513.1508036936.841
(0008, 0018) SOP Instance UID                    UI: 1.2.840.113619.2.382.14436926.6891088.15513.1508036936.796
(0009, 0000) Private Creator                     UL: 10242
(0009, 0000) Private Creator                     UL: 8210
	(0019, 10a2) [Raw data run number]               SL: 89183
	(0019, 10a2) [Raw data run number]               SL: 89138
(0020, 0000) Group Length                        UL: 402
(0020, 0000) Group Length                        UL: 400
	(0020, 0013) Instance Number                     IS: "92"
	(0020, 0013) Instance Number                     IS: "47"
	(0020, 0032) Image Position (Patient)            DS: [-184.214, -193.166, -48.9532]
	(0020, 0032) Image Position (Patient)            DS: [-179.96, -193.175, 40.9462]
(0020, 0037) Image Orientation (Patient)         DS: [0.998882, 9.15527e-07, -0.047267, 4.00543e-06, 1, 0.000104008]
(0020, 0037) Image Orientation (Patient)         DS: [0.998882, 9.15527e-07, -0.047267, 4.00543e-06, 1, 0.000103998]
	(0020, 1041) Slice Location                      DS: "-58.36735535"
	(0020, 1041) Slice Location                      DS: "31.53203011"
(0020, 9057) In-Stack Position Number            UL: 48
(0020, 9057) In-Stack Position Number            UL: 26
(0027, 1040) [RAS letter of image location]      SH: 'I'
(0027, 1040) [RAS letter of image location]      SH: 'S'
	(0027, 1041) [Image location]                    FL: -58.36735534667969
	(0027, 1041) [Image location]                    FL: 31.53203010559082
(0028, 0107) Largest Image Pixel Value           SS: 1631
(0028, 0107) Largest Image Pixel Value           SS: 2420
(0028, 1050) Window Center                       DS: "815.0"
(0028, 1050) Window Center                       DS: "1210.0"
(0028, 1051) Window Width                        DS: "1631.0"
(0028, 1051) Window Width                        DS: "2420.0"
""")