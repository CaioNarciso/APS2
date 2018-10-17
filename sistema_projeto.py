from usuario import Usuario
from conversa import Conversa
from url import URL
from mensagem import Mensagem
import webbrowser

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.feed = []
        self.conversas=[]
        self.urls=[]

    def cadastrar_usuario(self,email,senha,nome,idade,profissao):
        usuario=Usuario(email,senha,nome,idade,profissao)
        self.usuarios.append(usuario)

    def remover_usuario(self, email_usuario):
        usuario=self.buscar_usuario_email(email_usuario)
        self.usuarios.remove(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def cadastrar_url(self,nome,url):
        url=URL(url, nome)
        self.urls.append(url)

    def buscar_usuario_email(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return(usuario)

    def buscar_usuario_nome(self, nome):
        for usuario in self.usuarios:
            if usuario.nome == nome:
                return(usuario)

    def buscar_conversa(self, codigo):
        for conversa in self.conversas:
            if conversa.codigo == codigo:
                return(conversa)

    def buscar_url(self, nome):
        for url in self.urls:
            if url.nome == nome:
                return url

    def logar(self, email, senha):
        usuario=self.buscar_usuario_email(email)
        if usuario == None:
            print("Email Incorreto")
        elif senha != usuario.senha:
            print("Senha Incorreta")
        else:
            opcao2 = ''
            while opcao2 != 'x':
                opcao2 = self.menu_usuario(usuario)

    def listar_postagens_sistema(self):
        for postagem in self.feed:
            print(postagem)
            print('  ')

    def postagem_publica(self,usuario,texto,):
        postagem=Postagem(usuario, "todos",texto)
        self.feed.insert(0,postagem)
        usuario.postagens_usuario.insert(0,postagem)
        for usuario_sistema in self.usuarios:
            usuario_sistema.postagens_diversas.insert(0,postagem)

    def postagem_para_amigos(self,usuario,texto):
        postagem=Postagem(usuario, usuario.amigos, texto)
        for amigo in usuario.amigos:
            amigo.postagens_diversas.insert(0,postagem)
        usuario.postagens_usuario.insert(0, postagem)
        usuario.postagens_diversas.insert(0, postagem)

    def criar_nova_conversa(self,codigo,remetente,lista_destinatarios,texto):
        conversa=Conversa(codigo,remetente,lista_destinatarios)
        remetente.conversas.insert(0,conversa)
        for destinatario in lista_destinatarios:
            destinatario.conversas.insert(0, conversa)
        conversa.enviar_mensagem_grupo(remetente,lista_destinatarios,texto)
        self.conversas.append(conversa)

    def menu(self):
        print("  ")
        print("1 - Cadastrar Usuario")
        print("2 - Remover Usuario")
        print("3 - Listar Usuarios")
        print("4 - Listar Postagens")
        print("5 - Informações sobre determinado usuario")
        print("6 - Cadastrar site")
        print("7- Logar")
        print('x - Sair')
        print("  ")
        opcao=input("Digite a opção desejada: ")
        print("  ")

        if opcao == '1':
            email=str(input("Email: "))
            for usuario in self.usuarios:
                if usuario.email == email:
                    email=input("Email ja existente, por favor informe outro: ")
                else:
                    pass

            senha=str(input("Senha: "))
            nome=str(input("Nome: "))
            idade=input("Idade: ")
            profissao=str(input("Profissão: "))
            self.cadastrar_usuario(email,senha,nome,idade,profissao)

        elif opcao == '2':
            email_usuario=str(input("Email do Usuario: "))
            self.remover_usuario(email_usuario)

        elif opcao == '3':
             print("Usuarios: ")
             self.listar_usuarios()

        elif opcao == '4':
            print("Feed: ")
            self.listar_postagens_sistema()

        elif opcao == '5':
            usuario_info=input("Nome do usuario: ")
            print(self.buscar_usuario_nome(usuario_info))

        elif opcao == '6':
            nome = str(input("Nome do Site: "))
            link = str(input("Link: "))
            self.cadastrar_url(nome, link)

        elif opcao == '7':
            email = str(input("Email: "))
            senha = str(input("Senha: "))
            self.logar(email, senha)
        return opcao

    def menu_usuario(self, usuario):
        print("  ")
        print("1 - Editar Usuario")
        print("2 - Adicionar Amigo")
        print("3 - Remover Amigo")
        print("4 - Listar Amigos do Usuario")
        print("5 - Postagem Publica")
        print("6 - Mostrar Todas as Postagens Publicas do Sistema")
        print("7- Enviar Mensagem")
        print("8- Enviar Mensagem Para Grupo")
        print("9- Listar Conversas do Usuario")
        print("10- Listar Mensagens de determinada conversa")
        print("11- Abrir Site")
        print("x - Sair")
        print(" ")
        opcao = input("Digite a opção desejada: ")
        print("  ")

        if opcao == '1':
            print("1 - Alterar Nome")
            print("2 - Alterar Idade")
            print("3 - Alterar Email")
            print("4 - Alterar Senha")
            print("5 - Alterar Profissão")
            print("  ")
            opcao3 = input("Digite o número para qual atributo deseja alterar: ")
            print("  ")

            if opcao3 == '1':
                novo=input("Digite o novo nome: ")
                usuario.set_nome(novo)

            elif opcao3 == '2':
                novo=input("Digite a nova Idade: ")
                usuario.set_idade(novo)

            elif opcao3 == '3':
                novo=input("Digite o novo email: ")
                usuario.set_email(novo)

            elif opcao3 == '4':
                novo = input("Digite a nova Senha: ")
                usuario.set_senha(novo)

            elif opcao3 == '5':
                novo=input("Digite a nova profissão: ")
                usuario.set_profissao(novo)

        elif opcao == '2':
            nome_amigo=input("Digite o nome do usuario: ")
            usuario.adicionar_amigo(self.buscar_usuario_nome(nome_amigo))

        elif opcao == '3':
            nome_amigo = input("Digite o nome do amigo: ")
            usuario.remover_amigo(self.buscar_usuario_nome(nome_amigo))

        elif opcao == '4':
            usuario.listar_amigos()

        elif opcao == '5':
            texto = str(input("Texto: "))
            self.postagem_publica(usuario, texto)

        elif opcao == '6':
            print("Postagens publicas")
            self.listar_postagens_sistema()


        elif opcao == "7" or opcao == '8':
            codigo = str(input("Digite o código da conversa: "))
            conversa = self.buscar_conversa(codigo)
            if conversa != None:
                texto = str(input("Texto: "))
                conversa.enviar_mensagem(usuario, conversa.destinatario, texto)

            else:
                print("Conversa ainda nao existente")
                nomes_destinatarios = input("Nome do destinatario: ").split()
                texto = str(input("Texto: "))
                lista_destinatarios = []
                for destinatario in nomes_destinatarios:
                    if self.buscar_usuario_nome(destinatario) == None:
                        print("Usuario", destinatario, " não existente")
                    else:
                        lista_destinatarios.append(self.buscar_usuario_nome(destinatario))
                    self.criar_nova_conversa(codigo, usuario, lista_destinatarios, texto)

        elif opcao == '9':
            usuario.listar_conversas_grupo()

        elif opcao == '10':
            codigo=str(input("Codigo da conversa: "))
            conversa=self.buscar_conversa(codigo)
            if conversa != None:
                conversa.listar_mensagens()
            else:
                print("Conversa não existente")

        elif opcao == '11':
            nome=str(input("Nome do site: "))
            site=self.buscar_url(nome)
            if site != None:
                webbrowser.open(site.url, new=0, autoraise=True)
            else:
                print("Site não cadastrado")
                nome=str(input("Nome do Site: "))
                link=str(input("Link: "))
                self.cadastrar_url(nome,link)
                site=self.buscar_url(nome)
                webbrowser.open(site.url, new=0, autoraise=True)
        return opcao