import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_metric(image1, image2):
    # Calculate some metric for image quality
    # For demonstration, let's use mean squared error as the metric
    return np.mean((image1.astype(float) - image2.astype(float)) ** 2)

def quantify_image_quality_improvement(image_path):
    # Read the original image
    original_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    # Check if the image is read successfully
    if original_image is None:
        raise ValueError("Failed to read the image")
    
    # Apply traditional image enhancement techniques (e.g., contrast adjustment, sharpening)
    enhanced_image = cv2.addWeighted(original_image, 1.5, np.zeros(original_image.shape, original_image.dtype), 0, 0)

    # Apply homomorphic filtering
    filtered_image = homomorphic_filter(original_image)

    # Calculate improvement metrics
    improvement_metric = calculate_metric(enhanced_image, filtered_image)
    
    # Plot original and improved images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
    plt.title('Improved Image')
    plt.axis('off')

    plt.show()

    return improvement_metric

def homomorphic_filter(image):
    # Apply homomorphic filtering
    # For demonstration, you can use your own implementation or a library like OpenCV's
    # Here's a simple example using OpenCV's implementation
    rows, cols, _ = image.shape
    image_log = np.log1p(np.float32(image))
    M = 2 * np.floor(np.log2(max(rows, cols)))
    filtered_image = cv2.normalize(image_log, None, 0, 1, cv2.NORM_MINMAX)
    return filtered_image

# Example usage:
image_path = 'path/myimage1.jpg'
improvement = quantify_image_quality_improvement(image_path)
print("Improvement in image quality:", improvement)
