import instaloader
import schedule
import time

USERNAME = 'usuário_a_ser_verificado'
TARGET_USER = 'seguido'
YOUR_USERNAME = 'seu_usuario'
YOUR_PASSWORD = 'sua_senha'

# Instância do Instaloader
L = instaloader.Instaloader()

def login():
    try:
        L.login(YOUR_USERNAME, YOUR_PASSWORD)
        print('Login realizado com sucesso.')
    except Exception as e:
        print(f'Erro ao fazer login: {e}')

def get_following(username):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        following = [followee.username for followee in profile.get_followees()]
        return following
    except Exception as e:
        print(f'Erro ao obter seguidores: {e}')
        return []

def check_user():
    following = get_following(USERNAME)
    if TARGET_USER in following:
        print(f'{TARGET_USER} ainda está sendo seguido por {USERNAME}')
    else:
        print(f'Notificação: {TARGET_USER} não está mais sendo seguido por {USERNAME}')

login()

check_user()

schedule.every(20).minutes.do(check_user)

print('Iniciando monitoramento...')
while True:
    schedule.run_pending()
    time.sleep(1)
