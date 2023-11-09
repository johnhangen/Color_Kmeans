# Color Quantization Tool using KMeans Clustering

This tool performs color quantization by employing the KMeans clustering algorithm from the scikit-learn library. Color quantization is a process that reduces the number of colors in an image. It is commonly used in graphics to decrease the image file size and reduce the number of distinct colors for printing. It can also be used creatively to achieve a particular aesthetic or to preprocess images for machine learning tasks.

## What is Color Quantization?

Color quantization reduces the number of distinct colors in an image by grouping similar colors together. This is often necessary for many practical applications such as reducing the cost of printing or compressing the image without significantly altering its visual appearance.

### Example Before and After

Below are example images that demonstrate the color quantization process:

#### Before Color Quantization
![Before Color Quantization](images\test.jpg)

#### After Color Quantization
![After Color Quantization](images\pred_img.jpg)

## Features

- Fast color quantization of images
- Customizable number of color clusters
- Simple and intuitive Python API

## Installation

To use this tool, you need to have Python and the following packages installed:

```bash
pip install scikit-learn numpy pillow
