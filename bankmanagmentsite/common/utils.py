def calculate_daily_profit(amount):
    if amount==0:
        return 0
    anoual = amount/10
    per_day = anoual/360
    return per_day

def normalize_numbers(number):
    number_len = len(str(number))
    result = ''
    zero_needed = 5
    for i in range(0,5-number_len):
        result +='0'
    result+=str(number)
    return result


def generate_number(branch_id, user_id):
    branch_id=normalize_numbers(branch_id)
    user_id=normalize_numbers(user_id)

    return '31{}{}'.format(branch_id, user_id)

def get_seccond(x):
    return x[1]