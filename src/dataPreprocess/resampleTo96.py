import pickle
import os
import numpy as np
import nibabel as nib


base_path = "/home/bigt/All/Dataset/Hecktor/2021/963/CHGJ007/"
ct_path = base_path + "CHGJ007_ct.nii.gz"
pt_path = base_path + "CHGJ007_pt.nii.gz"
gt_path = base_path + "CHGJ007_gtvt.nii.gz"


ct_image = np.asarray(nib.load(ct_path).get_fdata())
pt_image = np.asarray(nib.load(pt_path).get_fdata())
gt_image = np.asarray(nib.load(gt_path).get_fdata())

images = np.stack(ct_image, pt_image)
mask = images.sum(-1) > 0
print(mask.shape)


