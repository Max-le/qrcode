# Source of this code : https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels


from PIL import Image

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
# img = Image.new( 'RGB', (250,250), "black") # create a new black image

img = Image.open('wifi.png')

pixels = img.load() # create the pixel map




for i in range(img.size[0]):    # for every col:
    for j in range(img.size[1]):    # For every row
        if pixels[i,j] == (0, 0, 0, 255):
            #print("BLACK PIXEL ! ")
            pixels[i,j] = (78, 186, 239) # set the colour accordingly
        #print(pixels[i,j])

img.show()
img.save("wifi.png")