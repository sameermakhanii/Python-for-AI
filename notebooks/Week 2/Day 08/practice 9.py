def invoice_numbers():
    number = 1
    while True:
        yield f"{number:04d}"
        number +=1

invoices = invoice_numbers()
print (next(invoices))
print (next(invoices))
print (next(invoices))
print (next(invoices))
        # print (next(number))


