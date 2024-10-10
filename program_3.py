def calculate_sales_tax(total_sales):
    state_tax_rate = 0.05
    county_tax_rate = 0.025
    
    state_tax = total_sales * state_tax_rate
    county_tax = total_sales * county_tax_rate
    total_tax = state_tax + county_tax
    
    return state_tax, county_tax, total_tax

def main():
  
    total_sales = float(input("Enter the total sales for the month: "))
    
   
    state_tax, county_tax, total_tax = calculate_sales_tax(total_sales)
    
    print(f"Amount of state sales tax: ${state_tax:.2f}")
    print(f"Amount of county sales tax: ${county_tax:.2f}")
    print(f"Total sales tax: ${total_tax:.2f}")

if __name__ == "__main__":
    main()
