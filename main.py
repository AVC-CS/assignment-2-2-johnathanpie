def main():
    """
    ##################################################
    # Comlete your code here
    # Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius = int(input())
    fahrenheit = (celcius * 9/5) + 32
    print(f'Temperature is {fahrenheit:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
