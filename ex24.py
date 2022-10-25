import subprocess
from sys import stderr, stdout

proc = subprocess.run( ['ping', '127.0.0.1' ,'-c', '4'],
    capture_output=True,
    text = True                      

)


saida = stdout
print(saida)
print(proc.args)
print(proc.returncode)  # DIFERENTE DE 0 É PQ TEM ERRO
