import cv2 #openCv use as cv2 in python
# import opencv as cv2 #openCv use as cv2 in python



# //////////////imgage show

# img1 = cv2.imread("C:\\Users\\ripon\\Downloads\\assets\\asset 15.png")
# img1 = cv2.resize(img1,(600,600))#widrh height
# print(img1)
# cv2.imshow("original",img1)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ///////// Gray style image

# img2 = cv2.imread("C:\\Users\\ripon\\Downloads\\assets\\asset 16.png",2)
# img2 = cv2.resize(img2,(600,600))#widrh height
# print(img2)
# cv2.imshow("Gray style image show",img2)
# cv2.waitKey(3000)##time how many milisecond it will show  
# cv2.destroyAllWindows()

#//////////////////// PRACTICE input path and show image

# path = input("enter the path of the image : ")
# print("enter your path ", path)
# img2 = cv2.imread(path)

img2 = cv2.imread("C:\\Users\\ripon\\Downloads\\assets\\asset 14.png")
img2 = cv2.resize(img2,(600,600))#widrh height
img2 = cv2.flip(img2,0)# rotate image 0,-1,1
print(img2)
cv2.imshow("Gray style image show",img2)

k = cv2.waitKey(0)
if k==ord("s"):
    cv2.imwrite("C:\\Users\\ripon\\asset 16.png",img2)
else:
    cv2.destroyAllWindows()


# //////////////////////////Blur


img1 = cv2.imread("C:\\Users\\ripon\\Downloads\\assets\\asset 15.png")
img1 = cv2.resize(img1,(600,600))#widrh height
# img1 = cv2.GaussianBlur(img1, (5, 5), 0) # Blur

cv2.imshow("original",img1)
cv2.waitKey()
cv2.destroyAllWindows()



# ////////////////////--------VIDEO ----//////////////////////


cap = cv2.VideoCapture("C:\\Users\\ripon\\Downloads\\Video\\We Sold Our Startup & Filmed Everything!.mp4")
print("video cap",cap)

while True:
    ret,frame = cap.read()
    
    frame = cv2.resize(frame,(600,600))
    
    # frame = cv2.resize(frame,(600,600))
    # cv2.imshow("original frame video ",frame)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow(" gray frame video ",gray)
    
    k =cv2.waitKey(25)
    if k ==  ord("s"):#// stop the video press s letter
     break
cap.release()
cv2.destroyAllWindows()

