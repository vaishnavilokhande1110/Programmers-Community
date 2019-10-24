#to convert binary to decimal
BinaryNo = int(input('Binary No= '))
rev = 0
decimal = 0
i = 0

if BinaryNo>2 or BinaryNo<0:
    print('This is not a binary no')

elif BinaryNo<=1:
    print('Decimal No= ',BinaryNo)

#reverse the no and multiply by power of 2 and to previous value
else:
    while BinaryNo>0:
        rev = BinaryNo % 10
        decimal = decimal + rev * pow(2,i)
        BinaryNo = BinaryNo // 10
        i = i + 1
    print('Decimal No= ',decimal)
