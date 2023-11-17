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


if __name__ == "__main__":
    cmd_group()