import sys
from advanced_polynomial_solver import AdvancedPolynomialSolver


def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError("Error: Invalid number of arguments")
        
        
        parsed_equation = AdvancedPolynomialSolver(sys.argv[1]).get_stock()
        
        # parse_equation(sys.argv[1])
        # stock = {}
        # equation = sys.argv[1].split("=")
        # stock = get_reduced_form(equation[0], 'left')
        # stock = get_reduced_form(equation[1], 'right', stock)
    
        # print(f"Reduced form: {equation}= 0")
        # polynomial_degree = max(list(stock.keys()))
        # print(f"Polynomial degree: {polynomial_degree}")
        # if polynomial_degree > 2:
        #     print("The polynomial degree is stricly greater than 2, I can't solve.")
        # elif polynomial_degree == 2:
        #     solve_degree_2(stock)
        # else:
        #     solve_degree_1(stock)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
