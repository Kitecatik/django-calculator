from django.shortcuts import render
from django.http import HttpResponse
def calculator(request):
    if request.method == 'POST':
        result = request.POST.get('result')
         
        num1 = float(request.POST.get('number1')) 
        num2 = float(request.POST.get('number2'))
        operation = request.POST.get('operation')
        
              
        return render(request, 'result.html', {'result': result, 'number1': num1, 'number2': num2, 'operation':operation })

    return render(request, 'index.html')

def result(request):
    if request.method == 'GET': 
        num1 = float(request.GET.get('number1')) 
        num2 = float(request.GET.get('number2'))
        operation = request.GET.get('operation')
    
        try:
            if operation == '+':
                result = num1 + num2
                return render(request,'result.html', {'result': result})
            elif operation == '-':
                result = num1 - num2
                return render(request,'result.html', {'result': result})
            elif operation == '*':
                result = num1 * num2
                return render(request,'result.html', {'result': result})
            elif operation == '/':
                result = num1 / num2
                return render(request,'result.html', {'result': result})
            elif operation == '**':
                result = num1 ** num2
                return render(request,'result.html', {'result': result})
            elif operation == '//':
                result = num1 // num2
                return render(request,'result.html', {'result': result})
            elif operation == '%':
                result = num1 % num2
                return render(request,'result.html', {'result': result})
            else:
                result = "Incorrect operation"
                return render(request, 'result.html', {'result': result})
        except ZeroDivisionError:
            result = "You can't divide by zero."
            return render(request, 'result.html', {'result': result})
        except OverflowError:
            result = "Result too large"
            return render(request, 'result.html', {'result': result})
        
