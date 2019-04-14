class Clientes:
    def __init__(self):
        Clientes
        
    def DadosClientes(self):
        arq = open('Clientes.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        arq.close()
        return lis

    def ArquivoVazioouNao(self):
        criar = open('Clientes.txt','a')
        criar.close()
        arq = open('Clientes.txt','r')
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

    def CPF_CadastradoOuNao(self,UserCPF):
        arq = open('Clientes.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if str(UserCPF) != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    resposta = "not"
                    return resposta
            else:
                resposta ="yes"
                return resposta
        arq.close()

    def AdicionarCliente(self):
        cpf = int(input("CPF: "))
        if len(str(cpf)) < 11:
            cpf = (str(0)) * (11 - (len(str(cpf)))) + str(cpf)
        ListaVazia = Clientes.ArquivoVazioouNao(self)
        if ListaVazia == 0 or ListaVazia == 1:
            arq = open('Clientes.txt','a')
            decisao = Clientes.CPF_CadastradoOuNao(self,cpf)
            if decisao == 'yes':
                print("CPF cadastrado, favor escolher uma nova opcao no Menu\n")
                Clientes.ChamadaMenuClientes(self)
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
                if ema == str('0'):
                    ema = 'Nao possui'
                rg  = int(input("RG: "))
                nas = input("Data de nascimento:  ")
    
                arq.write(str(cpf) + '{/' + nom + '{/' + end + '{/' + bai + '{/' + cid + '{/' + str(cep) + '{/' + est + '{/' + str(tel) + '{/' + str(cel) + '{/' + str(fax) + '{/' + ema + '{/' + str(rg) + '{/' + nas + '\n')
    
            arq.close()

    def CPF_Editar_Remover(self,CPFUser,lis):
        limite = 0
        for p in range(len(lis)):
            if CPFUser != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    d = "CPF nao cadastrado"
                    return d
            else:
                d = p
                return d

    def ConsultarCliente(self,CPFConsulta,lis):
        limite = 0
        for p in range(len(lis)):
            if CPFConsulta != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    return("CPF nao cadastrado")
            if CPFConsulta == lis[p][0]:
                d = p
                return("\nCPF: %s\nNome: %s\nEndereco: %s\nBairro: %s\nCidade: %s\nCEP: %s\nEstado: %s\nTelefone: %s\nCelular: %s\nFax: %s\nEmail: %s\nRG: %s\nData de Nascimento: %s  " % (lis[d][0],lis[d][1],lis[d][2],lis[d][3],lis[d][4],lis[d][5],lis[d][6],lis[d][7],lis[d][8],lis[d][9],lis[d][10],lis[d][11],lis[d][12]))

    def EditarRemoverClientes(self,decisao,d,lis):
        criar = open('Clientes.txt','a')
        criar.close
        if decisao.lower() == "remover":
            if d == "CPF nao cadastrado":
                print(d)
            else:
                del lis[d]
    
        elif decisao.lower() == 'editar':
            if d == "CPF nao cadastrado":
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
        arq = open('Clientes.txt','w')
        lista = lis
        for x in lista:
            p = '{/'.join(x)
            arq.write(p)
        arq.close()
        
    def ChamadaMenuClientes(self):
        print("\nMENU DE CLIENTES\n\n1 - Adicionar\n2 - Consultar\n3 - Editar\n4 - Remover\n")
        user = int(input("Escolha sua opcao: "))

        if user == 1:
            Clientes.AdicionarCliente(self)
            Clientes.ChamadaMenuClientes(self)
        elif user == 2:
            CPF = input("Informe o CPF que deseja consultar: ")
            resultado = Clientes.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum cliente, adicione um cliente no menu de clientes")
                Clientes.ChamadaMenuClientes(self)
            else:
                print(Clientes.ConsultarCliente(self,CPF, Clientes.DadosClientes(self)),'\n')
                Clientes.ChamadaMenuClientes(self)
        elif user == 3:
            CPFeditar = input("Informe o CPF que deseja editar: ")
            resultado = Clientes.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum cliente, adicione um cliente no menu de clientes")
                Clientes.ChamadaMenuClientes(self)
            else:
                decisao = Clientes.EditarRemoverClientes(self,'editar',Clientes.CPF_Editar_Remover(self,CPFeditar,Clientes.DadosClientes(self)),Clientes.DadosClientes(self))
                Clientes.SalvarDadosEditados(self,decisao)
                Clientes.ChamadaMenuClientes(self)
        elif user == 4:
            user = input("Informe qual CPF deseja remover: ")
            resultado = Clientes.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum cliente, adicione um cliente no menu de clientes")
                Clientes.ChamadaMenuClientes(self)
            else:
                decisao2 = Clientes.EditarRemoverClientes(self,'remover',Clientes.CPF_Editar_Remover(self,user,Clientes.DadosClientes(self)),Clientes.DadosClientes(self))
                Clientes.SalvarDadosEditados(self,decisao2)
                Clientes.ChamadaMenuClientes(self)
        else:
            print("\nOPCAO INVALIDA\n")
            Clientes.ChamadaMenuClientes(self)

    #Clientes.ChamadaMenuClientes()
   
cl = Clientes()
cl.ChamadaMenuClientes()