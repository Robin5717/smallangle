import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2*pi",
    show_default=True # show default in help
)
def sin(number):
    """Calculates values for sin between 0 and 2pi

    Args:
        number (integer): Number of steps
    """     
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return 



@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of steps between 0 and 2*pi",
    show_default=True
)
def tan(number):
    """Calculates values for sin between 0 and 2pi

    Args:
        number (integer): Number of steps
    """    
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


@cmd_group.command()
@click.option(
    "-e",
    "--epsilon",
    default=0.1,
    help="accuracy for which the smallest angle approximation holds",
    show_default=True
)
def approx(epsilon):
    """for the given accuracy calculates the largest angle for which the small angle approx for sin holds

    Args:
        epsilon (float): desired accuracy
    """    
    grootste = False
    x = 0
    while grootste == False and x != 2*pi:
        if abs(x-np.sin(x)) > epsilon:
            grootste = True
        else:
            x += 0.001
    print(f"For an accuracy of {epsilon}, the small-angle approximation holds up to x = {round(x,3)}")
        
    return


if __name__ == "__main__":
    cmd_group()