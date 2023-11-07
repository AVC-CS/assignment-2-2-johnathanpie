def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    celcius = int(input())
    fahrenheit = (celcius * 9/5) + 32
    print(f'Temperature is {farenheit:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
