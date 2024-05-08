from ninja import NinjaAPI, Schema

api = NinjaAPI()

class LoginInput(Schema):
    username: str
    password: str

@api.post("/login")
def login(request, data: LoginInput):
    username = data.username
    password = data.password

    # Aquí puedes implementar la lógica de autenticación, como verificar en una base de datos

    if username == 'h4srl' and password == 'pater':
        return {'success': True, 'message': 'Login successful'}
    else:
        return {'success': False, 'message': 'Invalid username or password'}

if __name__ == "__main__":
    api.run(debug=True)
