students = []

for index in range(5):
  print(f'--- Cadastrar {index + 1}° Aluno ---')
  
  student = { 
    'name': input('Nome: '), 
    'enrollment': int(input('Matrícula: ')), 
    'course': input('Curso: ')
  }
  
  students.append(student)

print('--- Lista de alunos ---')

for student in students:
  print(f'{student["name"]} - {student["enrollment"]} - {student["course"]}')
