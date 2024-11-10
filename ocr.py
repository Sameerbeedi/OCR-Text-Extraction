import matplotlib.pyplot as plt
import ssl
import keras_ocr
from collections import defaultdict

# Disable SSL certificate verification (insecure)
ssl._create_default_https_context = ssl._create_unverified_context

# Initialize the keras-ocr pipeline
pipeline = keras_ocr.pipeline.Pipeline()

# Read the image(s)
images = [
    keras_ocr.tools.read(filepath) for filepath in [
        'flip.png'
    ]
]

# Get the predictions
prediction_groups = pipeline.recognize(images)

# Create subplots
fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))

# If only one image, ensure axs is a list
if len(images) == 1:
    axs = [axs]

# Define a threshold for grouping words into lines (based on y-coordinate)
line_threshold = 15  # Adjust this value based on your images for better results

# Dictionary to count word occurrences
word_count = defaultdict(int)

# Process each image's predictions
for ax, image, predictions in zip(axs, images, prediction_groups):
    # Draw the image
    ax.imshow(image)
    ax.axis('off')
    
    # Sort predictions by the y-coordinate to attempt sentence formation
    sorted_predictions = sorted(predictions, key=lambda p: p[1][0][1])
    
    # Group words into lines based on their vertical positions
    current_line = []
    previous_y = sorted_predictions[0][1][0][1]  # Initialize with the y-coordinate of the first word
    
    # Count word occurrences
    for word, box in sorted_predictions:
        word_count[word] += 1  # Increment the count for each recognized word
        
        current_y = box[0][1]  # The y-coordinate of the top-left corner of the box
        if abs(current_y - previous_y) > line_threshold:
            current_line = []  # Start a new line when words are sufficiently apart
        current_line.append(word)
        previous_y = current_y
    
    # Draw the text in the same positions
    for word, box in predictions:
        # Get the position for the text (using the first point of the bounding box)
        x, y = box[0]
        # Overlay the word at the detected position
        ax.text(x, y, word, fontsize=12, color='red', bbox=dict(facecolor='white', alpha=0.7))

# Show the plot with overlaid text
plt.tight_layout()
plt.show()

# Print the word occurrences
print("\nWord Occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
