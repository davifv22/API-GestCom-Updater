from flask_restful import Resource
from api.app import api
from flask import request, make_response, jsonify
from ..schemas import user_schema
from ..entidades import user
from ..services import user_service
import uuid


class UserList(Resource):
    def post(self):
        us = user_schema.UserSchema()
        v = us.validate(request.json)
        if v:
            return make_response(jsonify(v), 400)
        else:
            user_ = request.json['user']
            nome = request.json['nome']
            email = request.json['email']
            senha = request.json['senha']
            situacao = True
            is_admin = request.json['is_admin']
            api_key = str(uuid.uuid4())
            
            novo_user = user.User(user=user_, nome=nome, email=email, senha=senha, situacao=situacao, is_admin=is_admin, api_key=api_key)
            x = user_service.set_user(novo_user)
            
            return make_response(us.jsonify(x), 201)


api.add_resource(UserList, '/user')