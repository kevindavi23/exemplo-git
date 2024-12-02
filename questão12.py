#questão 12
hora= float(input("digite a quantida de horas trabalhadas por dia:"))
total= float(input("digite o total de horas:"))
salario= (hora*total)
if(salario<=900):
    inss= (8*salario)/100
    fgts= (11*salario)/100
    sl= salario-inss-fgts   
    print("valor do salario bruto:",salario)
    print("desconto inss:",inss)
    print("desconto fgts:",fgts)
    print("salario liquido:",sl)
elif(salario<=1500):
    ir= (5*salario)/100
    inss= (8*salario)/100
    fgts= (11*salario)/100
    sl= salario-ir-inss-fgts
    print("valor do salario bruto:",salario)
    print("desconto imposto de renda",ir)
    print("desconto inss:",inss)
    print("desconto fgts:",fgts)
    print("salario liquido:",sl)
elif(salario<=2500):
    ir= (10*salario)/100
    inss= (8*salario)/100
    fgts= (11*salario)/100
    sl= salario-ir-inss-fgts
    print("valor do salario bruto:",salario)
    print("desconto imposto de renda",ir)
    print("desconto inss:",inss)
    print("desconto fgts:",fgts)
    print("salario liquido:",sl)
elif(salario>2500):
    ir= (20*salario)/100
    inss= (8*salario)/100
    fgts= (11*salario)/100
    sl= salario-ir-inss-fgts
    print("valor do salario bruto:",salario)
    print("desconto imposto de renda",ir)
    print("desconto inss:",inss)
    print("desconto fgts:",fgts)
    print("salario liquido:",sl)    