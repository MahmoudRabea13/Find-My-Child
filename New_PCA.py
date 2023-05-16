import cv2
import numpy as np
class NPCA():
    def __init__(self):
        self.mu = 0
        self.std_dev=0
        self.eigen_vals=0
        self.eigen_vecs=0
    def get_norm_param(self,faces_train):
        # flatten the imagaes from 
        X_train =  np.reshape(faces_train,(faces_train.shape[0], -1 ))
        self.mu = np.mean(X_train, axis = 0 )
        self.std_dev = np.std(X_train, axis = 0)
        # X_train = (X_train - mu)/std_dev
        # # normalize the test set with same mu and std values as training set 
        # return X_train
    def preprocess_data(self,Data):
        Data_processed =  np.reshape(Data,(Data.shape[0], -1 ))
        Data_processed  = (Data_processed  - self.mu)/self.std_dev
        return Data_processed
    def sorted_eigen(self,X):
        # X_cov = np.dot(X,X.T)
        X_cov = np.cov(X)
        w, v = np.linalg.eig(X_cov)
        sorted_index = np.argsort(w)[::-1]
        sorted_eigenvalue = w[sorted_index]
        sorted_eigenvectors = v[:,sorted_index]
        # eigenvalues, eigenvectors = np.linalg.eig(X_cov)
        # sorted_eigenvalue = np.sort(eigenvalues)[::-1]
        # sorted_eigenvectors = eigenvectors[:, eigenvalues.argsort()[::-1]]
        # self.eigen_vals = sorted_eigenvalue
        # self.eigen_vecs = sorted_eigenvectors
        return sorted_eigenvectors,sorted_eigenvalue
    def eigenvec_matrix(self,X):
        return(np.dot(X.T,self.eigen_vecs))
    def get_components(self,variance_threshold):
        variance_ratio = self.eigen_vals/np.sum(self.eigen_vals)
        s = 0
        i = -1
        while s < variance_threshold and s < 1.0:
            i += 1
            s +=  variance_ratio[i]
        return i
    def apply_pca(self,X):
        self.get_norm_param(X)
        X = self.preprocess_data(X)
        self.eigen_vecs,self.eigen_vals = self.sorted_eigen(X)
        self.eigen_vecs = self.eigenvec_matrix(X)
        # print(f"size is :{self.eigen_vecs.shape}")
        # print(f"eigen :{self.eigen_vecs}")
    def cut_values(self,var_th):
        var_val = self.get_components(var_th)
        self.eigen_vecs = self.eigen_vecs[:,:var_val]
    def reduce_dim(self,X):
        T1 = np.dot(X,self.eigen_vecs)
        T2 = np.dot(self.eigen_vecs.T,self.eigen_vecs)
        T2 = np.linalg.inv(T2)
        return np.dot(T1,T2)
    def reconstruct(self,X):
        return np.dot(X,self.eigen_vecs.T)
    def save_preprocessing(self):
        data = [self.mu,self.std_dev]
        np.save('pre',np.array(data))
        np.save('vecs',np.array(self.eigen_vecs))
        np.save('vals',np.array(self.eigen_vals))
    def load_preprocessing(self):
        data = np.load('pre.npy')
        self.eigen_vals = np.load('vals.npy')
        self.eigen_vecs = np.load('vecs.npy')
        self.mu,self.std_dev = data[0,:],data[1,:]