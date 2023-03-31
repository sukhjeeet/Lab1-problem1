# Function to calculate the bill
def calculate_bill(patient_name, cleaning_performed, cavity_filling_performed, xray_performed):
    # Set rates
    cleaning_rate = 60
    cavity_filling_rate = 200
    xray_rate = 100
    tax_rate = 0.15
    
    # Calculate the subtotal based on the services performed
    subtotal = 0
    if cleaning_performed.lower() == 'y':
        subtotal += cleaning_rate
    if cavity_filling_performed.lower() == 'y':
        subtotal += cavity_filling_rate
    if xray_performed.lower() == 'y':
        subtotal += xray_rate
        
    # Calculate the tax and total
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    # Apply discount if applicable
    if total > 300:
        total *= 0.9
    elif total > 200:
        total *= 0.95
    
    # Print the receipt
    print("Melanie Dental Clinic")
    print("Patient's name:", patient_name)
    print("Cleaning performed:", cleaning_performed)
    print("Cavity filling performed:", cavity_filling_performed)
    print("X-Ray performed:", xray_performed)
    print("Subtotal: $", subtotal)
    print("Tax ({}%): $".format(tax_rate * 100), tax)
    print("Total: $", total)

# Get inputs from user
patient_name = input("Enter patient's name: ")
cleaning_performed = input("Was cleaning performed? (y/n): ")
cavity_filling_performed = input("Was cavity-filling performed? (y/n): ")
xray_performed = input("Was X-Ray performed? (y/n): ")

# Calculate the bill and print the receipt
calculate_bill(patient_name, cleaning_performed, cavity_filling_performed, xray_performed)
