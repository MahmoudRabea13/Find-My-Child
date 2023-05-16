import cv2 
class FaceDetection():
    def detect_faces(self,image_path):
        # Load the image
        img = cv2.imread(image_path)
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
        cv2.imwrite('./static/Imgs/output.jpg',img)
        return len(faces),Dimensions
# img = FaceDetection.detect_faces(FaceDetection,'../data/Ahmed/IMG_20201117_090902.jpg')

# print(img[0]) # return the number of detected faces 
# print(img[1]) #list of lists of dimensions of each detected face [x,y,w,h]
#print(img[1][0]) #the dimensions of the first face detected
#print(img[1][0][1]) # y of first face , likewise
