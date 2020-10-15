# --------------------------
#      Unit Test
# --------------------------

'''
mspack.msmath and mspack.msstring modules are tested by 
chapter2_test.py file.
'''

from mspack import msmath
from mspack import msstring

print ( "Sum: ", msmath.sum(10, 20) )
print ( "Division: ", msmath.division(25, 5))
print ( "Full Name: ", msstring.MsName("Mahmud", "Ahsan").full_name())

------------------------------
# --------------------------
#      Unit Test
# --------------------------

'''
This test module test msmath and msstring module from mspack package
Common testing methods by TestCase:
    assertEqual(x,y)
    assertTrue(expression)
    assertIn(item, list)
'''

import unittest
from mspack import msmath
from mspack import msstring

class MsPackMsMathTestCase(unittest.TestCase):
    def test_sum(self):
        sum = msmath.sum(8, 12)
        self.assertEqual(sum, 20)
        
    def test_subtract(self):
        result = msmath.subtract(109, 9)
        self.assertTrue(result == 100)
        
    def test_multiplication(self):
        result = msmath.multiplication(9, 3)
        self.assertEqual(result, 27)
        
        result = msmath.multiplication(100, 3)
        self.assertEqual(result,300)
        
    def test_division(self):
        result = msmath.division(50, 25)
        self.assertEqual(result, 2)
        
class MsPackMsStringTestCase(unittest.TestCase):
    def test_full_name(self):
        name = msstring.MsName("Life", "Good").full_name()
        self.assertEqual("Life Good", name)
        
class MsPackMsString1TestCase(unittest.TestCase):
    def setUp(self): # setUp U is in uppercase
        self.str_obj = msstring.MsName("Life", "Good")
        
    def test_full_name(self):
        name = self.str_obj.full_name()
        self.assertEqual("Life Good", name)
        
    def test_full_name_length(self):
        length = len(self.str_obj.full_name())
        self.assertTrue(length == 9)
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
--------------------------
# --------------------------
#      Regular Expression
# --------------------------

'''
https://regex101.com
'''

## Text pattern matching
import re

date_data = '13/Feb/2019 I will go Canada'

if re.match(r'\d+/[a-zA-Z]+/\d{4}', date_data):
    print ("Matched")
else:
    print ("Mismatched")
    
## Compiling pattern for reuse
   
import re 
date_data    = '13/Feb/2019 I will go Canada'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

if date_pattern.match(date_data):
    print ("Matched")
else:
    print ("Mismatched")

## Matching all occurrences

import re 
date_data    = '13/Feb/2019 hmm 20/Mar/2038 ok 13/Feb/2019'
date_pattern = re.compile(r'\d+/[a-zA-Z]+/\d{4}')

result = date_pattern.findall(date_data)
print (result)

## Capture groups

import re 
date_data    = '13/Feb/2019 I will go Canada'
date_pattern = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

result       = date_pattern.match(date_data)

for x in range(0, 4):
    print ( result.group(x) )

print (result.groups())

day, month, year = result.groups()
print ("Today's day is: ", day)

## Raw String

import re

date_data = '13/Feb/2019 I will go Canada'

# r'\d+/[a-zA-Z]+/\d{4}' RAW String doesn't interpret \n escape char
if re.match('\\d+/[a-zA-Z]+/\\d{4}', date_data):
    print ("Matched")
else:
    print ("Mismatched")
    
## Search and Replace
    
import re

date_data     = '13/Feb/2019 I will go Canada' # Convert to 2019-Feb-13
date_pattern  = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')
print ("Before: ", date_data)

date_modify1 = date_pattern.sub(r'\3-\2-\1', date_data)
print ("After: ", date_modify1)

### Capital letter of month name
import re

date_data     = '13/Feb/2019 I will go Canada' 
date_pattern  = re.compile(r'(\d+)/([a-zA-Z]+)/(\d{4})')

def to_upper(m):
    return '{} {} {}'.format(m.group(3), m.group(2).upper(), m.group(1))

date_modify2 = date_pattern.sub(to_upper, date_data)
print ("After: ", date_modify2)

## Case-insensitive search

import re 

text = "I am GOOD, but I am NOt very good"
list = re.findall('good', text, flags=re.IGNORECASE)
print (list)
text = re.sub('gOOd', 'bad', text, flags=re.IGNORECASE)
print (text)


## Unicode characters
import re 

num = re.compile(r'\d') # also show '\d+'
list = num.findall('১২৩৪ আমার দেশ বাংলাদেশ')
print (list)

## Strip unwanted middle space

import re 

text = "Life            is            Good"
txtre = re.compile(r'\s+')
text = txtre.sub(' ', text)
print (text)
----------------
# --------------------------
#      Web Scraping
# --------------------------

## News title, link scraping

from webscrap import wlog
from webscrap import wscrap

# Define log file location
wlog.set_custom_log_info('html/error.log')

'''
# Testing log file reporting
try:
    raise Exception
except Exception as e:
    wlog.report(str(e))
'''

news_scrap = wscrap.NewsScraper(wscrap.url_aj, wlog)

## UNCOMMENT THE FOLLOWING 2 LINES OF CODE TO GET SITE'S LATEST DATA
## OTHERWISE THIS PROGRAM PARSE DATA FROM DISK FILE RETRIEVED PREVIOUSLY

#news_scrap.retrieve_webpage()
#news_scrap.write_webpage_as_html()

news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
#news_scrap.print_beautiful_soup()
news_scrap.parse_soup_to_simple_html()

--------------------
# --------------------------
#      Generator
# --------------------------

# Iterable 
str = "Hello World"
for i in str:
    print(i)
    
print("\nList Comprehension\n")

