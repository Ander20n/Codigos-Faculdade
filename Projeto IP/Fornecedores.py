class Fornecedores:
    
    def __init__(self):
        pass
    
    def DadosFornecedores(self):
        arq = open('Fornecedores.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        arq.close()
        return lis
    
    def ArquivoVazioouNao(self):
        criar = open('Fornecedores.txt','a')
        criar.close()
        arq = open('Fornecedores.txt','r')
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
    
    def CNPJ_CadastradoOuNao(self,UserCNPJ):
        arq = open('Fornecedores.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if str(UserCNPJ) != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    resposta = "not"
                    return resposta
            else:
                resposta ="yes"
                return resposta
        arq.close()
    
    def AdicionarFornecedores(self):
        cnp = int(input("CNPJ: "))
        if len(str(cnp)) < 13:
                cnp = (str(0)) * (13 - (len(str(cnp)))) + str(cnp)
        ListaVazia = Fornecedores.ArquivoVazioouNao(self)
        if ListaVazia == 0 or ListaVazia == 1:
            arq = open('Fornecedores.txt','a')
            decisao = Fornecedores.CNPJ_CadastradoOuNao(self,cnp)
            if decisao == 'yes':
                print("CNPJ cadastrado, favor escolher uma nova opcao no Menu\n")
                Fornecedores.ChamadaMenuFornecedores(self)
            else:
                nom = input("Nome: ")
                end = input("Endereco: ")
                bai = input("Bairro: ")
                cid = input("Cidade: ")
                cep = int(input("CEP: "))
                while len(str(cep)) < 8 or len(str(cep)) > 8:
                    cep = int(input("Informe um valor de 8 digitos\nCEP: "))
                est = input("Estado: ")
                tel = int(input("Telefone (Digite 0, caso nao possua): "))
                if tel == 0:
                    tel = 'Nao possui'
                cel = int(input("Celular (Digite 0, caso nao possua): "))
                if cel == 0:
                    cel = 'Nao possui'
                fax = int(input("Fax (Digite 0, caso nao possua): "))
                if fax == 0:
                    fax = 'Nao possui'
                ema = input("Email (Digite 0, caso nao possua):")
                if ema == 0:
                    fax = 'Nao possui'
        
                arq.write(str(cnp) + '{/' + nom + '{/' + end + '{/' + bai + '{/' + cid + '{/' + str(cep) + '{/' + est + '{/' + str(tel) + '{/' + str(cel) + '{/' + str(fax) + '{/' + ema + '\n')
      
            arq.close()
    
    def CNPJ_Editar_Remover(self,CNPJUser,lis):
        limite = 0
        for p in range(len(lis)):
            if CNPJUser != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    d = "CNPJ nao cadastrado"
                    return d
            else:
                d = p
                return d
    
    def ConsultarFornecedores(self,CNPJConsulta,lis):
        limite = 0
        for p in range(len(lis)):
            if CNPJConsulta != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    return("CNPJ nao cadastrado")
            if CNPJConsulta == lis[p][0]:
                d = p
                return("\nCNPJ: %s\nNome: %s\nEndereco: %s\nBairro: %s\nCidade: %s\nCEP: %s\nEstado: %s\nTelefone: %s\nCelular: %s\nFax: %s\nEmail: %s " % (lis[d][0],lis[d][1],lis[d][2],lis[d][3],lis[d][4],lis[d][5],lis[d][6],lis[d][7],lis[d][8],lis[d][9],lis[d][10]))
    
    def EditarRemoverFornecedores(self,decisao,d,lis):
        criar = open('Clientes.txt','a')
        criar.close
        if decisao.lower() == "remover":
            if d == "CNPJ nao cadastrado":
                print(d)
            else:
                del lis[d]
        
        elif decisao.lower() == 'editar':
            if d == "CNPJ nao cadastrado":
                print(d)    
            else:
                nnom = input("Nome: ")
                nend = input("Endereco: ")
                nbai = input("Bairro: ")
                ncid = input("Cidade: ")
                ncep = int(input("CEP: "))
                while len(str(ncep)) < 8 or len(str(ncep)) > 8:
                    ncep = int(input("Informe um valor de 8 digitos\nCEP: "))
                nest = input("Estado: ")
                ntel = int(input("Telefone (Digite 0, caso nao possua): "))
                if ntel == 0:
                    ntel = "Nao possui"
                ncel = int(input("Celular (Digite 0, caso nao possua): "))
                if ncel == 0:
                    ncel = "Nao possui"
                nfax = int(input("Fax (Digite 0, caso nao possua): "))
                if nfax == 0:
                    nfax = "Nao possui"
                nema = input("Email (Digite 0, caso nao possua):")
                if nema == str('0'):
                    nema = "Nao possui"
                
                lis[d][1] = nnom  
                lis[d][2] = nend
                lis[d][3] = nbai
                lis[d][4] = ncid
                lis[d][5] = str(ncep)
                lis[d][6] = nest
                lis[d][7] = str(ntel)
                lis[d][8] = str(ncel)
                lis[d][9] = str(nfax)
                lis[d][10] = nema
                
        return lis
            
    def SalvarDadosEditados(self,lis):
        arq = open('Fornecedores.txt','w')
        lista = lis
        for x in lista:
            p = '{/'.join(x)
            arq.write(p)
        arq.close()
            
    def ChamadaMenuFornecedores(self):
        print("\nMENU DE FORNECEDORES\n\n1 - Adicionar\n2 - Consultar\n3 - Editar\n4 - Remover\n")
        user = int(input("Escolha sua opcao: "))
    
        if user == 1:
            Fornecedores.AdicionarFornecedores(self)
            Fornecedores.ChamadaMenuFornecedores(self)
        elif user == 2:
            CNPJ = input("Informe o CNPJ que deseja consultar: ")
            resultado = Fornecedores.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum fornecedores, adicione um fornecedor no menu de fornecedores")
                Fornecedores.ChamadaMenuFornecedores(self)
            else:
                print(Fornecedores.ConsultarFornecedores(self,CNPJ, Fornecedores.DadosFornecedores(self)))
                Fornecedores.ChamadaMenuFornecedores(self)
        elif user == 3:
            CNPJeditar = input("Informe o CNPJ que deseja editar: ")
            resultado = Fornecedores.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum fornecedores, adicione um fornecedor no menu de fornecedores")
                Fornecedores.ChamadaMenuFornecedores(self)
            else:
                decisao = Fornecedores.EditarRemoverFornecedores(self,'editar',Fornecedores.CNPJ_Editar_Remover(self,CNPJeditar,Fornecedores.DadosFornecedores(self)),Fornecedores.DadosFornecedores(self))
                Fornecedores.SalvarDadosEditados(self,decisao)
                Fornecedores.ChamadaMenuFornecedores(self)
        elif user == 4:
            user = input("Informe qual CNPJ deseja remover: ")
            resultado = Fornecedores.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum fornecedores, adicione um fornecedor no menu de fornecedores")
                Fornecedores.ChamadaMenuFornecedores(self)
            else:
                decisao2 = Fornecedores.EditarRemoverFornecedores(self,'remover',Fornecedores.CNPJ_Editar_Remover(self,user,Fornecedores.DadosFornecedores(self)),Fornecedores.DadosFornecedores(self))
                Fornecedores.SalvarDadosEditados(self,decisao2)
                Fornecedores.ChamadaMenuFornecedores(self)
        else:
            print("\nOPCAO INVALIDA\n")
            Fornecedores.ChamadaMenuFornecedores(self)