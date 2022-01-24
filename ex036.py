from time import sleep
print('\033[1;34;40mResponda as perguntas caso queira um empréstimo para comprar sua nova casa!!\033[0;0;0m')
Vcasa = float(input('\033[1;31;40mQual o valor da casa que quer comprar? R$'))
Vsalario = float(input('\033[1;32;40mCerto! E qual é o teu salário? R$'))
Vanos = float(input('\033[1;36;40mPor último, em quantos anos pretende pagar? '))
Vmensal = Vcasa / (Vanos * 12)
print('\033[1;35;40mOK PROCESSANDO...\033[0;0;0m')
sleep(2)
if Vmensal <= Vsalario * (30/100):
    print('\033[4;32;40mMaravilha! Você PODE realizar um empréstimo bancário!\033[0;0;0m\n\033[4;32;40mSua prestação mensal é de {:.2f}R$!\033[0;0;0m'.format(Vmensal))
else:
    print('\033[1;31;40mInfelizmente, você NÃO PODE realizar um empréstimo bancário!\nSua prestação mensal excederia o valor de 30% de seu salário \nFicando em R${:.2f}\033[0;0;0m'.format(Vmensal))
print('\033[1;34;40mAGRADECEMOS PELA PREFERENCIA! VOLTE SEMPRE!!\033[0;0;0m')