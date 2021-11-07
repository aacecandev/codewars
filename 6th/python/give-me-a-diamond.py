def n % 2 == 0 or n < 0: return None 
    result = [("*" * i + '\n') if i == n else ('*' * i).center(n).rstrip() + '\n' for i in range(1,n+1,2)]
    return ''.join(result + list(reversed(result[:-1])))
