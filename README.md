# Quantization-Dithering-and-Color-Transformation

## Quantization
Quantization is a compression technique used in image processing that reduces a range of values to a single quantum value. It is the process of converting a sampled image with real values to one with just a limited set of different values The number of discrete symbols in a specific stream decrease, creating the stream more compressible. Reducing the number of colors necessary to portray a digital image allows for a smaller file size. The image's amplitude values are digitized during the quantization process.

## Dithering
Dithering is an image processing method used in computer graphics to generate the appearance of color depth in images with a limited color palette. The methodical application of noise to an image is referred to as dithering. Colors that are not accessible in the palette are approximated by a diffusion of colored pixels from the palette that is available. It has typically been used to improve the look of images whose output is restricted to a specific color spectrum.

## Floyd-Steinberg algorithm
Floyd-Steinberg dithering algorithm attempts to compress a picture to a smaller number of color pallets while minimizing perceived alterations. The technique uses error diffusion to accomplish dithering, which means it transfers a pixel's latent quantization error to its nearby pixels. It distributes the debt based on the distribution. The matching color to each pixel in the original image is picked from a palette, and any quantization error is divided the neighbor pixels.

## Requirements
* Tested on Python 3.6
* `pip install -r requirements.txt`

## Usage
* `python hough_transform.py`



## References
https://medium.com/analytics-vidhya/exploiting-the-floyd-steinberg-algorithm-for-image-dithering-in-r-c19c8008fc99