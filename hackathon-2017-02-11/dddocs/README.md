# Denoising Dirty Documents

## About

UBCS3 is hosting a mini hackathon on 11 December. There will be at least one group hacking on the Denoising Dirty Documents competition from Kaggle. This is a repository to get everyone going, with some initial data exploration, and some methods for loading/exporting data. It also sets a benchmark score with the "boneheaded" method of hard-thresholding. 

## External Resources

Links for material that could be useful for creating good methods; or to blog articles or kernels that I found particularly helpful. 

### Technical tools

* [Median filter](https://www.wikiwand.com/en/Median_filter) ([`scipy` implementation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.medfilt.html))
* [Wavelet transform](https://www.wikiwand.com/en/Wavelet_transform) ([`pywt` implementation](https://github.com/PyWavelets/pywt))
* Machine learning:
   * [Neural Networks](https://www.wikiwand.com/en/Convolutional_neural_network) ([`keras` implementation](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html));
   * [Random forests](https://www.wikiwand.com/en/Random_forest) ([`scipy` implementation](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html));
   * [Gradient Tree Boosting](https://www.wikiwand.com/en/Gradient_boosting#/Gradient_tree_boosting) ([xgboost](http://xgboost.readthedocs.io/en/latest/python/python_intro.html) is a pain to install)
* [Variational models for image denoising](https://www.wikiwand.com/en/Total_variation_denoising)


### Blog articles

* [Colin Priest](https://colinpriest.com/2015/08/01/denoising-dirty-documents-part-1/) has a 12-part blog series on getting a score of ~1 %
* The same series has been compressed and posted on the [Kaggle blog](http://blog.kaggle.com/2015/12/04/image-processing-machine-learning-in-r-denoising-dirty-documents-tutorial-series/).