class Math:
    @staticmethod
    def suma( num1, num2 ):
        return num1 + num2

    @staticmethod
    def resta( num1, num2 ):
        return num1 - num2
    
    @staticmethod
    def divide( num1, num2 ):
        return int(num1 / num2)
    
    @staticmethod
    def multiplica( num1, num2 ):
        return num1 * num2

res1 = Math.suma( 20, 30 )
res2 = Math.resta( 100, 15 )
res3 = Math.divide( 120, 4 )
res4 = Math.multiplica( 20, 10 )

print( f"Suma: {res1}" )
print( f"Resta: {res2}" )
print( f"Divide: {res3}" )
print( f"Multiplica: {res4}" )

