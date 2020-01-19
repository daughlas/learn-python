try:
    print(1/'a')
except Exception as e:
    print('%s' %e)

try:
    raise NameError('helloError')
except NameError:
    print('my custom error')


try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    print('无论如何我都会执行')
    a.close()
