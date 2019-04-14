from Fornecedores import Fornecedores
from CategoriasProdutos import CateProd
from Funcionarios import Funcionarios
from Clientes import Clientes
from Vendas import Vendas
from Relatorios_Vendas_Compras import Relatorios
from ControleEstoque import ContEstoque

func = Funcionarios()
CP = CateProd()
forn = Fornecedores() 
Cl = Clientes()
Ve = Vendas()
Re = Relatorios()
Ce = ContEstoque

class MenuOpcoes:
    
    def __init__(self):
        pass
    
    def MostrarMenu(self):
        print("MENU OPCOES\n\n1 - Categorias e Produtos\n2 - Funcionarios\n3 - Fornecedores\n4 - Vendas\n5 - Clientes\n6 - Relatorio de Vendas\n7 - Relatorio de Compras\n8 - Controle de Estoque")
        user = int(input("\nEscolha o numero da sua opcao: "))
        if user == 0 or user < 0 or user > 8:
            print("Opcao errada\n")
            MenuOpcoes.MostrarMenu(self)
        elif user == 1:
            CP.ChamadaMenu()
        elif user == 2:
            func.ChamadaMenuFuncionarios()
        elif user == 3:
            forn.ChamadaMenuFornecedores()
        elif user == 4:
            Ve.MenuVendas()
        elif user == 5:
            Cl.ChamadaMenuClientes()
        elif user == 6:
            Re.PrintarVendas()
        elif user == 7:
            Re.PrintarCompras()
        elif user == 8:
            Ce.Menu()
        
#MO = MenuOpcoes()    
#MO.MostrarMenu()