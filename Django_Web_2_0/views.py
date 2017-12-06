from django.http import HttpResponse
def here(request):
    return HttpResponse('Mom! I am here !')
def add(request,a,b):
    s = int(a) + int(b)
    return HttpResponse(str(s))
def math(request,a,b):
    a = int(a)
    b = int(b)
    s = a+b
    d = a-b
    p = a*b
    q = a//b
    html = '<html>' \
           'sum={s}<br>' \
           'dif={d}<br>' \
           'pro={p}<br>' \
           'quo={q}<br>' \
           '</html>'.format(s=s,d=d,p=p,q=q)
    return HttpResponse(html)