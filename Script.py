import os 
from time import sleep

#Usando um variável para deixar o script organizado e pequeno.
c = "clear"
os.system(c)

senha = str(input("\033[1;36mDigite a senha:\033[m "))
if senha == "wss":
    os.system(c)
    sleep(1)
    print ("\033[1;32mAcesso liberado :)\033[m")
    os.system(c)

else:
    os.system(c)
    sleep(1)
    print ("\033[1;31mAcesso negado :(\033[m")
    os.system(c)
    exit()

print ("\033[1;34mCarregando...\033[m")
sleep(2)
os.system("sl")
os.system(c)

while true:
    print ("▒▒▒▒▒▐▀▀▀█▄▒▒▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒▒▒█▀─────█▒▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒▒█────▄─▄─▌▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒▒▌───██─█▌▌▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒▒▌───█▌──▌▌▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒▒▌────────▌▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒█─────────▐▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▐▌─▐───────▐▄▄▒▒▒▒▒")
    sleep(0.1)
    print ("▒▐▌─▐────────▄▀▀█▒▒▒")
    sleep(0.1)
    print ("▒█──▀▄──▄█▄▀▀▒▒▒▌▀▄▒")
    sleep(0.1)
    print ("▐▌────██▀█░█▄▒▄▄█▀▀▌")
    sleep(0.1)
    print ("▐▌──▌▐───▐░░▐▀░░░░░▌")
    sleep(0.1)
    print ("▐▌──▌────▐░░▐░░░░░░▌")
    sleep(0.1)
    print ("▐───▌────▐░░▐░░░░░░▌")
    sleep(0.1)
    print ("▐───█────▐░░▐░░░░░░▌")
    sleep(0.1)
    print ("▐───█────▐░░▐░░░░░░▌")
    sleep(0.1)
    print ("▐───█─────▀█▐▄▄▄█▀▀▒")
    sleep(0.1)
    print ("▀▄▄─▐───────▄█▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒▒▀█───█▄▀▀▀▒▒▒▒▒▒▒")
    sleep(0.1)
    print ("▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒")
    sleep(0.1)

    print ("[\033[1;34m1\033[m] \033[1;33mAtualizar Termux\033[m")
    sleep(0.2)
    print ("[\033[1;34m2\033[m] \033[1;33mInstalar Git\033[m")
    sleep(0.2)
    print ("[\033[1;34m3\033[m] \033[1;33mInstalar Python3\033[m")
    sleep(0.2)
    print ("[\033[1;34m4\033[m] \033[1;33mInstalar Sqlmap\033[m")
    Print ("")
    print ("[\033[1;34m5\033[m] \033[1;31mSair\033[m")
    sleep(0.2)
    print ("")
    
    opcao = str(input("\033[1;32mDigite sua opção: "))
    pf opcao == "1":
        print ("")
        os.system("apt update && apt upgrade")
        os.system(c)

    elif opcao == "2":
        print ("")
        os.system("pkg install git")
        os.system(c)

    elif opcao == "3":
        print ("")
        os.system("pkg install python3")
        os.system(c)

    elif opcao == "4":
        print ("")
        os.system("git clone https://github.com/sqlmapproject/sqlmap")
        os.system(c)

    elif opcao == "5":
        print ("")
        os.system(c)
        break

    else:
        print ("")
        print ("\033[1;31mERRO! Opção não existe.\033[m")
        os.system(c)

