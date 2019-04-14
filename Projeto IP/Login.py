from Funcionarios import Funcionarios
from MenuOpcoes import MenuOpcoes
func = Funcionarios()
Mo = MenuOpcoes()

class Login:
    def __init__(self):
        pass
    
    def LoginConfere(self,Mat,Sen):
        arq = open('Funcionarios.txt','r')
        s = arq.readlines()
        lis = []
        for x in s:
            dados = x.split('{/')
            lis.append(dados)
        limite = 0
        for p in range(len(lis)):
            if Mat == lis[p][0] and Sen == lis[p][2]:
                resposta = 'yes'
                return resposta
            else:
                limite += 1 
                if limite == len(lis):
                    resposta = 'not'
                    return resposta
        arq.close()

    def AdicionarFuncionarios(self):
        mat = int(input("Matricula (Numero com 6 digitos): "))
        while len(str(mat)) < 6 or len(str(mat)) > 6:
            mat = int(input("Informe um valor de 6 digitos\nMatricula: "))
        ListaVazia = func.ArquivoVazioouNao()
        if ListaVazia == 0 or ListaVazia == 1:
            arq = open('Funcionarios.txt','a')
            decisao = func.Matricula_CadastradoOuNao(mat)
            if decisao == 'yes':
                print("Matricula cadastrada, favor escolher uma nova opcao no Menu\n")
                Login.ChamadaMenuLogin(self)
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
        
    def ChamadaMenuLogin(self):
        print('Login/Cadastro\n\n1 - Fazer Login\n2 - Fazer Cadastro\n')
        user = int(input("Escolha sua opcao: "))
        if user == 1:
            nom = input("\nLogin (matricula): ")
            sen = input("Senha (6 caracteres): ")
            Res = Login.LoginConfere(self,nom, sen)
            if Res == 'yes':
                print("Login Correto")
                Mo.MostrarMenu()
            else:
                print("Senha ou Login errados")
                Login.ChamadaMenuLogin(self)
        elif user == 2:    
            Login.AdicionarFuncionarios(self)
            Login.ChamadaMenuLogin(self)
        else:
            print("Opcao errada,escolha uma opcao no MENU de LOGIN/CADASTRO")
            Login.ChamadaMenuLogin(self)
l = Login()
l.ChamadaMenuLogin()