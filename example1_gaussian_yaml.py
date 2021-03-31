# to read cobaya input files
from cobaya.yaml import yaml_load_file

# to run the sampler/minimizer
from cobaya.run import run as cobayaRun

# to analyze the chains
from getdist.mcsamples import MCSamplesFromCobaya
# %matplotlib inline  # uncomment if running from the Jupyter notebook
import matplotlib.pyplot as plt
import getdist.plots as gdplt

import sys




# Read yaml file
pathInput = "./input/cobaya/example1_gaussian.yaml"
info = yaml_load_file(pathInput)

# Use 'force' to delete existing output
info['force'] = True
# Use 'resume' to start from the end of existing output
#info['resume'] = True
# Use 'debug' to print debug output
#info['debug'] = True



# run the sampling
updated_info, sampler = cobayaRun(info)



# Analyze the MCMC chains
gd_sample = MCSamplesFromCobaya(updated_info, sampler.products()["sample"])
mean = gd_sample.getMeans()[:2]
covmat = gd_sample.getCovMat().matrix[:2, :2]
print("Mean:")
print(mean)
print("Covariance matrix:")
print(covmat)

# Generate the triangle plot
gdplot = gdplt.get_subplot_plotter()
gdplot.triangle_plot(gd_sample, ["a", "b"], filled=True)
plt.show()


