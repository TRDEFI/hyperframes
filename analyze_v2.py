from PIL import Image
import numpy as np
import os

frames_dir = r'C:\Users\cemya\.openclaw\workspace\hyperframes\cd_test_v4_frames'
files = sorted([f for f in os.listdir(frames_dir) if f.endswith('.jpg')])

print('=== V2 TEST — 20-FRAME ANALYSIS ===')
print()
print(f"{'Frame':15} {'Time':>6}  {'Bright':>7}  {'Center':>7}  {'Noise':>6}  {'Vignette':>9}  {'Bars':>5}  {'Scene':>6}")
print('-' * 75)

prev_bright = 0
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

    delta = brightness - prev_bright if prev_bright > 0 else 0
    arrow = '' if delta == 0 else f'  {"+" if delta > 0 else ""}{delta:.1f}'
    prev_bright = brightness

    print(f"{fname:15} {time_sec:>5.1f}s  {brightness:>7.1f}  {center:>7.1f}  {noise:>6.1f}  {vignette:>9}  {bars:>5}  {scene:>6}{arrow}")