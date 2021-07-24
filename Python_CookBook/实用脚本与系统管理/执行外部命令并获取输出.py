import subprocess

try:
    out_bytes = subprocess.check_output(['netstat', '-a'])
    out_txt = out_bytes.decode('utf-8')
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode
