#! python3

import logging
# Nota si cambiamos el valor del parametro level  a logging.CRITICAL
# Desactivamos los mensajes del log en toda la ejecucion del programaclea
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

#_logger = logging.getLogger('__name__')

def factorial(n):
    logging.debug('Start of factoral(%s%%)' % (n))
    total = n
    for i in range(1,n):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total



if __name__ == '__main__':
    try:
        n = int(input('Ingrese un numero por favor: '))
    #assert n.isdigit() == False , 'No es un numero'
    except ValueError as e:
        print('Debe ingresar solo numeros al programa {}'.format(e))

    result = factorial(n)
    print('El resutado del factorial de {}  es {}'.format(n, result))
logging.debug('End of program')

"""Here we use the logging.debug() function when we watn to print log
information. This debug() function will call basicConfig(), and a line of information will be printed.
This information will be in the format we specified in basicConfig() and will include the messages 
we passed to debug().  print(factorial(5)) call is part of the original program, so the result is 
displayed even if logging messages are disabled."""
