"""
Downloading ConWhAt Atlases
===============================
"""

###################################################################################################
# Setup
# ---------------------

# Import the fetcher function

from conwhat.utils.fetchers import fetch_conwhat_atlas
import os,glob

# Define the output directory

atlas_dir = 'conwhat_atlases'

# Define which atlas to grab

atlas_name = 'CWL2k8Sc33Vol3d100s_v01'


###################################################################################################
# Download the atlases and take a look
# -------------------------------------

fetch_conwhat_atlas(atlas_name,atlas_dir,remove_existing=True);

# The zipped and unzipped atlas folders are now there in the top-level atlas directory;

glob.glob(atlas_dir + '/*')


# The .zip file can be optionally removed automatically if desired. 

# volumetric atlas folders contain a small number of fairly small .txt files

glob.glob('%s/%s/*.txt' %(atlas_dir,atlas_name))

# ...and a larger number of nifti images; one for each atlas structure

glob.glob('%s/%s/*.nii.gz' %(atlas_dir,atlas_name))[:5]

len(glob.glob('%s/%s/*.nii.gz' %(atlas_dir,atlas_name)))

