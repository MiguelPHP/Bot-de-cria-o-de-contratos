import docx

n2 = str(input("Digite seu nome: "))
n3 = str(input("Digite o RG com todos os '.': "))
n4 = str(input("Digite seu CPF com todos os '.': "))

n1 = (str('''
    pelo presente instrumento particular, de um lado, como LOCADORA,
Antónia Rosângela da Silva, brasileira, casada, nascida em 03/03/1965,
registrada sob RG MG 4688431 SSP / MG e CPF 697.168.206-82, residente
e domiciliada a Av. Geraldo Campos 347, Bandeirinhas, Betim / MG e,
de outro lado, como LOCATÁRIO, ''') + n2 + str(''' brasileiro,
nascido em 19/05/1999, registrado sob RG ''') + n3 + str(''' e CPF ''') + n4 + str(''' residente Rua Córsega 369, Arquipélago Verde de Betim / MG, resolvem celebrar
o presente contrato de locação, o qual deve reger-se pelas seguintes cláusulas e condições: '''))

document = docx.Document()


document.add_heading("Contrato de locação de imóvel residencial", level=1)

document.add_paragraph(n1)


document.save("test2.docx")
