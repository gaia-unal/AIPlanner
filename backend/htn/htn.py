
def get_operators(operators, problem):
  for operator in problem['operators']:
    operators[operator['name']] = operator

def get_tasks(tasks, problem):
  for task in problem['tasks']:
    tasks.append((task['name'],task['value']))

def get_state(state, problem):
  for task in problem['initialState']:
    state.append((task['name'], task['value']))

def get_methods(methods, problem):
  for method in problem['methods']:
    methods[method['name']] = method

def take_tasks(method, variables):
  tasks = []
  for task in method['postconditions']:
    value = []
    for val in task['value']:
      value.append(variables[val])
    
    tasks.append(
      (task['name'], value)
    )
  
  return tasks

def get_variables(operator, task, state):
  variables = {}
  for i in range(len(operator['variables'])):
    variables[operator['variables'][i]] = task[1][i]
  
  for prec in operator['preconditions']:
    for task in state:

      if prec['name'] == task[0]:

        for i in range(len(prec['value'])):
          if prec['value'][i] not in variables:
            if task[1][i] not in variables.values():
              variables[prec['value'][i]] = task[1][i]
  
  return variables

def equal(prec, task, variables):
  cont = 0

  if prec['name'] == task[0]:
    for i in range(len(prec['value'])):
      if prec['value'][i] in variables:
        if variables[prec['value'][i]] != task[1][i]:
          return False
      else:
        cont += 1
        variables[prec['value'][i]] = task[1][i]
    
    if cont == len(prec['value']):
      return False

  else:
    return False
  
  return True

def state_del_add(state, operator, variables):
  new_state = state[:]

  # add task to add in the operator
  #print('\nadd -> ', operator['add'])
  for task in operator['add']:
    value = []
    for val in task['value']:
      value.append(variables[val])
    
    new_state.append(
      (task['name'], value)
    )
  
  # task to delete in the operator
  #print('\ndel -> ', operator['del'])
  for task in operator['del']:
    value = []
    for val in task['value']:
      value.append(variables[val])

    for task2 in new_state:
      if task['name'] == task2[0] and value == task2[1]:
        new_state.remove((task2[0], task2[1]))

  return new_state

def apply_operator(task, operator, state):
  variables = get_variables(operator, task, state)
  #print('\nvariables -> ', variables)
  cont = 0
  
  for prec in operator['preconditions']:
    for task in state:
      if equal(prec, task, variables):
        cont += 1
        break
    else:
      return None
  
  if cont != len(operator['preconditions']):
    return None

  new_state = state_del_add(state, operator, variables)
  return new_state

def apply_method(task, method, state):
  variables = get_variables(method, task, state)
  #print('\nvariables -> ', variables)
  cont = 0

  for prec in method['preconditions']:
    for task in state:
      if equal(prec, task, variables):
        cont += 1
        break
    else:
      return None
  
  if cont != len(method['preconditions']):
    return None

  new_tasks = take_tasks(method, variables)
  return new_tasks

def seek_plan(state, tasks, operators, methods, plan, debug=False):
  if tasks == []:
    return plan

  task1 = tasks[:1][0]
  if task1[0] in operators:
    operator = operators[task1[0]]

    if debug:
      print('\noperator to apply -> ', operator, '\ntask -> ', task1)
    
    new_state = apply_operator(task1, operator, state)
    
    if debug:
      print('\nstate -> ', new_state)
      print('\ntasks ->', tasks[1:])
    
    if new_state:
      return seek_plan(new_state, tasks[1:], operators, methods, plan + [task1], debug=debug)
  
  elif task1[0] in methods:
    method = methods[task1[0]]
    if debug:
      print('\nmethod to apply -> ', method)
    
    subtasks = apply_method(task1, method, state)
    if subtasks:
      if debug:
        print('\ntasks -> ', subtasks + tasks[1:])
        print('\nstate -> ', state)
      return seek_plan(state, subtasks + tasks[1:], operators, methods, plan, debug=debug)
  
  return False

def print_plan(plan):
  result = {}
  for i, task in enumerate(plan):
    value = ''
    for val in task[1]:
      value += val +', '
    
    value = value[: (len(value) - 2)]
    result['paso ' + str(i+1)] = task[0] + '(' + value + ')'
  
  return result

