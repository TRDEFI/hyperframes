import os, shutil

pikachu_dir = r'C:\Users\cemya\.openclaw\workspace\hyperframes\pikachu'
src = os.path.join(pikachu_dir, 'product_photos', 'main')
dst = os.path.join(pikachu_dir, 'main_images')

# Create main_images folder
os.makedirs(dst, exist_ok=True)

# Copy all main images
for f in os.listdir(src):
    if f.endswith(('.jpg', '.jpeg', '.png', '.webp')):
        shutil.copy(os.path.join(src, f), os.path.join(dst, f))
        print(f"Copied: {f}")

print(f"\nmain_images now has {len(os.listdir(dst))} files")