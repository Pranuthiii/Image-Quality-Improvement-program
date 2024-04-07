# Image-Quality-Improvement-program
This program helps to improve the image quality by quantifying the improvement in image quality achieved through homomorphic filtering compared to traditional image enhancement techniques.
path of the file must be according to the path of the image file in your computer

Algorithm:
1. Input Image: Accept the file path of the input image.
2. Read Image: Read the original image from the provided file path using OpenCV.
3. Traditional Image Enhancement: Apply traditional image enhancement techniques to the original image (e.g., contrast adjustment, sharpening). This step aims to enhance the original image using conventional methods.
4. Homomorphic Filtering: Apply homomorphic filtering to the original image. Homomorphic filtering is a technique that enhances the contrast of images while simultaneously reducing the effect of lighting variations.
5. Calculate Improvement Metric: Calculate the improvement in image quality between the enhanced image (from traditional techniques) and the filtered image (from homomorphic filtering). Use a suitable metric such as mean squared error (MSE) to quantify the difference between the two images.
6. Visual Comparison: Display the original image and the enhanced image side by side for visual comparison. This helps to visualize the improvement achieved by homomorphic filtering.
7. Output Improvement Metric: Return the improvement metric calculated in step 5.

in this code:
● quantify_image_quality_improvement function orchestrates the entire process.
● enhance_image function applies traditional image enhancement techniques.
● homomorphic_filter function applies homomorphic filtering.
● show_comparison function displays the original and enhanced images for visual
comparison.
● calculate_metric function computes the improvement metric.

● The provided Python code effectively quantifies the improvement in image quality achieved through homomorphic filtering compared to traditional image enhancement techniques. Upon receiving the file path of an image, the program reads the image using OpenCV and checks its readability.
● Subsequently, it applies traditional image enhancement techniques, such as contrast adjustment, to the original image, and then proceeds to implement homomorphic filtering.
● This filtering method enhances image contrast while mitigating the impact of varying lighting conditions. Using a predefined metric—in this case, mean squared error—the program calculates the improvement in image quality between the enhanced image from traditional techniques and the filtered image from homomorphic filtering.
● It then visually compares the original and enhanced images side by side using matplotlib for clarity. With these steps, the program effectively demonstrates the efficacy of homomorphic filtering in enhancing image quality.
