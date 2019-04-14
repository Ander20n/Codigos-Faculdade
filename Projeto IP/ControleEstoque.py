from CategoriasProdutos import CateProd
from Compras import Compras
#from MenuOpcoes import MenuOpcoes

Co = Compras()
CP = CateProd()
#Mo = MenuOpcoes()

class ContEstoque:
    def __init__(self):
        pass
    
    def LimiteEstoque(self,LisProd):
        limite = 0
        if LisProd == 'vazio':
            return 'vazio'
        else:
            for x in range(len(LisProd)):
                if int(LisProd[x][4]) <= int(LisProd[x][5]):
                    print("%s - CODIGO %s - tem %s pecas disponiveis" % (LisProd[x][1],LisProd[x][0],LisProd[x][4]))
                else:
                    if int(LisProd[x][4]) > int(LisProd[x][5]):
                        limite += 1
                        if limite == len(LisProd):
                            return 0
        
    def Menu(self):
        Res = ContEstoque.LimiteEstoque(self,CP.DadosProdutos())
        if Res == 'vazio':
            print("SEJA BEM VINDO AO CONTROLE DA LOJA, INICIE ADICIONANDO FUNCIONARIOS, DEPOIS CLIENTES E EM SEGUIDA CATEGORIAS E PRODUTOS\n")
            #Mo.MostrarMenu()
        elif Res == 0:
            return("Estoque normal")
        else:
            Res
            Co.MenuCompras()

Contro = ContEstoque()
Contro.Menu()