from typing import Tuple
import berserk

def setup() -> Tuple:
    with open("token.txt","r") as token_file:
        TOKEN = token_file.readline()

    session = berserk.TokenSession(TOKEN)
    client = berserk.Client(session=session)

    return session, client