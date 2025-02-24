import typer
from polynomialSolver import PolynomialSolver

app = typer.Typer()

def display_equation_and_degree(solver):
    parsed_equation = solver.get_parsed_equation()

    equation_str = ''
    for key, value in parsed_equation.items():
        equation_str += f"{value.replace('-', '- ').replace('+', '+ ')} * X^{key} "
    
    if equation_str:
        print(f"Reduced form: {equation_str}= 0")
    else:
        print(f"Reduded form: 0 = 0")
    if parsed_equation:
        polynomial_degree = max(parsed_equation.keys())
    else:
        print("All real numbers are solutions")
        exit()
    print(f"Polynomial degree: {polynomial_degree}")
    if int(polynomial_degree) > 2:
       raise Exception("The polynomial degree is stricly greater than 2, I can't solve.")
    
    return polynomial_degree, parsed_equation



@app.command(name="mandatory")
def solve_equation(equation: str):
    try:
        solver = PolynomialSolver(equation)
        polynominal_degree, parsed_equation = display_equation_and_degree(solver)
        if polynominal_degree == '2':
            PolynomialSolver.solve_degree_2(parsed_equation)
        else:
            PolynomialSolver.solve_degree_1(parsed_equation)
    except Exception as e:
        print(f"Error : {e}")

@app.command(name="bonus")
def solve_equation_bonus(equation: str):
    from advanced_polynomial_solver import AdvancedPolynomialSolver

    try:
        solver = AdvancedPolynomialSolver(equation)
        polynomial_degree, parsed_equation = display_equation_and_degree(solver)
        if polynomial_degree == '2':
            solver.solve_degree_2(parsed_equation)
        else:
            solver.solve_degree_1(parsed_equation)
    except Exception as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    app()
