import re

def is_valid_email(addr):
    if re.match(r'^([0-9a-zA-Z\w.]*)(@)(\w*)\.(\w{3})$',addr):
        return True
    else:
        return False
        

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')