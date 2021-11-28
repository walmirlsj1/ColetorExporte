""" 
Data: 12/01/2019 15:47:00
Autor: Walmir
"""

import csv
import os


class Busca2():
    def __init__(self):
        self.achei = 0
        self.entrada = "./dadoscolhetor.csv"
        self.resultado = "./dados_pronto.csv"
        self.delimiter = self.delimiter(self.entrada)
        self.feitos = "./outros/.Feitos.txt"
        flimpa = open(self.feitos, 'w')
        flimpa.write("")
        flimpa.close()
        flimpa = open(self.resultado, 'w')
        flimpa.write("Codigo;Descr;Quant\n")
        flimpa.close()

    def buscar(self, cod_result):
        f_csv = csv.reader(open(self.entrada), delimiter=self.delimiter)
        search = 0
        qtd_result = 0
        count = 0
        for [Codigo, Quant] in f_csv:
            cod_ = Codigo.strip()
            # dest_ = Descr.strip()
            quant_ = Quant.strip()
            cod_result = cod_result.strip()
            if cod_.strip() == cod_result.strip():
                #print("%s == %s" % (cod_result, Codigo))
                if quant_.strip() == "":
                    qtd_result += int(0)
                else:
                    qtd_result += int(quant_)
                count += 1
        self.salvar(cod_result, qtd_result)
        #print("%s;%s;%s -- Repete: %s\n" % (cod_result, "", qtd_result, count))

    def inicio(self):
        achei = 0
        tamanho = 0
        count = 0
        f = csv.reader(open(self.entrada), delimiter=self.delimiter)
        for [Codigo, Quant] in f:
            tamanho = tamanho + 1
        print(tamanho)
        # f.close()
        f_txt = csv.reader(open(self.entrada), delimiter=self.delimiter)
        for [Codigo, Quant] in f_txt:
            os.system('cls' if os.name == 'nt' else 'clear')
            count = count + 1
            porcentagem = (count / tamanho * 100)
            print("############################")
            print("############################")
            print("Encontrados %s de %s" % (count, tamanho))
            print("Buscando Barra: %s " % Codigo)
            print("Concluido %.2f %s " % (porcentagem, "%"))
            print("############################")
            print("############################")
            #print(self.verificarFeitos(Codigo.strip()))
            
            if self.verificarFeitos(Codigo.strip()) == False:
                self.inserirFeitos(Codigo.strip())
                self.buscar(Codigo.strip())

    def inserirFeitos(self, cod):
        try:
            f = open(self.feitos, "a")
            f.write("%s\n" % (cod.strip()))
            f.close()
        except Exception:
            return False
        return

    def verificarFeitos(self, cod):
        r = False
        try:
            f = open(self.feitos, "r")
            for cod_ in f:
                if cod_.strip() == cod.strip():
                    r = True
            f.close()
            return r
        except Exception:
            return False
        return

    def salvar(self, Codigo, Quant):
        try:
            f = open(self.resultado, "a")
            f.write("%s;%s;%s\n" % (Codigo, "", Quant))
            f.close()
        except Exception:
            pass
        return
    
    def delimiter(self, filename):
        with open(filename, 'r') as myCsvfile:
            header=myCsvfile.readline()
            if header.find(";")!=-1:
                return ";"
            if header.find(",")!=-1:
                return ","
            #default delimiter (MS Office export)
        return ";"

if __name__ == "__main__":
    f2 = Busca2()
    f2.inicio()
    

