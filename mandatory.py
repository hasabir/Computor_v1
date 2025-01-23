import sys


def get_reduced_form(equation, equation_parts, stock={}):
    equation = equation.split(" ")
    for i in range(len(equation)):
        if equation[i] == '*':
            key = int(equation[i + 1].split("^")[1])
            value = f"{equation[i - 2]}{equation[i - 1]}"
                        
            if equation_parts == 'right':
                stock[key] = str(float(stock.get(key, 0)) - float(value))
                if stock[key] == '0.0':
                    del stock[key]
            else:
                if float(value) != 0:
                    stock[key] = value
    
    return stock

def solve_degree_2(stock):
    a = float(stock.get(2, 0))
    b = float(stock.get(1, 0))
    c = float(stock.get(0, 0))
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print(f"Discriminant is strictly positive, the two solutions are:\n{x1}\n{x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Discriminant is equal to zero, the solution is:\n{x}")
    else:
        print(f"Discriminant is strictly negative, the equation has no solution")


def solve_degree_1(stock):
    a = float(stock.get(1, 0))
    b = float(stock.get(0, 0))
    if a == 0:
        if b == 0:
            print("All real numbers are solutions")
        else:
            print("No solution")
    else:
        x = -b / a
        print(f"The solution is:\n{x}")


def main():
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        return
    
    stock = get_reduced_form(sys.argv[1].split("=")[0], 'left')
    stock = get_reduced_form(sys.argv[1].split("=")[1], 'right', stock)
    equation = ''
    for key, value in stock.items():
        equation += f"{value.replace("-",'- ').replace('+', '+ ')} * X^{key} "
    
    print(f"Reduced form: {equation}= 0")
    polynomial_degree = max(list(stock.keys()))
    print(f"Polynomial degree: {polynomial_degree}")
    if polynomial_degree > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    elif polynomial_degree == 2:
        solve_degree_2(stock)
    else:
        solve_degree_1(stock)

if __name__ == "__main__":
    main()
