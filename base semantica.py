from pysentimiento import create_analyzer

#crio os analisadores
emoção = create_analyzer(task='emotion', lang='pt')
ironia = create_analyzer(task='irony', lang='pt')

print('fale')

frase = input('')#uma frase de exemplo

rsl_emoção = emoção.predict(frase)#aqui ele preve qual emoção é a da frase
rsl_ironia = ironia.predict(frase)#aqui ele analisa se é ironia ou não

print(rsl_ironia.output,  rsl_emoção.output)#colocando o '.output' eu vejo apenas o que a IA entende que é 

if rsl_ironia.output == 'ironic':#se for ironia só printa que é ironia
    print('é ironia')
elif rsl_emoção.output == 'anger' and rsl_ironia.output == 'not ironic':#se não for ironia e a emoção da frase for brava/raiva ele printa que pode conter palavrão
    print('pode conter palavrão')
