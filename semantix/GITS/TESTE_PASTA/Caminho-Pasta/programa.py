from os import listdir, sep
from os.path import abspath, basename, isdir
from sys import argv

with open("resposta.txt","w+") as arq:

    def escala(dir, meio, FILES=True):
        arq.write(meio[:-1] + '+--<' + basename(abspath(dir)) +'>'+ '\n')
        meio = meio + ' '

        if FILES:
            files = listdir(dir)
        else:
            files = [f for f in listdir(dir) if isdir(dir + sep + f)]
        count = 0
        for file in files:
            count += 1
            arq.write(meio + '    |'+'\n')
            path = dir + sep + file
            if isdir(path):
                if count == len(files):
                    escala(path, meio + '     ', FILES)
                else:
                    escala(path, meio + '    |', FILES)
            else:
                arq.write(meio + '    +--' + file +'\n')


    def modelo():
        return '''Usar: %s [-f] <PATH>''' % basename(argv[0])


    def main():
        if len(argv) == 1:
            arq.write(modelo())
        elif len(argv) == 2:
            path = argv[1]
            if isdir(path):
                escala(path, '  ')
            else:
                print('ERRO DE INDEXAÇÃO: \'' + path + '\' diretorio nao encontrado')

        else:
            print(modelo())


    main()
