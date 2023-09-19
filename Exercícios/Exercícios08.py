#Escreva um programa que leia um valor em metros e exiba em centimetros a milimetro  
m = float(input('Informe o valor em metros: '))
km = m /1000
hm = m /100
dam = m /10
dm = m *10
cm = m *100
mm = m *1000
print('Quilômetro: {}km. \nHectômetro: {}hm. \nDecâmetro: {}dam.'.format(km, hm, dam))
print('Metro: {}m. \nDecímetros: {}dm. \nCentímetros: {}cm. \nValor em milimetros: {}mm'.format(m, dm, cm, mm))