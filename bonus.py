import sys
from advanced_polynomial_solver import AdvancedPolynomialSolver

def main():
    if len(sys.argv) != 2:
        print("Error: Invalid number of arguments")
        return
    parsed_equation = AdvancedPolynomialSolver(sys.argv[1]).get_parsed_equation()

    equation = ''
    for key, value in parsed_equation.items():
        equation += f"{value.replace("-",'- ').replace('+', '+ ')} * X^{key} "
    
    print(f"Reduced form: {equation}= 0")
    polynomial_degree = max(list(parsed_equation.keys()))
    print(f"Polynomial degree: {polynomial_degree}")
    if polynomial_degree > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    elif polynomial_degree == 2:
        AdvancedPolynomialSolver.solve_degree_2(parsed_equation)
    else:
        AdvancedPolynomialSolver.solve_degree_1(parsed_equation)

if __name__ == "__main__":
    main()
