

def main():
    name = get_name()
    print(name[1::2])


def get_name():
    name = input('What is your name? ')
    while not name.strip():
        name = input('Please enter your name: ')
    return name

name = 'Jared Cooke'
frequency = int(input('frequency: '))
s=''
for i in range(0, len(name), frequency):
    if i % frequency == 0:
        s += name(i)