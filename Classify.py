import cv2
import numpy as np
class Classify():
    def __init__(self):
        self.means = 0
        self.number = 0
    def fit(self,X,y,number):
        M,N = X.shape
        means = np.zeros((number,N))
        for i in range(number):
            means[i,:] = (1/N) * np.sum(X[y == i,: ], axis = 0 )
        self.means = means
        self.number = number
    def distance(self,X1,X2):
        diff = X1-X2
        d = np.sqrt(np.dot(diff,diff))
        return d
    def predict(self,test_img):
        min_dist = np.inf
        min_class = -1
        for i in range(self.number):
            d = self.distance(test_img, self.means[i,:])
            if d < min_dist:
                min_dist = d
                min_class = i 
        return min_class
    def save_weights(self):
        np.save('Weights',self.means)
    def load_weights(self):
        self.means = np.load('./Weights.npy')