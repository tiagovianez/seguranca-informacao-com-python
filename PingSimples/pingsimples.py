#IMPORANTO O MÚDULO OU BIBLIOTECA OS (INTEGRANDO OS PROGRAMAS E RECURSOS DO S.O)
import os

print('#' * 60)
ip_ou_host = input('Digite o Ip ou Host a ser verificado: ')

#CRIANDO UMA VARIÁVEL QUE VAI RECEBER DO USUÁRIO UM IP
print('-' * 60)
os.system('ping -n 6 {}'.format(ip_ou_host))
print('-' * 60)