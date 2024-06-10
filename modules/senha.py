class Login:
    def __init__(self) -> None:
        self.__logins_cadastrados = []
    def cadastrar_novo_login(self, usuario: str, senha: str) -> dict:
        self.__logins_cadastrados.append({usuario: senha})
        return {usuario: senha}
    
