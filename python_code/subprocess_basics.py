#  Date & Time 27/04/2024, 17:12.
#  @author Mesfin Haftu
import subprocess

result = subprocess.run(["ls", "-l"],
                        stdout = subprocess.PIPE,
                        stderr = subprocess.PIPE,
                        text = True)
result2 = subprocess.run(["grep", "keyword"],
                         input = " is the interkeyword",
                         text = True,
                         stdout = subprocess.PIPE)

print(result.stdout)
print()
print(result2.stdout)