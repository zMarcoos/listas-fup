commitments = [
  { 
    'date': { 'day': 12, 'month': 'Julho', 'year': 2022 }, 
    'schedule': { 'hour': 9, 'minutes': 30, 'seconds': 0 }, 
    'description': 'Go to market'
  }
]

def register_commitment():
  schedule = { 
    'hour': int(input('Hour: ')), 
    'minutes': int(input('Minutes: ')), 
    'seconds': int(input('Seconds: ')) 
  }
  
  date = { 
    'day': int(input('Day: ')), 
    'month': input('Month: '), 
    'year': int(input('Year: '))
  }

  commitments.append({
    'date': date,
    'schedule': schedule,
    'description': input('Descrição: ')
  })

def list_commitments():
  for commitment in commitments:
    date = commitment['date']
    schedule = commitment['horario']

    formatted_date = f'{date["day"]} de {date["month"]} de {date["year"]}'
    formatted_schedule = f'{schedule["hour"]}:{schedule["minutes"]}:{schedule["seconds"]}'
    
    print(f'{formatted_date} - {formatted_schedule} - {commitment["description"]}')