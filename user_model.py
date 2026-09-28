usuarios = {
    "admin": "1234",
    "teste": "senha123",
    "usuario": "12345"
}


def verificar_usuario(username, password):
    if username in usuarios:
        if usuarios[username] == password:
            return True

    return False