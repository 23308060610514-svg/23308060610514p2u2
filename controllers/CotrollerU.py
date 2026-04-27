from models.usuario import UsuarioModel
from models.schemas import UsuarioSchema
from pydantic import ValidationError


class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, email, password):
        try:
            
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            
            return False, e.errors()[0]['msg']
        
    def login (self, email, password):
        try:
            
            usuario_login = UsuarioLogin(email = email, password = password)
            
            if sucess: 
                return True, "Inicio de secion exitoso"
        else:
            return False, "Datos de inicio de sesion no validos"