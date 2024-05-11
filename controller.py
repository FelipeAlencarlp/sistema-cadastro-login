from models import Pessoa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib


def retorna_session():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    PORT = 3306
    BANCO = "cadastro_login"
    CONNECTION = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONNECTION, echo=True)
    Session = sessionmaker(bind=engine)

    return Session()


class ControllerCadastro:
    @classmethod
    def verificar_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        
        if len(email) > 200 or len(email) < 13:
            return 3
        
        if len(senha) > 100 or len(senha) < 6:
            return 4

        return 1

    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()

        if len(usuario) > 0:
            return 5

        dados_verificados = cls.verificar_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados
        
        try:
            senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
            pessoa = Pessoa(nome=nome, email=email, senha=senha_criptografada)

            session.add(pessoa)
            session.commit()

            return 1
        
        except:
            return 6


class ControllerLogin:
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
        usuario = session.query(Pessoa).filter_by(email=email, senha=senha_criptografada).all()

        if len(usuario) == 1:
            return {'logado' : True, 'id' : usuario[0].id}

        return False
    
print(ControllerLogin().login('felipealencar@gmail.com', 'felipe1234'))