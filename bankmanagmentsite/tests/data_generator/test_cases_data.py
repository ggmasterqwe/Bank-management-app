import random


NAMES = ['عباس','سهیل','سمیرا','مریم','تینا','حسین','فزاز','علی']
LAST_NAMES = ['قانع','مرادی','ثامانی','گیرا','عباسپور','تهرانی','دایار']
PASSWORD = 'junk123#'

BRANCH_NAME = ['نیاوران','پاسداران','دولت','انقلاب','هفت تیر']

def random_name():
    x = random.randint(0, len(NAMES)-1)
    y = random.randint(0, len(LAST_NAMES)-1)

    return NAMES[x], LAST_NAMES[y]


def random_phone_number():
    return '0912{}'.format(random.randint(1000, 90000))


def random_nationalid():
    return '195{}'.format(random.randint(1000,9999))


def random_branch_name():
    x = random.randint(0, len(BRANCH_NAME)-1)
    return BRANCH_NAME[x]

def branch_admin_data():
    first_name, last_name =random_name()

    data = {
        'first_name':first_name,
        'last_name':last_name,
        'nationalid':random_nationalid(),
        'phone_number':random_phone_number(),
        'salary':100000,
        'password':PASSWORD

    }
    
    return data

def random_branch_data(admin):
    data = {
        'name':random_branch_name(),
        'telephone':random_phone_number(),
        'admin':admin,
        'address':random_branch_name()
    }
    return data

def random_client_data():
    first_name, last_name = random_name()
    data = {
        'first_name':first_name,
        'last_name':last_name,
        'phone_number':random_phone_number(),
        'nationalid':random_nationalid(),
        
    }
    return data

def random_admin_data():
    first_name, last_name = random_name()
    data = {
        'first_name':first_name,
        'last_name':last_name,
        'phone_number':random_phone_number(),
        'nationalid':random_nationalid(),
        'password':PASSWORD
        
    }
    return data