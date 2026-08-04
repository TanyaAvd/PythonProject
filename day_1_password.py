import string as st
from unittest import result

st.digits
st.ascii_lowercase
st.ascii_uppercase
special='_!@#$%^&'

def check_password(password: str)->tuple[bool, str]:
   if  (len(password)<7 or len(password)>16):
        return False, f'Пароль не подходит. Длина пароля должна быть от 8 до 15 символов'

   else:
        result=''
        lower=upper=digit=special_sym=False
        for i in password:
            if i in special: special_sym=True
            elif i in st.digits: digit=True
            elif i in st.ascii_lowercase: lower=True
            elif i in st.ascii_uppercase: upper=True
            else:
                return False, f'Некорректный пароль'

        else:
            if not special_sym:
                result += ' нет спец символов\n'
            elif not digit:
                result +=' нет цифр\n'
            elif not lower:
                result +=' нет строчных букв\n'
            elif not upper:
                result +=' нет заглавных букв\n'

        if result:
            return False, result
        return True, result

def user_enter_password():
    for j in range(5):
        password=input(f'Попытка {j+1} - введите пароль ')
        status, msg=check_password(password)
        if status:
            print('Пароль корректен')
            break
        print(f'Пароль некорректен: {msg}')


#if __name__=='__main_':
#    user_enter_password()

password=input()
user_enter_password()
