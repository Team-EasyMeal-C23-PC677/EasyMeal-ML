from bing_image_downloader import downloader
from PIL import Image
import imagehash
import os

def is_duplicate(image_path, hash_list, threshold=5):
    # Open the image using Pillow
    image = Image.open(image_path)
    
    # Compute the image hash using the average hash algorithm
    image_hash = imagehash.average_hash(image)
    
    # Compare the image hash with the hashes in the list
    for stored_hash in hash_list:
        # Calculate the hamming distance between the hashes
        distance = image_hash - stored_hash
        if distance <= threshold:
            return True  # Image is a duplicate or very similar
    
    # Image is not a duplicate
    return False

def download_images(query, limit):
    output_dir = f"{query}_images"
    duplicate_hashes = set()  # Store the image hashes of downloaded images

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Download the images
    downloaded_images = downloader.download(query, limit=limit, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=5)

    # Remove duplicate images
    for image_path in downloaded_images[query]:
        if is_duplicate(image_path, duplicate_hashes):
            os.remove(image_path)
        else:
            # Add the hash of the downloaded image to the set
            image = Image.open(image_path)
            image_hash = imagehash.average_hash(image)
            duplicate_hashes.add(image_hash)

    print(f"Downloaded {len(downloaded_images[query]) - len(duplicate_hashes)} unique images of {query}.")

# Call the function to download 10 unique images of cats
download_images("Kaempferia galanga root", 100)