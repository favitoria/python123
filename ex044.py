from time import sleep
PN = float(input('Digite o valor deste produto: R$'))
CP = int(input('Qual a condição de pagamento escolhida? \n\033[1;35;40m[1] À VISTA (10% de desconto)\033[0;0;0m\n\033[1;35;40m[2] À VISTA NO CARTÃO (5% de desconto)\033[0;0;0m\n\033[1;35;40m[3] EM 2X NO CARTÃO (0% de desconto)\033[0;0;0m\n\033[1;35;40m[4] EM 3X OU MAIS NO CARTÃO (20% de juros)\033[0;0;0m\nOPÇÃO: '))
print('\033[1;35;40mPROCESSANDO...\033[0;0;0m')
sleep(2)
if CP == 1:
    V = PN - (PN * (10/100))
    print('OPÇÃO 1 ESCOLHIDA COM SUCESSO!\nDe R${:.2f} você pagará: \033[0;31;40mR${:.2f}\033[0;0;0m'.format(PN, V))
elif CP == 2:
    V = PN - (PN * (5/100))
    print('OPÇÃO 2 ESCOLHIDA COM SUCESSO!\nDe R${:.2f} você pagará: \033[0;31;40mR${:.2f}\033[0;0;0m'.format(PN, V))
elif CP == 3:
    T = PN / 2
    print('OPÇÃO 3 ESCOLHIDA COM SUCESSO!\nSerão 2x de R${:.2f}\nVocê pagará: \033[0;31;40mR${:.2f}\033[0;0;0m'.format(T, PN))
elif CP == 4:
    P = int(input('Quantas parcelas? '))
    print('\033[1;35;40mPROCESSANDO...\033[0;0;0m')
    sleep(1)
    V = PN + (PN * (20/100))
    T = V / P
    print('OPÇÃO 4 ESCOLHIDA COM SUCESSO!\nSerão {}x de {:.2f}R$\nCom os juros, o valor de R${:.2f} ficara ao todo: \033[0;31;40mR${:.2f}\033[0;0;0m'.format(P, T, PN, V))
else:
    print('OPÇAO INVÁLIDA!')
