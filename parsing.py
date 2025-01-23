import sys

def get_reduced_form():
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        sys.exit(1)
    equation = sys.argv[1]
    
    
    # equation = f"equation - {equation.split("=")[1]}"
    stock = {}
    variables = equation.split("=")[0].split(" ")
    
    for var in variables:
        stock[f"{var}"] = 0
        print(var)
    
    
    
    print(equation)
    
    
    
if __name__ == "__main__":
    get_reduced_form()