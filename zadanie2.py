from random import uniform
from math import sqrt

class Vector:

    def __init__(self, arg=3):
        """ input: wymiar wektora (int)
         funkcja określa wymiar wektora"""
        self.l=[]
        for i in range(arg):
            self.l.append(0)


    def nrgen(self):
        """input: brak
            output: zmienia wartości wektora na liczby z zakresu (-100, 100)"""
        for i in range(len(self.l)):
            self.l[i] = uniform(-100, 100)

    def load(self, s):
        """input: lista
                output: zmienia wartości wektora na podane w inpucie albo wywołuje błąd przy błędnym wymiarze"""
        if len(s)==len(self.l):
            self.l=s
        else:
            raise ValueError('zły wymiar')


    def __add__(self, k):
        """input: lista (list)
            output: suma
            funkcja określająca dodawanie w klasie jako sumę wektorów"""
        if len(self.l)!=len(k.l):
            raise ValueError('zły wymiar')
        else:
            for i in range(len(self.l)):
                self.l[i] = self.l[i] + k[i]
            return self.l


    def __sub__(self, k):
        """input: lista
            output: różnica
            funkcja określająca odejmowanie w klasie jako różnicę wektorów"""
        if len(self.l)==len(k.l):
            for i in range(len(self.l)):
                self.l[i]=self.l[i]-k[i]
            return self.l
        else:
            raise ValueError('zły wymiar')

    def scalar(self, p):
        """input: int
            output: iloczyn skalarny
            funkcja określająca iloczyn skalarny wektorów """
        for i in range(len(self.l)):
            self.l[i]=p*self.l[i]
        return self.l

    def len(self):
        """input: brak
            output: długośc wektora (int)
            funkcja obliczająca długość wektora"""
        u = []
        for i in range(len(self.l)):
            u.append((self.l[i])**2)
        x=0
        for j in range(len(u)):
            x+=u[j]
        return sqrt(x)


    def sum(self):
        """input: brak
            output: suma wyrazów wektora (float)
            funkcja obliczająca sumę wszystkich wyrazów wektora"""
        x=0
        for j in range(len(self.l)):
            x+=self.l[j]
        return x

    def __mul__(self, v2):
        """input: wektor (list)
            output: iloczyn wektorowy
            operator określający mnożenie na klasie jako iloczyn wektorowy"""
        if len(self.l)==len(v2.l):
            result=0
            for i in range(len(self.l)):
                result+=(self.l[i]*v2[i])
            return result
        else:
            raise ValueError('zły wymiar')

    def __str__(self):
        """input: brak
            output: wektor (list)
            operator returnujący reprezentację tekstową wektora"""
        return str(self.l)

    def __getitem__(self, n):
        """input: indeks wektora (int)
           output: wyraz z wektora (int)
           operator pozwalający na dostęp do konkretnego wyrazu z wektora"""
        if n<=len(self.l):
            return self.l[n]
        else:
            raise ValueError('zły indeks')

    def __cmp__(self, y):
        """input: liczba (int)
            output: T/F (bool)
            operator sprawdzający czy podany wyraz znajduje się w wektorze"""
        if y in self.l:
            return True
        else:
            return False