# List Comprehension
list = [x*x+2 for x in range(1, 5)]
for item in list:
    print(item)
    
# Everything we can use using for...in are iterable
# But for iteration all the values are stored in memory

print("\nGenerator\n")

# Generator
gen = (x*x+2 for x in range(1, 5)) # Generator comprehension
for item in gen:
    print(item)
    
# Nothing will print again, Gen is no longer available
for item in gen:
    print(item)
    
# Generator are kind of iterator which can only iterate once
# Generator do not store values in memory
# Generator generates value on fly
# List comprehension when iterator we use []
# Generator comprehension of List we use ()

print("\ngen123\n")
def gen123():
    yield 1 
    yield 2
    yield 3

print(gen123)    
print(gen123())
    
for i in gen123():
    print(i)

print("\ngen123 again\n")
gen_obj = gen123()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj)) # for loop catch the exception and terminate

# A function can not have both return and yield keywords
# yield is like return. The difference is when the function call again execution starts from the last call to yield statement
------------------------------------
# --------------------------
#  Closures
# --------------------------

# Highter order function example
def make_total():
    arr = []
    
    def get_total(value):
        arr.append(value)
       
        return sum(arr)
    
    return get_total
    
sum1 = make_total()
print(sum1(10))
print(sum1(20))

# Another example
def make_total2():
    total = 0
    
    def get_total(value):
        nonlocal total
        
        total += value
        return total
    
    return get_total
    
sum2 = make_total2()
print(sum2(10))
print(sum2(20))
______________________

# --------------------------
#      Metaprogramming: Decorator
# --------------------------

# Decorator is a callable that takes callable as argument and returns another callable
# The function which is passed as argument is called decorated function.
# It can process, change the decorated function 
# It either returns the original function or replace it with another function
# A decorator usually replace a function with different one which is part of metaprogramming

# Example 1
def decor(decoratedFunc):
    def inner():
        print("Inner Function")
    return inner 
    
def testFunc():
    print("Test Func")
    
decorated_func = decor(testFunc)
decorated_func()

print()
## syntactic sugar 
@decor
def testFunc1():
    print("Test Func1")
    
testFunc1()
    

print(testFunc)
print(testFunc1)

## Example 2 Uppercase
def uppercase(function):
    def decorated(*args):
        result = function(*args)
        result_upper = result.upper()
        return result_upper 
    return decorated
    
@uppercase 
def person_name(name):
    return name
    
upper_name = person_name("mahmud ahsan")
print(upper_name)

print(person_name("bill gates"))

---------------------------

# --------------------------
#  List Slicing - Techniques
# --------------------------

# syntax: list[start:end:step] # returns a new list
# end always exclusive

mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

## print all
print(mlist[:])

print()
## natural sequence of getting 5 elements
print(mlist[0:5:1])

print()
## skip one element and print all
print(mlist[::2])

print()
## copy of original list in reverse order
print(mlist[::-1]) # check by -2

# mlist.reverse() # modify the original list
# print(mlist)

print()
## copy list
crlist = mlist 
print(f'mlist: {mlist}')
print(f'crlist: {crlist}')
mlist.reverse()
print(f'mlist: {mlist}')
print(f'crlist: {crlist}')

print()
## cloning list
clist = mlist[:]
mlist.reverse()
print(f'mlist: {mlist}')
print(f'clist: {clist}')

## clear all elements
del mlist[:]
print(mlist)
___________________________

# --------------------------
#      Web Scraping
# --------------------------

'''
urllib
BeautifulSoup
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Installing Beautiful Soup
pip install beautifulsoup4
'''

from urllib.request import urlopen 
from bs4 import BeautifulSoup

# Global variables
url_aj   = 'http://www.aljazeera.com'
filepath = 'html/aj.html'
    
class NewsScraper:
    __url   = ''
    __data  = ''
    __wlog  = None
    __soup  = None 
    
    def __init__(self, url, wlog):
        self.__url  = url 
        self.__wlog = wlog 
    
    def retrieve_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            print (e)
            self.__wlog.report(str(e))
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print ("Retrieved successfully")
            
    def write_webpage_as_html(self, filepath=filepath, data=''):
        try:
            with open(filepath, 'wb') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
            
    def read_webpage_from_html(self, filepath=filepath):
        try:
            with open(filepath) as fobj:
                self.__data = fobj.read()
        except Exception as e:
            print (e)
            self.__wlog.report(str(e))
            
    def change_url(self, url):
        self.__url = url
            
    def print_data(self):
        print (self.__data)
    
    def convert_data_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, "html.parser")
        
    def parse_soup_to_simple_html(self):
        news_list = self.__soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) # h1
        
        #print (news_list)
        
        htmltext = '''
<html>
    <head><title>Simple News Link Scrapper</title></head>
    <body>
        {NEWS_LINKS}
    </body>
</html>
'''
        
        news_links = '<ol>'
        
        for tag in news_list:
            if tag.parent.get('href'):
                # print (self.__url + tag.parent.get('href'), tag.string)
                link  = self.__url + tag.parent.get('href')
                title = tag.string
                news_links += "<li><a href='{}' target='_blank'>{}</a></li>\n".format(link, title)
                
        news_links += '</ol>'
        htmltext = htmltext.format(NEWS_LINKS=news_links)
        
        # print(htmltext)
        self.write_webpage_as_html(filepath="html/simplenews.html", data=htmltext.encode())
    
    
    def print_beautiful_soup(self):
        # print (self.__soup.title.string)
        news_list = self.__soup.find_all(['h1', 'h2', 'h4']) # h1
        
        #print (news_list)
        for tag in news_list:
            if tag.parent.get('href'):
                print (self.__url + tag.parent.get('href'), tag.string)
