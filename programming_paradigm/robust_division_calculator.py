def safe_divide(numerator, denominator):
    """Safely divides two numbers, returning None if division by zero is attempted."""
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return result
    except ValueError:
        return("Error: Please enter numeric values only.")
      
  
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")
        


        