class Usuario:
    def __init__(self,email=' ', senha='', nome="joao", idade=18, profissao="Desempregado"):

        self.senha = senha
        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao
        self.amigos = []
        self.conversas = []
        self.postagens_usuario=[]
        self.postagens_diversas=[]

    def __str__(self):
        return ("Nome: " + self.nome + "\nIdade: " + str(self.idade) + "\nEmail: " + self.email + "\nProfissão: " + self.profissao)

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_email(self):
        return self.email

    def get_profissao(self):
        return self.profissao

    def get_amigos(self):
        return self.amigos

    def get_conversas(self):
        return self.conversas

    def get_postagens(self):
        return self.postagens_usuario

    def set_senha(self, novo_senha):
        self.senha = novo_senha

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_idade(self, novo_idade):
        self.idade = novo_idade

    def set_email(self, novo_email):
        self.email = novo_email

    def set_profissao(self, novo_profissao):
        self.profissao = novo_profissao

    def adicionar_amigo(self, amigo):
        self.amigos.append(amigo)

    def remover_amigo(self, amigo):
        self.amigos.remove(amigo)

    def listar_amigos(self):
        for amigo in self.amigos:
            print(amigo)

    def listar_conversas(self):
        for conversa in self.conversas:
            print("Codigo da conversa: " + conversa.codigo)
            print("Participantes: ")
            print(conversa.remetente.nome)
            print(conversa.destinatario.nome)
            print(" ")

    def listar_conversas_grupo(self):
        for conversa in self.conversas:
            print("Codigo da conversa: " + conversa.codigo)
            print("Participantes: ")
            print(conversa.remetente.nome)
            for destinatario in conversa.destinatario:
                print(destinatario.nome)
            print(" ")


    def listar_postagens_usuario(self):
        for postagem in self.postagens_usuario:
            print(str(postagem))
            print("  ")

    def listar_postagens_diversas(self):
        for postagem in self.postagens_diversas:
            print(str(postagem))
            print("  ")