import cv2
import os

video_path = r"C:\Users\cemya\.openclaw\media\outbound\d98f2edb-9247-4ec7-8a44-ab7d5971e283.mp4"
output_dir = r"C:\Users\cemya\.openclaw\workspace\frames"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps if fps > 0 else 0

print(f"Video: {total_frames} frames, {fps:.2f} fps, {duration:.2f} seconds")

frame_num = 0
saved = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    if frame_num % 30 == 0:  # Every 30th frame (1 second at 30fps)
        filename = os.path.join(output_dir, f"frame_{frame_num:04d}.png")
        cv2.imwrite(filename, frame)
        saved += 1
        print(f"Saved: frame_{frame_num:04d}.png")
    
    frame_num += 1

cap.release()
print(f"Done! Saved {saved} frames to {output_dir}")
