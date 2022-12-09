def calculate_tax(bill, tax_rate):
    return( round(bill * tax_rate/ 100.00, 2))

print("Total Tax is:" , calculate_tax(175.0056755, 15))