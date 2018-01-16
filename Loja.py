import datetime
def DiaSemana (aa, mm, dd):
    x = datetime.date (aa, mm, dd)
    return (x.weekday())
 
arq = open('produtos.txt', 'r')
S = arq.readlines()
x = 0
Codigo = []
Unidade = []
Estoque = []
Custo = []
Margem = []
P = []
 
while len(S) > x:
    L = S[x].split(';')
    Cod = int (L[0])
    Unid = str (L[1])
    Estoq = float (L[2])
    Cust = float (L[3])
    Marg = float (L[4])
    Codigo.append (Cod)
    Unidade.append (Unid)
    Estoque.append (Estoq)
    Custo.append (Cust)
    Margem.append (Marg)
    x = x + 1
     
print ("")
 
x = 0
while x == 0:
    Mes = int(input("Selecione o mês desejado (1 a 12): "))
    print ("")
    if Mes >12 or Mes <= 0:
        print ("*************************Valor inválido, tente novamente*************************")
        print ("       O mês deve estar no intervalo de 1 a 12 - Por favor digite novamente")
        print ("")
    else:
        if Mes == 1:
                NomeMes = "Janeiro"                    
        elif Mes == 2:
                NomeMes = "Fevereiro"          
        elif Mes == 3:
                NomeMes = "Março"
        elif Mes == 4:
                NomeMes = "Abril"
        elif Mes == 5:
                NomeMes = "Maio"
        elif Mes == 6:
                NomeMes = "Junho"
        elif Mes == 7:
                NomeMes = "Julho"
        elif Mes == 8:
                NomeMes = "Agosto"
        elif Mes == 9:
                NomeMes = "Setembro"
        elif Mes == 10:
                NomeMes = "Outubro"
        elif Mes == 11:
                NomeMes = "Novembro"     
        else:
                NomeMes = "Dezembro"
        print ("  O mês Escolhido foi: %s" % NomeMes)
        print ("")
        x = 1   
         
while x == 1:
    Ano = int(input("Selecione o ano desejado com 4 digitos (a partir de 2015): "))
    print ("")
 
    if Ano != 2015 and Ano != 2016 and Ano != 2017 :
        print ("*************************Valor inválido, tente novamente*************************")
        print ("          O ano deve estar no formato 20xx e ser de 2015 a 2017")
        print ("")
    else:
        x = 2
 
QtdeVendasDia = 0
while QtdeVendasDia <= 0:
        QtdeVendasDia = int(input("Digite a média de vendas por dia no mês de %s de %d: " % (NomeMes, Ano)))
        print("")

        if QtdeVendasDia <= 0:
                print ("*************************Valor inválido, tente novamente*************************")
                print ("          A quantidade de vendas por dia deve ser maior que 0!")
                print ("")
        else:
                if Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10 or Mes == 12:
                    NDiasMes = 31
                elif Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11:
                    NDiasMes = 30
                else:
                    NDiasMes = 28
                Dia = 1
                NDiasVenda = 0
                while Dia <= NDiasMes:
                        a = DiaSemana (Ano, Mes, Dia)
                        if a != 6:
                                NDiasVenda = NDiasVenda + 1
                        Dia = Dia + 1
                QtdeVendidaMes = QtdeVendasDia * NDiasVenda
 
arquivo = open ('RelVendas.txt', 'w')
 
from random import randint
 
cont = 1
Dia = 1
while cont <= QtdeVendidaMes:
        r = randint (0,14)
 
        Cod = Codigo[r]
        Estoq = Estoque[r]
        PrecoVenda = Custo[r]*Margem[r]
 
        texto1 = ("{Ano};".format(Ano=Ano))
        texto2 = ("{Mes:02d};".format(Mes=Mes))
        texto3 = ("{Dia:02d};".format(Dia=Dia))
        texto4 = ("{Cod};".format(Cod=Cod))
        texto5 = ("{Estoq};".format(Estoq=Estoq))
        texto6 = ("{PrecoVenda:.2f};".format(PrecoVenda=PrecoVenda))
 
        arquivo.write(texto1)
        arquivo.write(texto2)
        arquivo.write(texto3)
        arquivo.write(texto4)
        arquivo.write(texto5)
        arquivo.write(texto6)
        if (QtdeVendidaMes - cont) > 0:
                arquivo.write("\n")
        if (cont % QtdeVendasDia) == 0:
                Dia = Dia + 1
        if a == 6:
                Dia = Dia + 1
        cont = cont + 1
 
arquivo.close()
