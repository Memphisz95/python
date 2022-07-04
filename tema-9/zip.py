cursos = ['java', 'python', 'php']
asistentes = [20, 34, 10]

demo = zip(cursos, asistentes)
print(list(demo))

#ALL(and) y ANY(or)
list1 = [1 == 1, 2 == 2, 3 == 4]
res = all(list1)
print(res)

print(min(2,3,1,4,5))
print(pow(3, 2))

a = input('Tu nombre?')
print(f'Hola, {a}')