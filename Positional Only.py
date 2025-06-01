def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)

criar_carro("HB20", 2015, "ABC-1234", marca="Hyundai", motor="1.0", combustível="Gasolina")   #válido
criar_carro("HB20", 2015, "ABC-1234", "Hyundai", "1.0", "Gasolina")   #inválido

