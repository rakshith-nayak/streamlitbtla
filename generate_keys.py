import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ['BTLA_Product_Team']
usernames = ['BTLA_Product_Team']
passwords = ['Analytics@BTLA']

# Uses bcrypt algorithm for hashing
hashed_passwords = stauth.Hasher(passwords).generate()


file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as file:
	pickle.dump(hashed_passwords, file)
