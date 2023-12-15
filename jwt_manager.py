from jwt import encode, decode # pip install pyjwt
#import dotenv

SECRET = "1234567890"
ALGORITHM = "HS256"

# variables de entorno en python, se utiliza el modulo dotenv
def create_token(data, secret=SECRET):
    return encode(data, secret, ALGORITHM)

def validate_token(token):
    return decode(token, SECRET, [ALGORITHM])