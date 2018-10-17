class Postagem:
    def __init__(self,usuario, publico, texto=''):
        self.hora_data=horario_data()
        self.usuario=usuario
        self.texto=texto
        self.publico=publico
     def __str__(self):
        if self.texto != "":
            return("Usuario: " + str(self.usuario.nome) + "\n" + self.hora_data + "\n" + self.texto)
         elif self.texto != "":
            return ("Usuario: " + str(self.usuario.nome)+ "\n" + self.hora_data + "\n" + self.texto)
     def get_texto(self):
        return self.texto

     def get_publico(self):
        for usuario in self.publico:
            print(usuario)

     def set_texto(self,novo_texto):
        self.texto=novo_texto

     def set_publico(self,lista_usuarios):
        self.publico=lista_usuarios

def horario_data():
    from datetime import datetime
    now = datetime.now()
    hora = now.hour
    minutos = now.minute
    dia = now.day
    mes = now.month
    ano = now.year
    return ("Data: "+str(dia)+"/"+str(mes)+"/"+str(ano)+" \ Hora: "+str(hora)+":"+str(minutos))