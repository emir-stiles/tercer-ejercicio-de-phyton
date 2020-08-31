dato = int(input("ingrese un numero del 1 al 100 "))
a=[1,1,2,3,5,8,13,21,34,55,89]
print([cada_uno for cada_uno in a if cada_uno < dato])