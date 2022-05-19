from http.client import INSUFFICIENT_STORAGE


texto = input("Digite um texto ou palavra:")
caracteres = 0

for char in texto:
    caracteres = caracteres + 1
print("Este texto tem: ",caracteres,"caracteres.")    