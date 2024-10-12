import subprocess

result = subprocess.run(['grep', 'something'],              # args=['command', 'argument']
                        stdout = subprocess.PIPE,          # used to store the output
                        input = 'I am looking something from input string, it returns the whole input if the string is found. ',
                        text=True,                         # makes the output from binary to text format
                        stderr = subprocess.PIPE           # used to store error messages
                        )
print("=============================================================")
print(result.stdout)
print(result.returncode)    # 0 success else fail