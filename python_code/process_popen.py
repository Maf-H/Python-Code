#  Date & Time 23/04/2024, 17:30.
#  @author Mesfin Haftu
import subprocess
import os
import time

# If I create a subprocess using the Popen class instead of the run function,
# I can poll child process status periodically while Python does other work:

proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('Working')

print('Exit Status:', proc.poll())

start = time.time()
sleep_process = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', '1'])
    sleep_process.append(proc)

for proc in sleep_process:
    proc.communicate()

end = time.time()
delta = end - start
print(f'Finished in {delta:.3} seconds')


def run_encrypt(data):
    env = os.environ.copy()
    env['password'] = 'zf7ShyBhZOraQDdE/FiZpm/m/8f9X+M1'
    proc = subprocess.Popen(['openssl', 'enc', '-des3', '-pass', 'env:password'],
                            env = env,
                            stdin = subprocess.PIPE,
                            stdout = subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()  # Ensure that the child gets input.
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_encrypt(data)
    procs.append(proc)

for proc in procs:
    out, _ = proc.communicate()
    print(out[-10:])
