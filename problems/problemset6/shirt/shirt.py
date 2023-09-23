# Paul Gebeline, Problem Set 6 

'''

INSTRUCTIONS
------------

In a file called shirt.py, implement a program that expects exactly two command-line arguments:

    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping 
the input to be the same size, saving the result as its output.

The program should instead exit via sys.exit:

    if the user does not specify exactly two command-line arguments,
    if the inputs and outputs names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the inputs name does not have the same extension as the outputs name, or
    if the specified input does not exist.

Assume that the input will be a photo of someone posing in just the right way, like these demos, so that, when theyre 
resized and cropped, the shirt appears to fit perfectly.

'''

import sys
from PIL import Image, ImageOps



def main():
    
    # Usage
    usage = 'Usage: python shirt.py input_img output_img'

    # Try to store the name of input/output based on cmd-line arguments
    try:
        in_img, out_img = sys.argv[1], sys.argv[2]

        # Try to split each file into its name and its extension
        in_img_name, in_img_ext = in_img.split('.')
        out_img_name, out_img_ext = out_img.split('.')

    # Except if there is an index error (two arguments do not exist) then exit with usage
    except IndexError:
        sys.exit(usage)
    
    # List of valid extensions
    valid_exts = ['jpg', 'jpeg', 'png']

    # If there are more than two arguments, if the extensions arent the same, or they arent a valid extension,
    # exit with usage
    if len(sys.argv) != 3 or in_img_ext != out_img_ext or in_img_ext not in valid_exts:
        sys.exit(usage)

    # Call function
    resize_and_paste(in_img, out_img)
    


def resize_and_paste(input_image, output_image):

    # Open the input image and open shirt.png
    with Image.open(input_image) as img, Image.open('shirt.png') as shirt: 


        # Resize image to width x height pixels returned by the size of the shirt
        resized_img =  ImageOps.fit(img, shirt.size)

        # Paste the shirt onto the image at 0,0 with shirt mask
        resized_img.paste(im = shirt, box = (0,0), mask = shirt)

        # Save result 
        resized_img.save(output_image)





if __name__ == '__main__':
    main()


