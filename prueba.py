def mortgage_payment(principal, interest_rate, term):
    r = interest_rate / 12
    n = term * 12
    payment = (r * principal) / (1 - (1 + r) ** -n)
    return payment

if __name__ == '__main__':
    principal = float(input('Enter the loan amount: '))
    interest_rate = float(input('Enter the interest rate (as a decimal): '))
    term = int(input('Enter the term of the loan (in years): '))
    payment = mortgage_payment(principal, interest_rate, term)
    print('Your monthly mortgage payment is ${:.2f}'.format(payment))
#Este código define una función llamada mortgage_payment que toma como argumentos el monto del préstamo, la tasa de interés y el término del préstamo en años. Luego, utiliza una fórmula conocida para calcular el pago mensual de la hipoteca. Finalmente, el programa principal pide al usuario que ingrese estos valores y llama a la función para calcular el pago mensual.




