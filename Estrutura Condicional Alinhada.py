conta_normal = True
conta_universitária = False

saldo = 2000
saque = 1000
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo - cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficiente")
elif conta_universitária:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
else:
    print("Sistema nao reconhece esse tipo de conta. Entre em contato com o seu gerente!")