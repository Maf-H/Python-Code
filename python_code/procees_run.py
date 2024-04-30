#  Date & Time 23/04/2024, 17:30.
#  @author Mesfin Haftu
import subprocess

result = subprocess.run(['echo', 'Hello from Child Process'],
                        capture_output = True,
                        encoding='utf-8')

result.check_returncode()  # No exception means success or clean exit
print(result.stdout)