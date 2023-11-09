from sklearn.cluster import KMeans
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time

def preprocess_image(image_path: str) -> np.array:
    '''
    Preprocesses the image to be fed into the model.
    
    Parameters:
        image_path (str): Path to the image.
        
    Returns:
        flat_img_array (np.array): 1D array of the image.
    '''
    try:
        img = Image.open(image_path)
    except:
        print('Image not found. Please check the path.')
        return None

    img_array = np.array(img, dtype=np.float64) / 255

    h, w, d = img_array.shape
    img_array = img_array.reshape(h*w, d)

    return img_array, h, w

def visualize_img(image_vector):
    '''
    Visualizes the image vector.
    
    Parameters:
        image_vector (np.array): 1D array of the image.
        
    Returns:
        None
    '''
    plt.imshow(image_vector, cmap='gray')
    plt.show()

def fit_model(image_vector, n_clusters=10, h=100, w=100) -> np.array:
    """
    Fits the model to the image vector.
    
    Parameters:
        image_vector (np.array): 1D array of the image.
        n_clusters (int): Number of clusters to be formed.
        h (int): Height of the image.
        w (int): Width of the image.
        
    Returns:
        pred_img (np.array): Predicted image.
    """
    start = time.time()

    kmeans = KMeans(
        n_clusters=n_clusters, 
        random_state=42, 
        n_init=10
        )
    
    kmeans.fit(image_vector)

    end = time.time()

    pred_img = kmeans.predict(image_vector)

    print(f'Time taken: {end-start}')

    pred_img = kmeans.cluster_centers_[kmeans.labels_]
    pred_img = pred_img.reshape(h, w, -1)

    return pred_img

def save_image(image_vector, path):
    '''
    Saves the image vector as an image.
    
    Parameters:
        image_vector (np.array): 1D array of the image.
        path (str): Path to save the image.
        
    Returns:
        None
    '''
    plt.imsave(path, image_vector)

def main():
    img_path = 'images/test.jpg'

    img, h, w = preprocess_image(img_path)
  
    pred_img = fit_model(img, 10, h=h, w=w)

    visualize_img(pred_img)

    save_image(pred_img, 'images/pred_img.jpg')


if __name__ == '__main__':
    main()