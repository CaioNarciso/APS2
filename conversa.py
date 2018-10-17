from mensagem import Mensagem

class Conversa:

    def __init__(self,codigo,usuario,destinatario):
        self.remetente=usuario
        self.destinatario=destinatario
        self.mensagens=[]
        self.codigo=codigo

    def enviar_mensagem(self, remetente, destinatario, texto):
        mensagem=Mensagem(remetente, destinatario, texto)
        self.mensagens.insert(0,mensagem)

    def enviar_mensagem_grupo(self,remetente, destinatario, texto):
        mensagem = Mensagem(remetente, destinatario, texto)
        self.mensagens.insert(0, mensagem)

    def listar_mensagens(self):
        print("Mensagens:")
        print("  ")
        for mensagem in self.mensagens:
            print(str(mensagem))
            print("  ")