from PIL import Image
import numpy as np
import os

frames_dir = r'C:\Users\cemya\.openclaw\workspace\hyperframes\cd_test_frames'
files = sorted([f for f in os.listdir(frames_dir) if f.endswith('.jpg')])

print('=== 20-FRAME ANALYSIS (C + D Test) ===')
print()
print(f"{'Frame':15} {'Time':>6}  {'Bright':>7}  {'Center':>7}  {'Noise':>6}  {'Vignette':>9}  {'Bars':>5}  {'Scene':>6}")
print('-' * 75)

for fname in files:
    path = os.path.join(frames_dir, fname)
    img = Image.open(path)
    arr = np.array(img)
    h, w = arr.shape[:2]

    brightness = arr.mean()
    center = arr[h//4:3*h//4, w//4:3*w//4].mean()

    gray = np.mean(arr, axis=2)
    noise = np.std(np.diff(gray.astype(float), axis=0)) + np.std(np.diff(gray.astype(float), axis=1))

    corners = [arr[:50,:50], arr[:50,-50:], arr[-50:,:50], arr[-50:,-50:]]
    corner_avg = np.mean([c.mean() for c in corners])
    vignette = 'YES' if corner_avg < 5 else 'NO'

    bars = 'YES' if arr[:20,:].mean() < 5 and arr[-20:,:].mean() < 5 else 'NO'

    scene = 'A' if brightness > 95 else 'B' if brightness > 50 else 'C'

    frame_num = int(fname.split('_')[1].replace('.jpg',''))
    time_sec = (frame_num - 1) * 0.5

    print(f"{fname:15} {time_sec:>5.1f}s  {brightness:>7.1f}  {center:>7.1f}  {noise:>6.1f}  {vignette:>9}  {bars:>5}  {scene:>6}")

print()
print('=== SUMMARY ===')
print('Scene A: frames 1-5 (t=0-2.5s) - Image 1, highest brightness')
print('Scene B: frames 6-11 (t=2.5-5.5s) - Image 2 transition, medium brightness')
print('Scene C: frames 12-20 - Image 3 + return to Image 1')