def run_htn(problem):
  state = []
  tasks = []
  operators = {}
  methods = {}

  get_state(state, problem)
  get_operators(operators, problem)
  get_tasks(tasks, problem)
  get_methods(methods, problem)

  """ print('\nstate -> ', state, '\n\nmethods -> ', methods, '\n\noperators -> ', operators, '\n\ntasks -> ', tasks) """

  plan = seek_plan(state, tasks, operators, methods, [])
  result = print_plan(plan)
  return result

if __name__ == "__main__":

  problem = {
    "name": "viajar",
    "initialState": [
      {
        "name": "estar",
        "value": ["Manizales"]
      },
      {
        "name": "aeropuerto",
        "value": ["Manizales", "La nubia"]
      },
      {
        "name": "aeropuerto",
        "value": ["Bogota", "El dorado"]
      }
    ],
    "tasks": [
      {
        "name": "viajarEnAvion",
        "value": ["Manizales", "Bogota"]
      }
    ],
    "methods" : [
      {
        "name" : "viajarEnAvion",
        "variables" : ["x", "y"],
        "preconditions" : [
          {
            "name" : "aeropuerto",
            "value" : ["x", "a"]
          },
          {
            "name" : "aeropuerto",
            "value" : ["y", "b"]
          },
          {
            "name" : "estar",
            "value" : ["x"]
          }
        ],
        "postconditions" : [
          {
            "name" : "comprarTiquete",
            "value" : ["a", "b"]
          },
          {
            "name" : "viajar",
            "value" : ["x", "a"]
          },
          {
            "name" : "volar",
            "value" : ["a", "b"]
          },
          {
            "name" : "viajar",
            "value" : ["b", "y"]
          }
        ]
      },
      {
        "name" : "viajar",
        "variables" : ["x", "y"],
        "preconditions" : [
          {
            "name" : "estar",
            "value" : ["x"]
          }
        ],
        "postconditions" : [
          {
            "name" : "conseguirTaxi",
            "value" : ["x"]
          },
          {
            "name" : "irTaxi",
            "value" : ["x", "y"]
          }
        ]
      }
    ],
    "operators": [
      {
        "name": "comprarTiquete",
        "variables" : ["x", "y"],
        "preconditions" : [
          {
            "name": "aeropuerto",
            "value": ["a", "x"]
          },
          {
            "name": "aeropuerto",
            "value": ["b", "y"]
          }
        ],
        "del":[],
        "add":[
          {
            "name": "tenerTiquete",
            "value": ["x", "y"]
          }
        ]
      },
      {
        "name" : "volar",
        "variables" : ["x", "y"],
        "preconditions" : [
          {
            "name" : "estar",
            "value" : ["x"]
          },
          {
            "name" : "tenerTiquete",
            "value" : ["x", "y"]
          }
        ],
        "del" : [
          {
            "name" : "estar",
            "value" : ["x"]
          },
          {
            "name" : "tenerTiquete",
            "value" : ["x", "y"]
          }
        ],
        "add": [
          {
            "name" : "estar",
            "value" : ["y"]
          }
        ]
      },
      {
        "name" : "conseguirTaxi",
        "variables" : ["x"],
        "preconditions" : [
          {
            "name" : "estar",
            "value" : ["x"]
          }
        ],
        "del" : [],
        "add": [
          {
            "name" : "taxi",
            "value" : ["x"]
          }
        ]
      },
      {
        "name" : "irTaxi",
        "variables" : ["x", "y"],
        "preconditions" : [
          {
            "name" : "taxi",
            "value" : ["x"]
          },
          {
            "name" : "estar",
            "value" : ["x"]
          }
        ],
        "del" : [
          {
            "name" : "taxi",
            "value" : ["x"]
          },
          {
            "name" : "estar",
            "value" : ["x"]
          }
        ],
        "add": [
          {
            "name" : "estar",
            "value" : ["y"]
          }
        ]
      }
    ],
    "output": {}
  }

  plan = run_htn(problem)
  print('\nplan -> ', plan)
