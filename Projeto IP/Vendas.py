from CategoriasProdutos import CateProd
from Clientes import Clientes
from Compras import Compras
from Funcionarios import Funcionarios

CP = CateProd()
Cl = Clientes()
Co = Compras()
func = Funcionarios()

class Vendas:
    
    def __init__(self):
        pass

    def PrintCategorias(self,Cate):
        for x in range(len(Cate)):
            print("Codigo: %s - Categoria: %s" % (Cate[x][0],Cate[x][1][:-1]))
          
    '''def PrintProdutos(self,Prod):
        print('PRODUTOS DISPONIVEIS\n')
        for x in range(len(Prod)):
            print("Codigo: %s - Descricao: %s - Preco: R$ %s" % (Prod[x][0],Prod[x][1][:-1],Prod[x][6]))'''
    
    def ProdutosCodigos(self,LisProd,CodProd):
        limite = 0 
        for x in range(len(LisProd)):
            if str(CodProd) != LisProd[x][2]:
                limite += 1
                if limite == len(LisProd):
                    return 0
            elif str(CodProd) == LisProd[x][2]:
                print('Codigo: %s - Descricao: %s - Preco: R$ %s - Pecas Disponiveis: %s unidades' % (LisProd[x][0],LisProd[x][1],LisProd[x][6],LisProd[x][4]))
     
    def ProdutoCadastrado(self,cod,lisp):
        limite = 0
        for p in range(len(lisp)):
            if str(cod) != lisp[p][0]:
                limite += 1 
                if limite == len(lisp):
                    return 0
            if str(cod) == lisp[p][0]:
                    return 1
    
    def CPFCadastrado(self,CPF,lista):
        limite = 0
        for p in range(len(lista)):
            if str(CPF) != lista[p][0]:
                limite += 1 
                if limite == len(lista):
                    return 0
            if str(CPF) == lista[p][0]:
                return 1
            
    def QuantLiberada(self,pecas,cod,prod):
        for x in range(len(prod)):
            if cod == x:
                pd = prod[x][4]
                val = int(pd) - pecas
        
        return val
        
    def AlterarProdComp(self,quan,poscod,lis_pro):
        for x in range(len(lis_pro)):
            if poscod == x:
                va = lis_pro[x][4]
                nv = int(va) - quan
                lis_pro[x][4] = str(nv)
            
        return lis_pro 
    
    def RelaVenda(self,CPF,MAT,PROD,QUAN):
        arq = open('Relatorio Vendas.txt','a')
        arq.write(str(CPF) + '{/' + str(MAT) + '{/' + str(PROD) + '{/' + str(QUAN) + '\n')
        arq.close
    
    def MenuVendas(self):
        print('MENU DE VENDAS\n\n1 - Categorias/Produtos\n')
        user = int(input("\nSua Opcao: "))
        if user == 1:
            Vendas.PrintCategorias(self,CP.DadosCategorias())
            cod = int(input("\nInforme o codigo da categoria: "))
            dec = Vendas.ProdutosCodigos(self,CP.DadosProdutos(),cod)
            if dec == 0:
                print("Categoria nao cadastrada\n")
                Vendas.MenuVendas(self)
            else:
                du = int(input("\n0 - Voltar ao Menu de compras\n1 - Continuar a compra\nOpcao: "))
                if du < 0 or du >1:
                    print("Opcao invalida\n")
                    Vendas.MenuVendas(self)
                elif du == 0:
                    Vendas.MenuVendas(self)
                elif du == 1:
                    Prod = int(input("\nInforme do codigo do produto que deseja comprar: "))
                    Val1 = Vendas.ProdutoCadastrado(self,str(Prod), CP.DadosProdutos())
                    if Val1 == 0:
                        print("Produto nao cadastrado\n")
                        Vendas.MenuVendas(self)
                    else:
                        CPFUser = input("Informe o CPF do comprador: ")
                        val2 = Vendas.CPFCadastrado(self, CPFUser, Cl.DadosClientes())
                        if val2 == 0:
                            print("CPF nao cadastrado\n")
                            Cl.AdicionarCliente()
                            mat = int(input("Matricula do vendedor: "))
                            val2 = Co.MatriculaCadastrada(mat, func.DadosFuncionarios())
                            if val2 == 0:
                                print("Matricula nao cadastrada\n ")
                                Vendas.MenuVendas(self)
                            else:
                                quan = int(input("Unidades compradas: "))
                                val3 = Vendas.QuantLiberada(self, quan, CP.CodProd_Editar_Remover(str(Prod), CP.DadosProdutos()), CP.DadosProdutos())
                                if val3 == 0 or val3 < 0:
                                    print("Quantidade indisponivel, compra cancelada\n")
                                    Vendas.MenuVendas(self)
                                else:
                                    print("Compra Finalizada\n")
                        elif val2 == 1:
                            mat = int(input("Matricula do vendedor: "))
                            val2 = Co.MatriculaCadastrada(mat, func.DadosFuncionarios())
                            if val2 == 0:
                                print("Matricula nao cadastrada\n ")
                                Vendas.MenuVendas(self)
                            else:
                                quan = int(input("Unidades compradas: "))
                                val3 = Vendas.QuantLiberada(self, quan, CP.CodProd_Editar_Remover(str(Prod), CP.DadosProdutos()), CP.DadosProdutos())
                                if val3 == 0 or val3 < 0:
                                    print("Quantidade indisponivel, compra cancelada\n")
                                    Vendas.MenuVendas(self)
                                else:
                                    print("Compra Finalizada\n")
                                
            Vendas.RelaVenda(self,CPFUser,str(mat),str(Prod),str(quan))
            Vendas.AlterarProdComp(self,quan,CP.CodProd_Editar_Remover(str(Prod), CP.DadosProdutos()), CP.DadosProdutos())
            CP.Prod_SalvarDadosEditados(Vendas.AlterarProdComp(self,quan,CP.CodProd_Editar_Remover(str(Prod), CP.DadosProdutos()), CP.DadosProdutos()))
            Vendas.MenuVendas(self)    
        else:
            print('Opcao invalida\n')  
            print(Vendas.MenuVendas(self))


#V = Vendas()
#V.MenuVendas()

#print(DadosCategorias())
#PrintCategorias(DadosCategorias())
#PrintProdutos(DadosProdutos())