import cv2 
class FaceDetection():
    def detect_faces(self,image_path):
        # Load the image
        img = cv2.imread(image_path)
        self.img = img
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Load the face detection classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
        Dimensions=[]
        # Loop through the faces and draw rectangles around them
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            face= [x,y,w,h]
            Dimensions.append(face)
        self.dim = Dimensions
        return len(faces),Dimensions
    def save(self,pred):
        for i in range(len(pred)):
            self.img = cv2.putText(self.img,pred[i],org=(self.dim[i][0],self.dim[i][1]),fontFace=cv2.QT_FONT_NORMAL,fontScale=int(min(self.dim[i][2],self.dim[i][3])*1e-2),thickness=int(min(self.dim[i][2],self.dim[i][3])*1e-2),color=(0,255,0))
        cv2.imwrite('./static/Imgs/output_img.jpg',self.img)
# img = FaceDetection.detect_faces(FaceDetection,'../data/Ahmed/IMG_20201117_090902.jpg')

# print(img[0]) # return the number of detected faces 
# print(img[1]) #list of lists of dimensions of each detected face [x,y,w,h]
#print(img[1][0]) #the dimensions of the first face detected
#print(img[1][0][1]) # y of first face , likewise
