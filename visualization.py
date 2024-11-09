import rasterio
import numpy as np
import matplotlib.pyplot as plt


if __name__=="__main__":

    # Open the .tif file
    with rasterio.open("/mnt/data1tb/SAR2NDVI/output/test_tif/daiki_20170506_ndvi.tif") as src:
        # Read Red and NIR bands (assuming Red is band 1 and NIR is band 2; adjust if different)
        red = src.read(1).astype('float32')
        nir = src.read(2).astype('float32')

    # Calculate NDVI
    ndvi = (nir - red) / (nir + red)

    # Handle division by zero errors
    ndvi = np.nan_to_num(ndvi, nan=0.0, posinf=0.0, neginf=0.0)

    # Visualize the NDVI
    plt.figure(figsize=(10, 6))
    plt.imshow(ndvi, cmap='RdYlGn')  # Use a colormap that represents vegetation well
    plt.colorbar(label="NDVI")
    plt.title("NDVI Visualization")
    plt.xlabel("Pixel X-axis")
    plt.ylabel("Pixel Y-axis")
    plt.show()

