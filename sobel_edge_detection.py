import cv2
import os

# Set the path to the directory containing the images
path_to_images = "C:/Users/danie/Desktop/NTU/Modules/Year 4 Semester 2/Intelligence System/Assignment/Assignment 2/retina2"

# Set the path to the directory where you want to save the edges
path_to_edges = "C:/Users/danie/Desktop/NTU/Modules/Year 4 Semester 2/Intelligence System/Assignment/Assignment 2/Sobel Edge Detection Output/sobel_output"

# Create the directory if it doesn't exist
if not os.path.exists(path_to_edges):
    os.makedirs(path_to_edges)

# Loop through all the files in the directory
for filename in os.listdir(path_to_images):
    # Load the image using OpenCV
    img = cv2.imread(os.path.join(path_to_images, filename))

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Sobel edge detection
    edges_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    edges_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    edges = cv2.magnitude(edges_x, edges_y)

    # Display the edges
    cv2.imshow("Edges", edges)
    cv2.waitKey(0)

    # Save the edges to a new file in the edges directory
    edge_filename = os.path.splitext(filename)[0] + "_edges.bmp"
    cv2.imwrite(os.path.join(path_to_edges, edge_filename), edges)

# Close all windows
cv2.destroyAllWindows()
