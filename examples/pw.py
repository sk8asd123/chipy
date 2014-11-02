#!/usr/bin/python

import uuid
import hashlib

class User:
    __id = 0
    def __init__(self, pw, age, name):
        self.ident = User.__id
        User.__id += 1
        self.name = name
        self.age = age
        self.pw = self.get_pw(pw)


    def get_pw(self ,pw):
        self.salt = uuid.uuid4().hex
        return hashlib.sha512(pw+self.salt).hexdigest() 

    def check_pw(self, pw):
        return self.pw == hashlib.sha512(pw + self.salt).hexdigest()

    def save(self, csv_file_name = 'usercred.csv'):
        with open(csv_file_name, 'a') as f:
            f.write('%d,%s,%s,%d,%s\n' % (self.ident, self.name, self.pw, self.age, self.salt))
       
    def debug_print(self):
	    print self.ident, self.name, self.pw, self.age, self.salt 


if __name__ == '__main__':
    u1 = User('pwd1', 12, 'user_one')
    u2 = User('pwd2', 14, 'user_two')
    u3 = User('pwd3', 17, 'user_three')

    u1.debug_print()
    u1.save()
   
    u2.debug_print()
    u2.save()

    u3.debug_print()
    u3.save()

