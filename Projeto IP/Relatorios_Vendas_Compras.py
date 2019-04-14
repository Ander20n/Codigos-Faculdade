class Relatorios:
    
    def __init__(self):
        pass
    
    def dados_compras(self):
        criar = open('Relatorio Compras.txt','a')
        criar.close()
        arq = open('Relatorio Compras.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        arq.close()
        return lis
        
    def Compras(self,mat,lis):
        limite = 0
        if len(lis) == 0:
            print("Nenhuma compra foi realizada")
        else:    
            for p in range(len(lis)):
                if mat != lis[p][1]:
                    limite += 1 
                    if limite == len(lis):
                        print("O funcionario nao realizou compras\n")
                elif mat == lis[p][1]:
                    d = p
                    print("CNPJ: %s\nFuncionario: %s\nProduto: %s\nQuantidade comprada: %s\nPreco total: %s" % (lis[d][0],lis[d][1],lis[d][2],lis[d][3],lis[d][4]))
    
    def AllCompras(self,lis):
        print('Todas compras feitas\n')
        for x in range(len(lis)):
            print("CNPJ: %s\nFuncionario: %s\nProduto: %s\nQuantidade comprada: %s\nPreco total: %s" % (lis[x][0],lis[x][1],lis[x][2],lis[x][3],lis[x][4]))
    
    def PrintarCompras(self):
        user = int(input("MENU RELATORIO DE COMPRAS\n\n1 - Mostrar todas compras realizadas\n2 - Procurar por funcionario\nSua escolha: "))
        if user == 1:
            Relatorios.AllCompras(self, Relatorios.dados_compras(self))
            Relatorios.PrintarCompras(self)
        elif user == 2:
            mat = int(input("Matricula do funcionario: "))
            Relatorios.Compras(self, str(mat), Relatorios.dados_compras(self))
            Relatorios.PrintarCompras(self)
        else:
            print("Opcao invalida\n")
            Relatorios.PrintarCompras(self)
            
    def dados_vendas(self):
        criar = open('Relatorio Vendas.txt','a')
        criar.close()
        arq = open('Relatorio Vendas.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        arq.close()
        return lis
        
    def Vendas(self,mat,lis):
        limite = 0
        if len(lis) == 0:
            print("Nenhuma compra foi realizada")
        else:    
            for p in range(len(lis)):
                if mat != lis[p][0]:
                    limite += 1 
                    if limite == len(lis):
                        print("O cliente nao realizou compras\n")
                elif mat == lis[p][0]:
                    d = p
                    print("CPF: %s\nFuncionario: %s\nProduto: %s\nQuantidade comprada: %s" % (lis[d][0],lis[d][1],lis[d][2],lis[d][3]))
    
    def AllVendas(self,lis):
        print('Todas vendas realizadas\n')
        for x in range(len(lis)):
            print("CPF: %s\nFuncionario: %s\nProduto: %s\nQuantidade comprada: %s" % (lis[x][0],lis[x][1],lis[x][2],lis[x][3]))
    
    def PrintarVendas(self):
        user = int(input("MENU RELATORIO DE VENDAS\n\n1 - Mostrar todas vendas realizadas\n2 - Procurar por cliente\nSua escolha: "))
        if user == 1:
            Relatorios.AllVendas(self, Relatorios.dados_vendas(self))
            Relatorios.PrintarVendas(self)
        elif user == 2:
            cpf = int(input("CPF do cliente: "))
            if len(str(cpf)) < 11:
                cpf = (str(0)) * (11 - (len(str(cpf)))) + str(cpf)
            print(cpf)
            Relatorios.Vendas(self, str(cpf), Relatorios.dados_vendas(self))
            Relatorios.PrintarVendas(self)
        else:
            print("Opcao invalida\n")
            Relatorios.PrintarCompras(self)
        
#R = Relatorios()
#R.PrintarVendas()