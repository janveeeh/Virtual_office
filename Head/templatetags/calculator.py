from msilib.schema import Error
from django import template
# import math
ERROR_MESSAGE = "Cast string to float Exception ... !"
register = template.Library()



def discount(value,args):
    try:
        first_number = float(value)#marked_price
        second_number = float(args)#selling_price
        ans = (first_number-second_number)/first_number * 100
        formatted_ans = "{:.2f}".format(ans)
        return formatted_ans
    except:
        raise ValueError(ERROR_MESSAGE)

# def Minuse(value,args):
#     try:
#         first_number = float(value)
#         second_number = float(args)
#         answer = first_number - second_number
#         return answer
#     except:
#         raise ValueError(ERROR_MESSAGE)
# def Multiple(value,args):
#     try:
#         first_number = float(value)
#         second_number = float(args)
#         answer = first_number * second_number
#         return answer
#     except:
#         raise ValueError(ERROR_MESSAGE)  
# def Divide(value,args):
#     try:
#         first_number = float(value)
#         second_number = float(args)
#         answer = first_number / second_number
#         return answer
#     except:
#         raise ValueError(ERROR_MESSAGE)  



register.filter("dis",discount)
# register.filter("min",Minuse)
# register.filter("mul",Multiple)
# register.filter("div",Divide)
# register.filter("pow",Power)
# register.filter("sqrt",Sqrt)
# register.filter("sin",SinAngle)
# register.filter("cos",CosAngle)
# register.filter("tan",TanAngle)