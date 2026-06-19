'''This is a Function to Generate multiplication table'''
def Multiplication_Table(start_num,end_num=12):
    for i in range(1,end_num+1):
        x="{} X {} = {}"
        x=x.format(start_num,i,start_num*i)
        print(x)

Multiplication_Table(8)