"""
Задача №1
1.1 Написать программу, которая расшифрует строку.
Каждая символ - это две цифры. Отчет с 00 -> 'a', 01 -> 'b' и до 25 -> 'z',
26 - это пробел, он не входит в набор букв
Вход: строка из цифр. Выход: Текст.

1.2 Реализовать и расшифровку и зашифровку через функции
In/Out: '070411111426152419071413' <-> Out/In: 'hello python'

1.3 Добавить обработку неправильных входных данных.

1.4 Написать тесты для отработки корректных и некорректных данных.

"""
import unittest
import string as st
def decrypt(encrypted_text:str)->tuple[bool, str]:
    result_decrypt = []
    dec_dict={}
    enc_dict={}
    dec_dict , enc_dict=alphabet()
    for i in range(0, len(encrypted_text),2):
        code_str=encrypted_text[i:i+2]
        result_decrypt.append(dec_dict[code_str])
    return (''.join(result_decrypt))

def encrypt(test_decrypted:str)->tuple[bool, str]:
    result_encrypt=[]
    enc_dict ={}
    dec_dict={}
    dec_dict , enc_dict=alphabet()
    for i in test_decrypted:
        result_encrypt.append(enc_dict[i])
    return (''.join(result_encrypt))


def alphabet():
    code=0
    dec_dict={}
    enc_dict={}
    for i in st.ascii_lowercase:
        dec_dict[f'{code:02d}']=i
        enc_dict[i]=f'{code:02d}'
        code=code + 1
    dec_dict['26']=' '
    enc_dict[' ']='26'
    return dec_dict , enc_dict


def main():

    print('Введите строку из цифр, например 070411111426152419071413' )
    test_encrypted = input()
    if not ( len(test_encrypted) % 2== 0 and test_encrypted.isdigit()):
        print('Неправильный ввод данных. Условия: длина должна быть четной, в строке должны быть только цифры')
    else:
        print(decrypt(test_encrypted))
    print('Введите предложение, например hello python')
    test_decrypted = input().replace(" ","")
    if  not test_decrypted.isalpha() :
        print('Неправильный ввод данных. Недопустимые значения')
    else:
        print(encrypt(test_decrypted))


if __name__ == '__main__':
    main()

