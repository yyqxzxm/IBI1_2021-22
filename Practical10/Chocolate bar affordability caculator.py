#input the variables
total_money = int(input('please input the total money:' ))
cho_price = int(input('please input the chocolate price:' ))
#define a function to determine how many chocolate bars the user can buy and the remaining change
def affordabilitychcolate (total_money,cho_price):
    bar = int(total_money/cho_price)
    remain = total_money - bar*cho_price
    print("The user can afford %d bars of chocolate"%bar,'and remain %d yuan'%remain)
    return
#run the function
affordabilitychcolate(total_money,cho_price)
#example: The user has 100 yuan and a piece of chocolates cost 7 yuan
#the output result is "The user can afford 14 bars of chocolates and remain 2 yuan.
