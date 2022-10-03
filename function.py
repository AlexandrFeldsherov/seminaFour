from random import randint

def input_int_numbers() -> int:
    """
    Ввод и проверка целого числа
    """
    index = True
    while index:
        try:
            number = int(input("Введите целое число : "))
            index = False
        except ValueError:
            print("Это не целое число.")
    return number

def SumNumberInputInt(num):
    sumNumber = 0
    num = str(num)
    for i in num:
        if i != '.' and i != '-' and i != ',':
            sumNumber = sumNumber + int(i)
    return sumNumber

def Factorial(number):
    if number > 1:
        number = number*Factorial(number-1)
    return number

def ReversNumber(num):
    num = str(num)
    listNum = []
    for i in num:
        listNum.append(i)
    revListNum = listNum
    revListNum.reverse()
    return int(''.join(map(str, revListNum)))

def RandomNumberInt(a,x):

    randDelta=x-a
    count=0
    while randDelta>1:
        randDelta=randDelta/10
        count=count+1
    randArray=[]
    i=0
    while i<count:
        j=10000
        while j>0:
                j=j-1
                numberRandom=RND()
        randArray.append(numberRandom)
        i=i+1  
    rand = int(''.join(map(str, randArray)))
    rand=float(rand/(10**count))
    rand=int((x-a)*rand)
    return a+rand


def сreating_list_int() -> list:
    """
    Создает список INT случайных чисел с запросом размера
    Есть проверка ввода размера
    """

    size = (input("Введите размер списка: "))
    size = int(input_int_numbers(size))
    numbers = []
    for i in range(size):
        numbers.append(randint(1, 10))
    return numbers

