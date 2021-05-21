from PIL import Image, ImageEnhance

user_account_name = "Thomas.Li26"

def main():
    mode = input("Specify image editing mode. Type DEEPFRY, STRETCH, BRIGHTNESS, SHARPEN, or INVERT: ")
    if mode == "DEEPFRY":
        DEEPFRY()
    if mode == "STRETCH":
        STRETCH()
    if mode == "INVERT":
        INVERT()
    if mode == "BRIGHTNESS":
        BRIGHTNESS()
    if mode == "SHARPEN":
        SHARPEN()

def DEEPFRY():
    img = input("Insert the name of an image found in the Downloads folder (for example: Image.png): ")
    im = Image.open(r"C:\Users\{}\Downloads\{}".format(user_account_name, img))
    enhancer = ImageEnhance.Contrast(im)
    factor = float(input("Specify deepfry amount (0-100): "))
    im_output = enhancer.enhance(factor)
    im_output.save('more-contrast-image.png')
    im_output.show()

def STRETCH():
    img = input("Insert the name of an image found in the Downloads folder (for example: Image.png): ")
    im = Image.open(r"C:\Users\{}\Downloads\{}".format(user_account_name, img))
    factor = int(input("Specify width: "))
    factor2 = int(input("Specify height: "))
    im_output = im.resize((factor,factor2))
    im_output.save('more-contrast-image.png')
    im_output.show()

def INVERT():
    img = input("Insert the name of an image found in the Downloads folder (for example: Image.png): ")
    im = Image.open(r"C:\Users\{}\Downloads\{}".format(user_account_name, img))
    enhancer = ImageEnhance.Contrast(im)
    im_output = enhancer.enhance(-1)
    im_output.save('more-contrast-image.png')
    im_output.show()

def BRIGHTNESS():
    img = input("Insert the name of an image found in the Downloads folder (for example: Image.png): ")
    im = Image.open(r"C:\Users\{}\Downloads\{}".format(user_account_name, img))
    enhancer = ImageEnhance.Brightness(im)
    factor = float(input("Specify brightness amount: "))
    im_output = enhancer.enhance(factor)
    im_output.save('more-contrast-image.png')
    im_output.show()

def SHARPEN():
    img = input("Insert the name of an image found in the Downloads folder (for example: Image.png): ")
    im = Image.open(r"C:\Users\{}\Downloads\{}".format(user_account_name, img))
    enhancer = ImageEnhance.Sharpness(im)
    factor = float(input("Specify sharpening amount: "))
    im_output = enhancer.enhance(factor)
    im_output.save('more-contrast-image.png')
    im_output.show()

if __name__ == "__main__":
    main()
