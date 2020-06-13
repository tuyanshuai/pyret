import nibabel as nib
import matplotlib.pyplot as plt
import pymesh as pymesh


epi_img = nib.load('data/testdata.nii.gz')
epi_img_data = epi_img.get_fdata()


# test mesh plot

mesh = pymesh.load_mesh("model.obj")


