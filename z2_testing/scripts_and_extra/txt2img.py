import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import argparse

def txt_to_image(txt_path, output_dir, show_image=False):
    """
    Convert a text file containing a 28x28 matrix of pixel values (0-1 range) to a grayscale image.
    
    Args:
        txt_path: Path to the text file with pixel values in matrix format
        output_dir: Directory to save the output images
        show_image: Whether to display the image after conversion
    
    Returns:
        Path to the saved image
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get filename without extension for saving
    base_filename = os.path.basename(txt_path)
    filename_no_ext = os.path.splitext(base_filename)[0]
    
    # Read the pixel values from the text file
    with open(txt_path, 'r') as f:
        lines = f.readlines()
    
    # Parse the matrix - assuming each line is a row with space-separated values
    pixels = []
    for line in lines:
        # Clean and split the line
        row = line.strip().split()
        if not row:  # Skip empty lines
            continue
        # Convert to float
        row = [float(x) for x in row]
        pixels.append(row)
    
    # Convert to numpy array
    pixels = np.array(pixels)
    
    # Verify dimensions
    if pixels.shape != (28, 28):
        print(f"Warning: Expected 28x28 matrix, but got {pixels.shape}. Attempting to reshape...")
        if pixels.size == 784:  # If we have the right number of pixels
            pixels = pixels.reshape(28, 28)
        else:
            raise ValueError(f"Image dimensions incorrect: {pixels.shape}, cannot reshape to 28x28")
    
    # Scale to 0-255 for image (if needed)
    if np.max(pixels) <= 1.0:
        pixels = (pixels * 255).astype(np.uint8)
    
    # Create and save the image
    image = Image.fromarray(pixels)
    output_path = os.path.join(output_dir, f"{filename_no_ext}.png")
    image.save(output_path)
    print(f"Saved image to {output_path}")
    
    # Display the image if requested
    if show_image:
        plt.figure(figsize=(4, 4))
        plt.imshow(pixels, cmap='gray')
        plt.title(f"Image from {base_filename}")
        plt.axis('off')
        plt.show()
    
    return output_path

def process_directory(input_dir, output_dir, show_images=False):
    """
    Process all .txt files in a directory and convert them to images.
    
    Args:
        input_dir: Directory containing text files
        output_dir: Directory to save output images
        show_images: Whether to display images during conversion
    """
    txt_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    
    if not txt_files:
        print(f"No .txt files found in {input_dir}")
        return
    
    print(f"Found {len(txt_files)} text files to convert")
    
    for txt_file in txt_files:
        txt_path = os.path.join(input_dir, txt_file)
        try:
            txt_to_image(txt_path, output_dir, show_images)
        except Exception as e:
            print(f"Error processing {txt_file}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert 28x28 matrix text files to images')
    parser.add_argument('--input', type=str, required=True, help='Input text file or directory')
    parser.add_argument('--output', type=str, default='output_images', help='Output directory for images')
    parser.add_argument('--show', action='store_true', help='Display images during conversion')
    
    args = parser.parse_args()
    
    if os.path.isdir(args.input):
        process_directory(args.input, args.output, args.show)
    elif os.path.isfile(args.input):
        txt_to_image(args.input, args.output, args.show)
    else:
        print(f"Input path {args.input} not found")

# Example usage:
# python convert_matrix_to_image.py --input data.txt --output images --show
# python convert_matrix_to_image.py --input data_directory --output images