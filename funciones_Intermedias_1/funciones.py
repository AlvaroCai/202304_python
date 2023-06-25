x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print(estudiantes)

x[1][0] = 15
print(x) 

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes) 

directorio_deportes ['futbol'][0] = 'andres'
print (directorio_deportes)

z[0]['y'] = 30 
print(z)


def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key, value in dictionary.items():
            output += f"{key} - {value}, "
        print(output[:-2])


students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

# Ejemplo de uso
estudiantes = [
    {'nombre': 'Michael', 'apellido': 'Jordan'},
    {'nombre': 'John', 'apellido': 'Rosales'},
    {'nombre': 'Mark', 'apellido': 'Guillen'},
    {'nombre': 'KB', 'apellido': 'Tonel'}
]

iterateDictionary2('nombre', estudiantes)
iterateDictionary2('apellido',estudiantes)



