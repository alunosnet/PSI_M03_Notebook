import sys

"""Programa para demonstrar a leitura de argumentos passados pela linha de comandos
"""

#mostrar argumentos passados
for arg in sys.argv:
    print(arg)


print(f"Nº de argumentos passados {len(sys.argv)}")

#confirmar que um argumento existe na lista dos argumentos passados
if "ola" in sys.argv:
    print("olá para ti também")