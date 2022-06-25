import cv2 as cv
import numpy as np

img=cv.imread("umaru.jpg")
gray=cv.imread("umaru.jpg", 0)

print("""
    1. Using a fixed variable, accept and load colored image. Grayscale images should be rejected by the application.
    2. Using user input, allow the user to access and have the program output a pixel value using
the item() method. You may simply print() the value accessed.
    3. Using user input, allow the user to modify a pixel value using the itemset() method. You
may use cv.imshow() to show changes, or use print() to show the before-after value
changes.
    4. Using fixed variables, set image dimensions then determine if the currently loaded image is
within the boundaries or not. print() the check results.
    5. Using fixed variables, set image total pixel count then determine if the currently loaded
image is lower or higher than the set pixel count. print() the check results.
    6. Show the currently loaded image's datatype.
""")

opt=int(input("Input number: "))
if opt == 1 :
    imgsh = len(img.shape)
    graysh = len(gray.shape)
    if imgsh > graysh:
        cv.imshow("Colored", img)
        cv.waitKey(0)
    else:
        exit()

elif opt == 2:
    x = int(input("For x axis: "))
    y = int(input("For y axis: "))
    color = int(input("Selection: \n 1. Blue \n 2. Green \n 3. Red \nInput number: "))
    c=color-1
    print(img.item(x, y , c))


elif opt == 3:
    x = int(input("For x axis: "))
    y = int(input("For y axis: "))
    print(img[x, y])
    for i in range(0, 3, 1):
        color = int(input("Selection: \n 1. Blue \n 2. Green \n 3. Red \nInput number: "))
        pixelValue = int(input("Pixel value: "))
        c=color-1
        img.itemset((x, y, c), pixelValue)
    print(img[x, y])
    cv.imshow("Colored", img)
    cv.waitKey(0)

elif opt == 4:
    x=450
    y=150
    print(img.shape)
    print(f"""
                Total pixel in x-axis: {img.shape[0]}
                Total pixel in y-axis: {img.shape[1]}
                Compared value in x-axis: {x}
                Compared value in y-axis: {y}
            """)

    if x <= img.shape[0] and y <= img.shape[1] :
        print("Within the boundaries")
    else :
        print("Out of boundaries")

elif opt == 5:
    x=150
    y=150
    fixedValue=x * y
    totalPixel=img.shape[0] * img.shape[1]

    print(f"""
              Total fixed value: {fixedValue}
              Total pixel: {totalPixel}
            """)

    if fixedValue > totalPixel :
        print("Higher")
    elif fixedValue < totalPixel :
        print("Lower")
    else :
        print("Equal")

elif opt == 6:
    print(f"Currently loaded image's datatype: {img.dtype}")

else:
    exit()