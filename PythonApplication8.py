from sign import DSignature
from elipt import ECurve





#main
LHS=[[]]
RHS=[[]]
LHS.append([])
RHS.append([])
p=999
a=0
b=0
print("Цифровая подпись по ГОСТ Р34.10-2001\n\nОбщая форма эллиптической кривой:\t y^2=(x^3  + a*x + b)mod p\n")
while (4*a*a*a+27*b*b)%p==0:
    print("Введите 'p': ")
    p=int(input())
    print("Введите 'a': ")
    a=int(input())
    print("Введите 'b': ")
    b=int(input())
    if (4*a*a*a+27*b*b)%p==0:
        print("не выполняется условие (4*a^3+27*b^2)%p!=0, попробуйте ввести другие значения")

#Polynomial
DSignature.polynomial(LHS,RHS,a,b,p)

#Создание базовых точек
count,points=DSignature.points_generate(LHS,RHS,a,b,p)
    
#Печать сгенерированных точек
print("Сгенерированные точки:")
for i in range(0,count):
    print(i+1," (",points[i].x,",",points[i].y,")\n")
q=p
ji=0
while q==p:
    G=points[ji]
    #Расчет базовой точки
    q=DSignature.find_q(G,a,b,p)
    ji+=1

print("Базовая точка взята равной:\t(",G.x,",",G.y,")\n")
test_sign = DSignature(p, a, b, q, G.x, G.y)
xa,YA=test_sign.gen_keys()
print("Сгенерированная пара ключей(закрытый,открытый)",xa,",","(",YA.x,",",YA.y,")")
menu=-1
while menu!=0:
    print("Выберите пункт меню:\n1)Подписать\n2)Проверить подпись\n0)Выход")
    menu=int(input())
    if menu==1:
        print("Введите сообщение: ")
        message = int(input())
        r,s = test_sign.sign(message, xa)
        print ("в итоге подписанное сообщение имеет вид: (", message, "; ", r, ", ",s,")");
    if menu==2:
        print("Введите сообщение: ")
        message = int(input())
        print("Введите первое число подписи (r)")
        r = int(input())
        print("Введите второе число подписи (s)")
        s = int(input())
        if test_sign.verify(message, (r,s), YA):
            print("подпись верна")
        else:
            print("подпись неверна")