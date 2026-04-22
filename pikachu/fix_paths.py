import os, shutil

# 1. Remove duplicate index files from root (keeping only pikachu/index.html)
root_dir = r'C:\Users\cemya\.openclaw\workspace\hyperframes'
for f in ['index-BACKUP-pikachu.html', 'index-BACKUP.html']:
    path = os.path.join(root_dir, f)
    if os.path.exists(path):
        os.remove(path)
        print(f"Removed: {f}")

# 2. Check what's in pikachu folder for images
pikachu_dir = r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu'
print("\nPikachu folder contents:")
for f in os.listdir(pikachu_dir):
    print(f"  {f}/" if os.path.isdir(os.path.join(pikachu_dir, f)) else f)

# 3. Check product_photos structure
pp_dir = r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu\product_photos'
for root, dirs, files in os.walk(pp_dir):
    for f in files[:3]:
        print(f"  {os.path.relpath(os.path.join(root, f), pp_dir)}")