import re

def is_valid_email(addr):
    if re.match(r'^([0-9a-zA-Z\w.]*)(@)(\w*)\.(\w{3})$',addr):
        print('%s is a email' % addr)
        return True
    else:
        print('%s is not a email' %addr)
        return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


def name_of_email(addre):
    m = re.match(r'^(<(?P<name>.+?)>)?\s*(?P<name1>[a-zA-Z]+)@([a-zA-Z]+)[.]([a-zA-Z]{3})',addre)
    firstName = m.group('name')
    secondName = m.group('name1') 
    if m :
        if firstName is not None:
            print('%s => %s' % (addre,firstName))
            return firstName
        else:
            print('%s => %s' % (addre,secondName))
            return secondName
    else:
        print('%s is not a email' %addr)

assert name_of_email('tom@voyager.org') == 'tom'
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
print('ok')