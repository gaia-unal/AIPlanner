
def create_file(name, data):
  new_file = open('strip/'+ name + '.txt', 'w')
  initial_state = data.get('initialState')
  final_state = data.get('finalState')
  actions = data.get('actions')

  new_file.write('Initial state: ')
  for i, item in enumerate(initial_state):
    new_file.write('{}({})'.format(item.get('name').capitalize(),item.get('value')))
    if len(initial_state) - 1 != i:
      new_file.write(', ')
  new_file.write('\n')
  
  new_file.write('Goal state: ')
  for i, item in enumerate(final_state):
    new_file.write('{}({})'.format(item.get('name').capitalize(),item.get('value')))
    if len(final_state) - 1 != i:
      new_file.write(', ')
  new_file.write('\n')

  new_file.write('\nActions: \n')
  for i, item in enumerate(actions):
    new_file.write('{}({})\n'.format(item.get('name').capitalize(),item.get('variables')))

    new_file.write('Preconditions: ')
    preconditions = item.get('preconditions')
    for j, element in enumerate(preconditions):
      if element.get('name')[0] == '!':
        new_file.write('{}({})'.format(element.get('name')[0]+element.get('name')[1:].capitalize(),element.get('value')))
      else:
        new_file.write('{}({})'.format(element.get('name').capitalize(),element.get('value')))
      if len(preconditions) - 1 != j:
        new_file.write(', ')
    new_file.write('\n')

    new_file.write('Postconditions: ')
    postconditions = item.get('postconditions')
    for k, element in enumerate(postconditions):
      if element.get('name')[0] == '!':
        new_file.write('{}({})'.format(element.get('name')[0]+element.get('name')[1:].capitalize(),element.get('value')))
      else:
        new_file.write('{}({})'.format(element.get('name').capitalize(),element.get('value')))
      if len(postconditions) - 1 != k:
        new_file.write(', ')
    new_file.write('\n')
    new_file.write('\n')
  
  new_file.close()