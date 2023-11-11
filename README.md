# Color Quantization Tool using KMeans Clustering

<p>
<img alt="Pandas" src="https://img.shields.io/badge/-Pandas-5849BE?style=flat-square&logo=pandas&logoColor=white" />
<img alt="NumPy" src="https://img.shields.io/badge/-NumPy-blue?style=flat-square&logo=NumPy&logoColor=white" />
<img alt="Docker" src="https://img.shields.io/badge/-Docker-46a2f1?style=flat-square&logo=docker&logoColor=white" />
<img alt="python" src="https://img.shields.io/badge/-Python-13aa52?style=flat-square&logo=python&logoColor=white" />
<img alt="Jupyter" src="https://img.shields.io/badge/-Jupyter-FB542B?style=flat-square&logo=Jupyter&logoColor=white" />
<img alt="Scikit-learn" src="https://img.shields.io/badge/-Scikit learn-DD0031?style=flat-square&logo=Scikit-learn&logoColor=white" />
</p>

This tool performs color quantization by employing the KMeans clustering algorithm from the scikit-learn library. Color quantization is a process that reduces the number of colors in an image. It is commonly used in graphics to decrease the image file size and reduce the number of distinct colors for printing. It can also be used creatively to achieve a particular aesthetic or to preprocess images for machine learning tasks.

## What is Color Quantization?

Color quantization reduces the number of distinct colors in an image by grouping similar colors together. This is often necessary for many practical applications such as reducing the cost of printing or compressing the image without significantly altering its visual appearance.

### Example Before and After

Below are example images that demonstrate the color quantization process:

#### Before Color Quantization
![Before Color Quantization](images/test.jpg)

#### After Color Quantization
![After Color Quantization](images/pred_img.jpg)

## Features

- Fast color quantization of images
- Customizable number of color clusters
- Simple and intuitive Python API

## Installation

To use this tool, you need to have Python and the following packages installed:

```bash
pip install scikit-learn numpy pillow
