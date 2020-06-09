from sanic import Sanic, response
from sanic.response import json
from sanic_cors import CORS
import jwt
from uuid import uuid4
from os import remove
import os

import model
from strip.file_strip import create_file
from strip.strips import main
from problems import PROBLEMS
from htn.htn import run_htn

app = Sanic(__name__)
CORS(app)

@app.route('/aiplanner/auth/sign-up', methods=['POST', 'OPTIONS'])
async def sign_up(request):
  if request.method == 'OPTIONS':
    return response.json({})
  
  data = request.json
  if not data:
      return response.json({'auth': False, 'message': 'Datos requeridos'}, status=404)

  data['problems'] = PROBLEMS
  _id = model.save_user(data)
  if not _id:
    return response.json({'auth': False, 'message': 'El usuario ya existe'}, status=404)
  token = jwt.encode({'_id': _id}, os.getenv('TOKEN_KEY'))
  return response.json({'auth': True, 'token': token, 'name': data.get('name')}, status=201)

@app.route('/aiplanner/auth/login', methods=['POST', 'OPTIONS'])
async def login(request):
  if request.method == 'OPTIONS':
    return response.json({})
  
  data = request.json
  if not data:
    return response.json({'auth': False, 'message': 'Datos requeridos'}, status=404)
  
  user = model.get_user_email(data.get('email'))
  if not user:
    return response.json({'auth': False, 'message': 'Usuario no encontrado'}, status=404)
  
  if data.get('password') != user.get('password'):
    return response.json({'auth': False, 'message': 'Clave o usuario inválido. Inténtalo de nuevo'}, status = 401)
  
  token = jwt.encode({'_id': str(user.get('_id'))}, os.getenv('TOKEN_KEY'))
  return response.json({'auth': True, 'token': token, 'name': user.get('name')}, status=200)

@app.route('/aiplanner/user', methods=['PUT', 'OPTIONS'])
async def change_user(request):
  if request.method == 'OPTIONS':
    return response.json({})
  
  token = request.headers.get('Authorization')
  token = token.split(' ')[1]
  if not token:
    return response.json({'auth': False, 'message': 'No ha enviado un token'}, status=401)

  data = request.json
  if not data:
    return response.json({'auth': False, 'message': 'Datos requeridos'}, status=404)

  try:
    decoded = jwt.decode(token, os.getenv('TOKEN_KEY'), verify=True)
  except jwt.exceptions.DecodeError as e:
    return response.json({'auth': False, 'message': 'Token invalido'}, status=401)
  
  user = model.get_user_id(decoded.get('_id'))
  if data.get('currentPassword') != user.get('password'):
    return response.json({'auth': False, 'message': 'Clave inválida. Inténtalo de nuevo'}, status = 401)
  
  del user['_id']
  user['password'] = data.get('newPassword')
  model.replace_user(decoded.get('_id'), user)
  return response.json({'auth': True, 'message': 'Ok'}, status=200)

@app.route('/aiplanner/user/strip/problem', methods=['POST', 'OPTIONS'])
async def save_problem(request):
  if request.method == 'OPTIONS':
    return response.json({})

  data = request.json
  if not data:
    return response.json({'auth': False, 'message': 'Datos requeridos'}, status=404)
  
  token = request.headers.get('Authorization')
  token = token.split(' ')[1]
  _id = ''

  if token != 'null':
    try:
      decoded = jwt.decode(token, os.getenv('TOKEN_KEY'), verify=True)
    except jwt.exceptions.DecodeError as e:
      return response.json({'auth': False, 'message': 'Token invalido'}, status=401)
    
    _id = decoded.get('_id')
    create_file(_id, data)
    result = main(_id)
    if not result:
      result = {'Error': 'Solución no encontrada'}
    
    user = model.get_user_id(_id)
    del user['_id']
    data['output'] = result
    name = data['name']
    user['problems']['strip'][name] = data
    model.replace_user(_id, user)
  else:
    _id = str(uuid4())
    create_file(_id , data)
    result = main(_id)
    if not result:
      result = {'Error': 'Solución no encontrada'}

  remove('strip/'+ _id +'.txt')
  return response.json({'auth': True, 'message': result}, status=200)

@app.route('/aiplanner/user/htn/problem', methods=['POST', 'OPTIONS'])
async def save_problem(request):
  if request.method == 'OPTIONS':
    return response.json({})

  data = request.json
  if not data:
    return response.json({'auth': False, 'message': 'Datos requeridos'}, status=404)
  
  token = request.headers.get('Authorization')
  token = token.split(' ')[1]
  _id = ''

  if token != 'null':
    try:
      decoded = jwt.decode(token, os.getenv('TOKEN_KEY'), verify=True)
    except jwt.exceptions.DecodeError as e:
      return response.json({'auth': False, 'message': 'Token invalido'}, status=401)
    
    _id = decoded.get('_id')
    result = run_htn(data)
    if not result:
      result = {'Error': 'Solución no encontrada'}
    
    user = model.get_user_id(_id)
    del user['_id']
    data['output'] = result
    name = data['name']
    user['problems']['htn'][name] = data
    model.replace_user(_id, user)
  else:
    _id = str(uuid4())
    result = run_htn(data)
    if not result:
      result = {'Error': 'Solución no encontrada'} 

  return response.json({'auth': True, 'message': result}, status=200)

@app.route('/aiplanner/user/problems', methods=['GET', 'OPTIONS'])
async def get_problems(request):
  if request.method == 'OPTIONS':
    return response.json({})

  token = request.headers.get('Authorization')
  token = token.split(' ')[1]
  if not token:
    return response.json({'auth': False, 'message': 'No ha enviado un token'}, status=401)

  try:
    decoded = jwt.decode(token, os.getenv('TOKEN_KEY'), verify=True)
  except jwt.exceptions.DecodeError as e:
    return response.json({'auth': False, 'message': 'Token invalido'}, status=401)

  user = model.get_user_id(decoded.get('_id'))
  return response.json({'auth': True, 'message': user.get('problems')}, status=200)

@app.route('/aiplanner/user/<type_problem>/problem/<key>', methods=['DELETE', 'OPTIONS'])
async def delete_problem(request, type_problem, key):
  if request.method == 'OPTIONS':
    return response.json({})

  token = request.headers.get('Authorization')
  token = token.split(' ')[1]
  if not token:
    return response.json({'auth': False, 'message': 'No ha enviado un token'}, status=401)

  try:
    decoded = jwt.decode(token, os.getenv('TOKEN_KEY'), verify=True)
  except jwt.exceptions.DecodeError as e:
    return response.json({'auth': False, 'message': 'Token invalido'}, status=401)
  
  user = model.get_user_id(decoded.get('_id'))
  del user['problems'][type_problem][key]
  model.replace_user(decoded.get('_id'), user)
  return response.json({'auth': True, 'message': 'Ok'}, status=200)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=(os.environ.get('PORT', 8000)))
