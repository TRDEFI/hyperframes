import subprocess, os

os.chdir(r'C:\Users\cemya\.openclaw\workspace\hyperframes')
result = subprocess.run(
    ['hyperframes', 'render', '--workers', '2'],
    capture_output=True, text=True,
    cwd=r'C:\Users\cemya\.openclaw\workspace\hyperframes'
)
print("STDOUT:", result.stdout[-3000:] if len(result.stdout) > 3000 else result.stdout)
print("STDERR:", result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)
print("Return code:", result.returncode)