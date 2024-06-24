from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

layout = """
    <h1> Proyecto Web (LP3 - 2024) | Andres Sanchez </h1>
    <hr/>
    <ul>
        <li>
            <a href="/index"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
         <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
         <li>
            <a href="/rango2"> Digitar Números [a,b]</a>
        </li>
    </ul>
    <hr/>
"""



def index(request):

    return render(request,'index.html')
def saludo(request):
   
    return render(request,'saludo.html')

def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """   
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout+ resultado)

def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
"""
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)


