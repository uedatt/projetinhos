import smtplib
import getpass

ep = input('digite o seu email:\n')

flag = True

lista = []

while flag == True:
    ed = input('digite um ou mais emails de pessoas para quem deseja enviar:\n')
    lista.append(ed)
    if ed == 'sair':
        lista.pop()
        flag = False


sen = getpass.getpass('Digite sua senha:\n')
men = input('digite a mensagem que deseja enviar:\n')

email_num = int(input('digite o numero de emails que deseja enviar para a pessoa com essa mesma mensagem:\n'))



valor_lista = len(lista)

contador = 0
cont = email_num * valor_lista
while contador < cont:
    for email in lista:
        print(email)
        email_de = ep
        smtp = 'smtp.gmail.com'

        senha = sen
        server = smtplib.SMTP(smtp, 587)

        server.starttls()
        server.login(email_de, senha)
        msg = men

        server.sendmail(email_de, email, msg)
        server.quit()

        contador +=1
        print('foram enviados', contador, 'emails')