class Funcionarios:
    
    def __init__(self):
        pass
    
    def DadosFuncionarios(self):
        arq = open('Funcionarios.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        arq.close()
        return lis
    
    def ArquivoVazioouNao(self):
        criar = open('Funcionarios.txt','a')
        criar.close()
        arq = open('Funcionarios.txt','r')
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
    
    def Matricula_CadastradoOuNao(self,UserMat):
        arq = open('Funcionarios.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if str(UserMat) != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    resposta = "not"
                    return resposta
            else:
                resposta ="yes"
                return resposta
        arq.close()
    
    def AdicionarFuncionarios(self):
        mat = int(input("Matricula (Numero com 6 digitos): "))
        while len(str(mat)) < 6 or len(str(mat)) > 6:
            mat = int(input("Informe um valor de 6 digitos\nMatricula: "))
        ListaVazia = Funcionarios.ArquivoVazioouNao(self)
        if ListaVazia == 0 or ListaVazia == 1:
            arq = open('Funcionarios.txt','a')
            decisao = Funcionarios.Matricula_CadastradoOuNao(self,mat)
            if decisao == 'yes':
                print("Matricula cadastrada, favor escolher uma nova opcao no Menu\n")
                Funcionarios.ChamadaMenuFuncionarios(self)
            else:
                nom = input("Nome: ")
                sen = input("Senha para login: ")
                car = input("Cargo: ")
                nas = input("Data de nascimento: ")
                sex = input("Sexo: ")
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
        
                arq.write(str(mat) + '{/' + nom + '{/' + sen + '{/' + car + '{/' + nas + '{/' + sex + '{/' + end + '{/' + bai + '{/' + cid + '{/' + str(cep) + '{/' + est + '{/' + str(tel) + '{/' + str(cel) + '\n')
      
            arq.close()
    
    def MAT_Editar_Remover(self,MATUser,lis):
        limite = 0
        for p in range(len(lis)):
            if MATUser != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    d = "Matricula nao cadastrada"
                    return d
            else:
                d = p
                return d
    
    def ConsultarFuncionarios(self,MatConsulta,lis):
        limite = 0
        for p in range(len(lis)):
            if MatConsulta != lis[p][0]:
                limite += 1 
                if limite == len(lis):
                    return("Matricula nao cadastrada")
            if MatConsulta == lis[p][0]:
                d = p
                return("\nMatricula: %s\nNome: %s\nCargo: %s\nData de nascimento: %s\nSexo: %s\nEndereco: %s\nBairro: %s\nCidade: %s\nCEP: %s\nEstado: %s\nTelefone: %s\nCelular: %s " % (lis[d][0],lis[d][1],lis[d][3],lis[d][4],lis[d][5],lis[d][6],lis[d][7],lis[d][8],lis[d][9],lis[d][10],lis[d][11],lis[d][12]))
    
    def EditarRemoverFuncionarios(self,decisao,d,lis):
        criar = open('Funcionarios.txt','a')
        criar.close
        if decisao.lower() == "remover":
            if d == "Matricula nao cadastrada":
                print(d)
            else:
                del lis[d]
        
        elif decisao.lower() == 'editar':
            if d == "Matricula nao cadastrada":
                print(d)    
            else:
                nnom = input("Nome: ")
                ncar = input("Cargo: ")
                nnas = input("Data de nascimento: ")
                nsex = input("Sexo: ")
                nend = input("Endereco: ")
                nbai = input("Bairro: ")
                ncid = input("Cidade:")
                ncep = input('CEP: ')
                while len(str(ncep)) < 8 or len(str(ncep)) > 8:
                    ncep = int(input("Informe um valor de 8 digitos\nCEP: "))
                nest = input("Estado: ")
                ntel = int(input("Telefone (Digite 0, caso nao possua): "))
                if ntel == 0:
                    ntel = "Nao possui"
                ncel = int(input("Celular (Digite 0, caso nao possua): "))
                if ncel == 0:
                    ncel = "Nao possui"
                
                lis[d][1] = nnom  
                lis[d][3] = ncar
                lis[d][4] = nnas
                lis[d][5] = nsex
                lis[d][6] = nend
                lis[d][7] = nbai
                lis[d][8] = ncid
                lis[d][9] = ncep
                lis[d][10] = nest
                lis[d][11] = str(ntel)
                lis[d][12] = str(ncel)
                
        return lis
            
    def SalvarDadosEditados(self,lis):
        arq = open('Funcionarios.txt','w')
        lista = lis
        for x in lista:
            p = '{/'.join(x)
            arq.write(p)
        arq.close()
            
    def ChamadaMenuFuncionarios(self):
        print("\nMENU DE FUNCIONARIOS\n\n1 - Adicionar\n2 - Consultar\n3 - Editar\n4 - Remover\n")
        user = int(input("Escolha sua opcao: "))
    
        if user == 1:
            Funcionarios.AdicionarFuncionarios(self)
            Funcionarios.ChamadaMenuFuncionarios(self)
        elif user == 2:
            MAT = input("Informe o Matricula que deseja consultar: ")
            resultado = Funcionarios.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum funcionario, adicione um funcionario no menu de funcionarios")
                Funcionarios.ChamadaMenuFuncionarios(self)
            else:
                print(Funcionarios.ConsultarFuncionarios(self,MAT, Funcionarios.DadosFuncionarios(self)))
                Funcionarios.ChamadaMenuFuncionarios(self)
        elif user == 3:
            Mateditar = input("Informe o matricula que deseja editar: ")
            resultado = Funcionarios.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum fornecedores, adicione um fornecedor no menu de fornecedores")
                Funcionarios.ChamadaMenuFuncionarios(self)
            else:
                decisao = Funcionarios.EditarRemoverFuncionarios(self,'editar',Funcionarios.MAT_Editar_Remover(self,Mateditar,Funcionarios.DadosFuncionarios(self)),Funcionarios.DadosFuncionarios(self))
                Funcionarios.SalvarDadosEditados(self,decisao)
                Funcionarios.ChamadaMenuFuncionarios(self)
        elif user == 4:
            user = input("Informe qual MATRICULA deseja remover: ")
            resultado = Funcionarios.ArquivoVazioouNao(self)
            if resultado == 0:
                print("Nao existem dados de nenhum funcionarios, adicione um funcionario no menu de funcionarios")
                Funcionarios.ChamadaMenuFuncionarios(self)
            else:
                decisao = Funcionarios.EditarRemoverFuncionarios(self,'remover',Funcionarios.MAT_Editar_Remover(self,user,Funcionarios.DadosFuncionarios(self)),Funcionarios.DadosFuncionarios(self))
                Funcionarios.SalvarDadosEditados(self,decisao)
                Funcionarios.ChamadaMenuFuncionarios(self)
        else:
            print("\nOPCAO INVALIDA\n")
            Funcionarios.ChamadaMenuFuncionarios(self)