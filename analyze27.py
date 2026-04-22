import subprocess, os

video = r'C:\Users\cemya\.openclaw\workspace\hyperframes\renders\cd_test_27s.mp4'
out_dir = r'C:\Users\cemya\.openclaw\workspace\hyperframes\frames27s'
os.makedirs(out_dir, exist_ok=True)

cmd = ['ffmpeg', '-i', video, '-vf', 'fps=2', out_dir + '\\frame_%03d.jpg', '-y']
r = subprocess.run(cmd, capture_output=True, text=True)

frames = sorted([f for f in os.listdir(out_dir) if f.endswith('.jpg')])
print(f'Frames extracted: {len(frames)}')

probe = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                       '-of', 'default=noprint_wrappers=1:nokey=1', video],
                      capture_output=True, text=True)
print(f'Duration: {probe.stdout.strip()}s')
print(f'File size: {os.path.getsize(video)/1024/1024:.2f} MB')