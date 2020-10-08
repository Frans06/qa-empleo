"""Package Qa Empleo 

Returns:
    estado: ['bien', 'mal']
"""
__version__ = "0.1"
import sys

# https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3


def main(args):
    paramsList = [
        args[1].strip(),
        int(args[2].strip()),
        int(args[3].strip()),
        int(args[4].strip()),
        int(args[5].strip()),
        int(args[6].strip()),
        int(args[7].strip()),
        int(args[8].strip()),
    ]

    def calculamedia():
        total = 0
        media = 0
        # http://lineadecodigo.com/python/iterar-una-lista-en-python-con-indices/
        for a in range(2, len(paramsList)):
            total = total + paramsList[a]
        if total == 0:
            print("No hay datos suficientes")
        else:
            media = total / 7
        print(f"La puntuación media obtenida es: {media}")
        return media

    nota = calculamedia()
    estado = ""
    if nota <= 6:
        estado = "mal"

    elif 6 < nota < 10:
        estado = "bien"
    else:
        print("Debes introducir valores coherentes")
        exit(1)

    print(f"La oferta está {estado}")


if __name__ == "__main__":
    main(sys.argv)