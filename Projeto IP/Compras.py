from Fornecedores import Fornecedores
from CategoriasProdutos import CateProd
from Funcionarios import Funcionarios

func = Funcionarios()
CP = CateProd()
forn = Fornecedores() 


class Compras:
    
    def __init__(self):
        pass
     
    def RelaCompra(self,CNPJ,MAT,COD,QUA,PRE):
        arq = open('Relatorio Compras.txt','a')
        arq.write(str(CNPJ) + '{/' + str(MAT) + '{/' + str(COD) + '{/' + str(QUA) + '{/' + str(PRE) + '\n')
        arq.close
        
    def AlterarProdComp(self,cod,qua,pre,poscod,listprod):
        for x in range(len(listprod)):
            if poscod == x:
                va = listprod[x][4]
                nv = int(va) + qua
                listprod[x][4] = str(nv)
                listprod[x][7] = str(pre)
        
        return listprod
                
    def CNPJCadastrado(self,CNPJ,lis):
        limite = 0
        for p in range(len(lis)):
            if CNPJ != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    return 0
            if CNPJ == lis[p][0]:
                return 1
    
    def MatriculaCadastrada(self,MAT,lista):
        limite = 0
        for p in range(len(lista)):
            if str(MAT) != lista[p][0]:
                limite += 1 
                if limite == len(lista):
                    return 0
            if str(MAT) == lista[p][0]:
                return 1
    
    def ProdutoCadastrado(self,cod,lisp):
        limite = 0
        for p in range(len(lisp)):
            if str(cod) != lisp[p][0]:
                limite += 1 
                if limite == len(lisp):
                    return 0
            if str(cod) == lisp[p][0]:
                    return 1
            
    def MenuCompras(self):
        CNPJ = input("MENU DE COMPRAS\nCNPJ do fornecedor: ")
        if len(str(CNPJ)) < 13:
                CNPJ = (str(0)) * (13 - (len(str(CNPJ)))) + str(CNPJ)
        val = Compras.CNPJCadastrado(self,CNPJ,forn.DadosFornecedores())
        if val == 0:
            print("CNPJ nao cadastrado, informe um CPNJ valido\n")
            Compras.MenuCompras(self)
        else:
            mat = int(input("Matricula do vendedor: "))
            val2 = Compras.MatriculaCadastrada(self, mat, func.DadosFuncionarios())
            if val2 == 0:
                print("Matricula nao cadastrada\n ")
                Compras.MenuCompras(self)
            else:
                cod = input("Codigo do produto: ")
                val3 = Compras.ProdutoCadastrado(self, cod, CP.DadosProdutos())
                if val3 == 0:
                    print("Produto nao cadastrado\n")
                    Compras.MenuCompras(self)
                qua = int(input("Quantidade comprada: "))
                if qua <= 0: 
                    qua = int(input("Informe uma quantidade positiva\nQuantidade comprada: "))
                pre = float(input("Preco de compra: "))
                prect = qua*pre
        Compras.RelaCompra(self,CNPJ,mat,cod,qua,prect)
        Compras.AlterarProdComp(self, cod, qua, pre, CP.CodProd_Editar_Remover(cod, CP.DadosProdutos()), CP.DadosProdutos())
        CP.Prod_SalvarDadosEditados(Compras.AlterarProdComp(self,cod,qua,pre,CP.CodProd_Editar_Remover(cod, CP.DadosProdutos()), CP.DadosProdutos()))
        
