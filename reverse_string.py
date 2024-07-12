string = input()
letras = ""
for index in range(len(string)):
    letras += string[-index-1]
print (letras)