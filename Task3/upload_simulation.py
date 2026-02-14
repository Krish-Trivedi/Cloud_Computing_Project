import os
import shutil
from datetime import datetime

print("=" * 70)
print("SIMULATED BLOB STORAGE - UPLOAD PROCESS")
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# Create simulated blob storage structure
storage_path = "./simulated_blob_storage"
container_name = "datasets"
container_path = os.path.join(storage_path, container_name)

print("\n[1/3] Creating simulated Azure Blob Storage...")
os.makedirs(container_path, exist_ok=True)
print(f"      ✓ Storage location: {os.path.abspath(storage_path)}")
print(f"      ✓ Container: {container_name}\n")

print("[2/3] Uploading All_Diets.csv to container...")
source_file = "All_Diets.csv"
dest_file = os.path.join(container_path, "All_Diets.csv")

if not os.path.exists(source_file):
    print(f"      ✗ Error: {source_file} not found!")
    exit(1)

shutil.copy2(source_file, dest_file)
file_size = os.path.getsize(dest_file)
print(f"      ✓ Uploaded: All_Diets.csv ({file_size:,} bytes)\n")

print("[3/3] Listing blobs in container...")
print("      Blobs in 'datasets' container:")
for filename in os.listdir(container_path):
    filepath = os.path.join(container_path, filename)
    size = os.path.getsize(filepath)
    print(f"        - {filename} ({size:,} bytes)")

print("\n" + "=" * 70)
print("UPLOAD COMPLETED SUCCESSFULLY")
print("=" * 70)
print("\nNote: This simulates Azure Blob Storage using local filesystem.")
print(f"Your data is stored at: {os.path.abspath(container_path)}")
print("=" * 70 + "\n")
