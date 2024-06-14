import bcrypt

class Login:
    def __init__(self) -> None:
        self.__logins_cadastrados = []
        
    def criar_senhaCriptografada(self,senha):
        senha_bytes = senha.encode("utf-8")
        salt_senha = bcrypt.gensalt()
        senha_criptografada = bcrypt.hashpw(senha_bytes,salt_senha)
        return senha_criptografada
    
    def cadastrar_novo_login(self, usuario: str, senha: str) -> dict:
        self.__logins_cadastrados.append({usuario: senha})
        return {usuario: senha}