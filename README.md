# Display Image

Display image is a Python project which provides a command `display-image` to visualize the image and metadata by QtPy6.

## Installation

~~~~~~~~~~~~~~~{.shell}
pip install display-image
~~~~~~~~~~~~~~~

## Usage

~~~~~~~~~~~~~~~{.shell}
display-image -i <path_to_image>
~~~~~~~~~~~~~~~


The following format extensions can be displayed by command `display-image`

| Image format  | Read | EXIF | Pixel precision        | Pixel type           | File extension                   |  Sidecar needed  |
|---------------|------|------|------------------------|----------------------|----------------------------------|------------------|
| BMP           | x    |      | 8 bits                 | Grayscale, RGB, RGBA | .bmp                             |                  |
| CFA           | x    |      | 16 bits                | Bayer                | .cfa                             |                  |
| DNG           | x    | x    | 16 bits                | Bayer                | .dng                             |                  |
| JPEG          | x    | x    | 8 bits                 | Grayscale, RGB       | .jpg, .jpeg                      |                  |
| MIPI RAW      | x    |      | 10 bits, 12 bits       | Bayer                | .RAWMIPI, .RAWMIPI10, .RAWMIPI12 | x                |
| PLAIN RAW     | x    |      | *                      | *                    | .raw .plain16, *                 | x                |
| PNG           | x    |      | 8 bits                 | Grayscale, RGB, RGBA | .png                             |                  |
| TIFF          | x    | x    | 8 bits, 16 bits        | Bayer, RGB           | .tif, .tiff                      |                  |


![displaye-image GUI](https://github.com/sygslhy/display-image/blob/master/images/display-image-gui.png)

### Image display with sidecar JSON

Some file formats need to know in advance some informations about the image. For example, the PLAIN RAW format is just a simple dump of a buffer into a file, thus it needs to know how to interpret the data.
In this case, user need to have an image sidecar JSON located next to the image file as the same name and path `path_to_image.json`

~~~~~~~~~~~~~~~{.json}
{
    "fileInfo": {
        "format": "plain",
        "height": 3072,
        "width": 4080
        "pixelPrecision": 16,
        "pixelType": "bayer_gbrg",
    }
}
~~~~~~~~~~~~~~~

After image reading, the information in JSON sidecar will be shown in tab Widegt of `ImageMetadata`

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/sygslhy/display-image/blob/master/LICENSE.md) file for details.
