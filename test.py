import nibabel as nib
import matplotlib.pyplot as plt
import pymesh as pymesh


epi_img = nib.load('data/testdata.nii.gz')
epi_img_data = epi_img.get_fdata()

# test gii

import nibabel as nib
from nibabel.testing import test_data

surf_img = nib.load(test_data('gifti', 'ascii.gii'))
