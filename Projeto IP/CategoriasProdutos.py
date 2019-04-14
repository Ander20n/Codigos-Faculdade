from Funcionarios import Funcionarios
from Fornecedores import Fornecedores

func = Funcionarios()
forn = Fornecedores()

class CateProd:
    def __init__(self):
        pass

    def DadosCategorias(self):
        arq = open('Categorias.txt','r')
        lin_cate = arq.readlines()
        lis_cate = []
        for x in lin_cate:
            dados = x.split('{/')
            lis_cate.append(dados)
        arq.close()
        return lis_cate
    
    def DadosProdutos(self):
        criar = open('Produtos.txt','a')
        criar.close()
        arq = open('Produtos.txt','r')
        lin_prod = arq.readlines()
        lis_prod = []
        for x in lin_prod:
            dados = x.split('{/')
            lis_prod.append(dados)
        arq.close()
        if len(lis_prod) == 0:
            lis_prod = 'vazio'
        return lis_prod
    
    def ArqCat_VazioouNao(self):
        criar = open('Categorias.txt','a')
        criar.close()
        arq = open('Categorias.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        if len(lis) == 0:
            return 0
        else:
            return 1
        arq.close()
    
    def ArqPro_VazioouNao(self):
        criar = open('Produtos.txt','a')
        criar.close()
        arq = open('Produtos.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        if len(lis) == 0:
            return 0
        else:
            return 1
        arq.close()    
        
    def Cat_CadastradoOuNao(self,UserCat):
        arq = open('Categorias.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if str(UserCat) != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    resposta = "not"
                    return resposta
            else:
                resposta ="yes"
                return resposta
        arq.close()
        
    def DescCat_CadasOuNao(self,UserDescCat):
        arq = open('Categorias.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if UserDescCat != lis[p][1]:
                limite += 1 
                if limite == len(lis):
                    resposta = "not"
                    return resposta
            else:
                resposta ="yes"
                return resposta
        arq.close()    
    
    #APAGAR EM CASO DE ERRO COMECA AQUI
    
    def RelaCompra(self,CNPJ,MAT,COD,QUA,PRE):
        arq = open('Relatorio Compras.txt','a')
        arq.write(str(CNPJ) + '{/' + str(MAT) + '{/' + str(COD) + '{/' + str(QUA) + '{/' + str(PRE) + '\n')
        arq.close
        
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
    
    #TERMINA AQUI
    
    def DescProd_CadasOuNao(self,UserDescProd):
        arq = open('Produtos.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if UserDescProd != lis[p][1]:
                limite += 1 
                if limite == len(lis):
                    resposta = "not"
                    return resposta
            else:
                resposta ="yes"
                return resposta
        arq.close()    
        
    def Prod_CadastradoOuNao(self,UserProd):
        arq = open('Produtos.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if str(UserProd) != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    return "not"
            else:
                return "yes"
        arq.close()
    
    def AdicionarCategorias(self):
        codigo = int(input("Informe o codigo da categoria: "))
        ListaVazia = CateProd.ArqCat_VazioouNao(self)
        if ListaVazia == 0 or ListaVazia == 1:
            arq = open('Categorias.txt','a')
            decisao = CateProd.Cat_CadastradoOuNao(self,codigo)
            if decisao == 'yes':
                print("Codigo cadastrado, favor escolher uma nova opcao no Menu\n")
                CateProd.MenuCategorias(self)
            elif decisao == 'not':
                descricao = input("Descricao da Categoria: ")
                dec = CateProd.DescCat_CadasOuNao(self,str(descricao))
                if dec == 'yes':
                    print("Descriao cadastrada, favor escolher uma nova opcao no Menu\n")
                    CateProd.MenuCategorias(self)
                else:
                    arq.write(str(codigo) + '{/' + descricao + '\n')
        
            arq.close()
    
    def AdicionarProdutos(self):
        CNPJ = input("MENU DE COMPRAS\nCNPJ do fornecedor: ")
        if len(str(CNPJ)) < 13:
                CNPJ = (str(0)) * (13 - (len(str(CNPJ)))) + str(CNPJ)
        val = CateProd.CNPJCadastrado(self, CNPJ, forn.DadosFornecedores())
        if val == 0:
            print("CNPJ nao cadastrado, informe um CPNJ valido\n")
            CateProd.MenuProdutos(self)
        else:
            mat = int(input("Matricula do vendedor: "))
            val2 = CateProd.MatriculaCadastrada(self, mat, func.DadosFuncionarios())
            if val2 == 0:
                print("Matricula nao cadastrada\n ")
                CateProd.MenuProdutos(self)
            else:
        #EM CASO DE ERRO, APAGAR DE CIMA ATE AQUI
                cp = int(input("Informe o codigo do produto: "))
                ListaVazia = CateProd.ArqPro_VazioouNao(self)
                if ListaVazia == 0 or ListaVazia == 1:
                    arq = open('Produtos.txt','a')
                    decisao = CateProd.Prod_CadastradoOuNao(self,cp)
                    if decisao == 'yes':
                        print("Codigo cadastrado, favor escolher uma nova opcao no Menu\n")
                        CateProd.MenuProdutos(self)
                    else:
                        dp = input("Descricao do produto: ")
                        dec = CateProd.DescProd_CadasOuNao(self,str(dp))
                        if dec == 'yes':
                            print("Descriao cadastrada, favor escolher uma nova opcao no Menu\n")
                            CateProd.MenuCategorias(self)
                        cap = input("Codigo da Categoria: ")
                        fp = input("Foto do produto: ")
                        emaxp = int(input("Estoque maximo do produto: "))
                        eminp = int(input("Estoque minimo do produto: "))
                        while eminp >= emaxp:
                            eminp = int(input("O valor do estoque minimo precisa ser menor que estoque maximo\nEstoque Minimo: "))
                        calcomp = float(input("Valor de compra: "))
                        valvenp = float(input("Valor de venda: "))
                        while valvenp <= calcomp:
                            valvenp = float(input("O valor de venda do produto precisa ser maior que o valor de compra\nValor de venda do produto: "))
                        arq.write(str(cp) + '{/' + dp + '{/' + cap + '{/' + fp + '{/'  + str(emaxp) + '{/' + str(eminp) + '{/' + str(valvenp) + '{/' + str(calcomp) + '\n')
                        
                        prect = emaxp * calcomp
                        CateProd.RelaCompra(self, CNPJ, mat, cp, emaxp, prect)
                        
                    arq.close()
        
    def CodCate_Editar_Remover(self,cod_cate_user,lis_cate):
        limite = 0
        for x in range(len(lis_cate)):
            if cod_cate_user != lis_cate[x][0]:
                limite += 1 
                if limite == len(lis_cate):
                    Pos_Cod_Cate = 'Categoria nao cadastrada'
                    return Pos_Cod_Cate
            else:
                Pos_Cod_Cate = x
                return Pos_Cod_Cate
    
    def CodProd_Editar_Remover(self,cod_prod_user,lis_prod):
        limite = 0
        for x in range(len(lis_prod)):
            if cod_prod_user != lis_prod[x][0]:
                limite += 1 
                if limite == len(lis_prod):
                    Pos_Cod_Prod = "Produto nao cadastrado"
                    return Pos_Cod_Prod
            else:
                Pos_Cod_Prod = x
                return Pos_Cod_Prod
            
    def Consultar_Categorias(self,cod,lis_cate):
        limite = 0
        for p in range(len(lis_cate)):
            if cod != lis_cate[p][0]:
                limite += 1 
                if limite == len(lis_cate):
                    return("Categoria nao cadastrada")
            if cod == lis_cate[p][0]:
                d = p
                return("\nCodigo: %s\nCategoria: %s" % (lis_cate[d][0],lis_cate[d][1]))
    
    def Consultar_Produtos(self,cod,lis_prod):
        limite = 0
        for p in range(len(lis_prod)):
            if cod != lis_prod[p][0]:
                limite += 1 
                if limite == len(lis_prod):
                    return("Produto nao cadastrada")
            if cod == lis_prod[p][0]:
                d = p
                return("\nCodigo: %s\nCategoria: %s\nFoto: %s\nDescricao: %s\nEstoque Maximo: %s\nEstoque Minimo: %s\nValor base venda: %s\nValor base compra: %s" % (lis_prod[d][0],lis_prod[d][1],lis_prod[d][2],lis_prod[d][3],lis_prod[d][4],lis_prod[d][5],lis_prod[d][6],lis_prod[d][7]))   
    
    def Cat_EditarRemover(self,decisao,Pos_Cod_Cate,lis_cate):
        criar = open('Categorias.txt','a')
        criar.close
        if decisao.lower() == "remover":
            if Pos_Cod_Cate == 'Categoria nao cadastrada':
                print(Pos_Cod_Cate)
            else:
                del lis_cate[Pos_Cod_Cate]
        
        elif decisao.lower() == 'editar':    
            if Pos_Cod_Cate == 'Categoria nao cadastrada':
                print(Pos_Cod_Cate)
            else:
                newdesc = input("Descricao: ")
            
                lis_cate[Pos_Cod_Cate][1] = newdesc +'\n'
            
        return lis_cate
    
    def Prod_EditarRemover(self,decisao,Pos_Cod_Prod,lis_prod):
        criar = open('Produtos.txt','a')
        criar.close
        if decisao.lower() == "remover":
            if Pos_Cod_Prod == "Produto nao cadastrado":
                print(Pos_Cod_Prod)
            else:
                del lis_prod[Pos_Cod_Prod]
        
        elif decisao.lower() == 'editar':    
            if Pos_Cod_Prod == "Produto nao cadastrado":
                print(Pos_Cod_Prod)
            else:
            
                newcate = input("Codigo da Categoria: ")
                newfoto = input("Foto: ")
                newdesc = input("Descricao: ")
                newestmax = int(input("Estoque Maximo: "))
                newestmin = int(input("Estoque Minimo: "))
                while newestmin >= newestmax:
                    newestmin = int(input("O valor do estoque minimo precisa ser menor que estoque maximo\nEstoque Minimo: "))
                newvc = float(input("Valor compra: "))
                newvv = float(input("Valor venda: "))
                while newvv <= newvc:
                    newvv = float(input("O valor de venda do produto precisa ser maior que o valor de compra\nValor de venda do produto: "))
            
                lis_prod[Pos_Cod_Prod][1] = newcate
                lis_prod[Pos_Cod_Prod][2] = newfoto
                lis_prod[Pos_Cod_Prod][3] = newdesc
                lis_prod[Pos_Cod_Prod][4] = str(newestmax)
                lis_prod[Pos_Cod_Prod][5] = str(newestmin)
                lis_prod[Pos_Cod_Prod][6] = str(newvv)
                lis_prod[Pos_Cod_Prod][7] = str(newvc)
            
        return lis_prod
    
    def Cat_SalvarDadosEditados(self,lis_cate):
        arq = open('Categorias.txt','w')
        lista = lis_cate
        for x in lista:
            p = '{/'.join(x)
            arq.write(p)
        arq.close()
    
    def Prod_SalvarDadosEditados(self,lis_prod):
        arq = open('Produtos.txt','w')
        lista = lis_prod
        for x in lista:
            p = '{/'.join(x)
            arq.write(p)
        arq.close()
        
    def ChamadaMenu(self):
        print("1 - Trabalhar com Categorias\n2 - Trabalhar com Produtos\n")
        user = int(input("Escolha sua opcao: "))
        if user == 1:
            CateProd.MenuCategorias(self)
        elif user == 2:
            CateProd.MenuProdutos(self)
        else:
            print("Opcao invalida")
            CateProd.ChamadaMenu(self)
    
    def MenuCategorias(self):
        
        print("\nMENU DE CATEGORIAS\n\n1 - Adicionar\n2 - Consultar\n3 - Editar\n4 - Remover\n5 - Voltar\n")
        user = int(input("Escolha sua opcao: "))
    
        if user == 1:
            CateProd.AdicionarCategorias(self)
            CateProd.MenuCategorias(self)
        elif user == 2:
            codcat = input("Informe o codigo da categoria que deseja consultar: ")
            resultado =  CateProd.ArqCat_VazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de categorias, adicione um categoria no menu de categorias")
                CateProd.MenuCategorias(self)
            else:
                print(CateProd.Consultar_Categorias(self,codcat, CateProd.DadosCategorias(self)))
                CateProd.MenuCategorias(self)
        elif user == 3:
            CODCATeditar = input("Informe o codigo da categoria que deseja editar: ")
            resultado = CateProd.ArqCat_VazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de categorias, adicione um categoria no menu de categorias")
                CateProd.MenuCategoriasself()
            else:
                decisao = CateProd.Cat_EditarRemover(self,'editar',CateProd.CodCate_Editar_Remover(self,CODCATeditar,CateProd.DadosCategorias(self)),CateProd.DadosCategorias(self))
                CateProd.Cat_SalvarDadosEditados(self,decisao)
                CateProd.MenuCategorias(self)
        elif user == 4:
            user = input("Informe o codigo da categoria que deseja remover: ")
            resultado = CateProd.ArqCat_VazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de categorias, adicione um categoria no menu de categorias")
                CateProd.MenuCategorias(self)
            else:
                decisao2 = CateProd.Cat_EditarRemover(self,'remover',CateProd.CodCate_Editar_Remover(self,user,CateProd.DadosCategorias(self)),CateProd.DadosCategorias(self))
                CateProd.Cat_SalvarDadosEditados(self, decisao2)
                CateProd.MenuCategorias(self)
        elif user == 5:
            CateProd.ChamadaMenu(self)
        else:
            print("\nOPCAO INVALIDA\n")
            CateProd.MenuCategorias(self)
    
    def MenuProdutos(self):
        
        print("\nMENU DE PRODUTOS\n\n1 - Adicionar\n2 - Consultar\n3 - Editar\n4 - Remover\n5 - Voltar\n")
        user = int(input("Escolha sua opcao: "))
    
        if user == 1:
            CateProd.AdicionarProdutos(self)
            CateProd.MenuProdutos(self)
        elif user == 2:
            codprod = input("Informe o codigo da produto que deseja consultar: ")
            resultado = CateProd.ArqPro_VazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum produto, adicione um produto no menu de produtos")
                CateProd.MenuProdutos(self)
            else:
                print(CateProd.Consultar_Produtos(self,codprod, CateProd.DadosProdutos(self)))
                CateProd.MenuProdutos(self)
        elif user == 3:
            CODPROD = input("Informe o codigo do produto que deseja editar: ")
            resultado = CateProd.ArqPro_VazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum produto, adicione um produto no menu de produtos")
                CateProd.MenuProdutos(self)
            else:
                decisao = CateProd.Prod_EditarRemover(self,'editar',CateProd.CodProd_Editar_Remover(self,CODPROD,CateProd.DadosProdutos(self)),CateProd.DadosProdutos(self))
                CateProd.Prod_SalvarDadosEditados(self,decisao)
                CateProd.MenuProdutos(self)
        elif user == 4:
            user = input("Informe o codigo do produto que deseja editar: ")
            resultado = CateProd.ArqPro_VazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum produto, adicione um produto no menu de produtos")
                CateProd.MenuProdutos(self)
            else:
                decisao2 = CateProd.Prod_EditarRemover(self,'remover',CateProd.CodProd_Editar_Remover(self,user,CateProd.DadosProdutos(self)),CateProd.DadosProdutos(self))
                CateProd.Prod_SalvarDadosEditados(self,decisao2)
                CateProd.MenuProdutos(self)
        elif user == 5:
            CateProd.ChamadaMenu(self)
        else:
            print("\nOPCAO INVALIDA\n")
            CateProd.MenuProdutos(self)