import time
inicio = time.time()

arq = open('dataset-2-e.csv', 'r')
arq1 = arq.read()
aaa = arq1.split()
print(max(aaa))
g = open('filee.txt', 'a')
g.writelines(str(max(aaa)) + "\n" )                   
fim = time.time()
g.writelines(str(fim - inicio) + "\n" )                   
g.close()


