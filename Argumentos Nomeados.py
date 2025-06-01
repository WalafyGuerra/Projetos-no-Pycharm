def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com suceso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro('Hyundai', 'HB20', 2015, 'ABC-1234')
salvar_carro(marca='Hyundai', modelo='HB20', ano=2015, placa='ABC-1234')
salvar_carro(**{'marca': 'Hyundai', 'modelo': 'HB20', 'ano': 2015, 'placa': 'ABC-1234'})

# Carro inserido com sucesso! Hyundai/HB20/2015/ABC-1234