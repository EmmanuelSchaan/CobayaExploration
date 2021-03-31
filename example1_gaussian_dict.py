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



# Generate infor dictionary
info = {
    "likelihood": {
        "gaussian_mixture": {
            "means": [0.2, 0],
            "covs": [[0.1, 0.05],
                     [0.05, 0.2]],
            "derived": True}},
    "params": dict([
        ("a", {
            "prior": {"min": -0.5, "max": 3},
            "latex": r"\alpha"}),
        ("b", {
            "prior": {"dist": "norm", "loc": 0, "scale": 1},
            "ref": 0,
            "proposal": 0.5,
            "latex": r"\beta"}),
        ("derived_a", {
            "latex": r"\alpha^\prime"}),
        ("derived_b", {
            "latex": r"\beta^\prime"})]),
    "sampler": {
        "mcmc": None},
    "output": "output/cobaya/example1_gaussian/example1_gaussian"
}


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


