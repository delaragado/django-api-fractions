from fractions import Fraction
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

jdata = open('operaciones/num.json').read()
data = json.loads(jdata)

@method_decorator(csrf_exempt)
def SumaFrac(request):
    if request.method == "GET":
        #return HttpResponse('hola mundo')
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        #return HttpResponse("respondiendo al post")
        #data = [{'num1': 5, 'den1': 3},{'num2': 8, 'den2': 7}]
        num1 = data['num1']
        den1 = data['den1']
        num2 = data['num2']
        den2 = data['den2']
        frac1 = Fraction(numerator=num1,denominator=den1)
        frac2 = Fraction(numerator=num2,denominator=den2)
        res = frac1 + frac2
        resstr = {"num":res.numerator, "den":res.denominator}
        return JsonResponse(resstr)

@method_decorator(csrf_exempt)
def RestaFrac(request):
    if request.method == "GET":
        #return HttpResponse('hola mundo')
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        #return HttpResponse("respondiendo al post")
        #data = [{'num1': 5, 'den1': 3},{'num2': 8, 'den2': 7}]
        num1 = data['num1']
        den1 = data['den1']
        num2 = data['num2']
        den2 = data['den2']
        frac1 = Fraction(numerator=num1,denominator=den1)
        frac2 = Fraction(numerator=num2,denominator=den2)
        res = frac1 - frac2
        resstr = {"num":res.numerator, "den":res.denominator}
        return JsonResponse(resstr)

@method_decorator(csrf_exempt)
def MultiFrac(request):
    if request.method == "GET":
        #return HttpResponse('hola mundo')
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        #return HttpResponse("respondiendo al post")
        #data = [{'num1': 5, 'den1': 3},{'num2': 8, 'den2': 7}]
        num1 = data['num1']
        den1 = data['den1']
        num2 = data['num2']
        den2 = data['den2']
        frac1 = Fraction(numerator=num1,denominator=den1)
        frac2 = Fraction(numerator=num2,denominator=den2)
        res = frac1 * frac2
        resstr = {"num":res.numerator, "den":res.denominator}
        return JsonResponse(resstr)

@method_decorator(csrf_exempt)
def DivFrac(request):
    if request.method == "GET":
        #return HttpResponse('hola mundo')
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        #return HttpResponse("respondiendo al post")
        #data = [{'num1': 5, 'den1': 3},{'num2': 8, 'den2': 7}]
        num1 = data['num1']
        den1 = data['den1']
        num2 = data['num2']
        den2 = data['den2']
        frac1 = Fraction(numerator=num1,denominator=den1)
        frac2 = Fraction(numerator=num2,denominator=den2)
        res = frac1 / frac2
        resstr = {"num":res.numerator, "den":res.denominator}
        return JsonResponse(resstr)