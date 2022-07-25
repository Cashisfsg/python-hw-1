import sys

def calculate():
    try:
        operators = ['+', '-', '*', '/']

        float(sys.argv[1])
        float(sys.argv[3])

        if sys.argv[2] not in operators:
            raise ArithmeticError

        if len(sys.argv) > 4:
            raise AttributeError

        exp = ''
        for i in range(1, len(sys.argv)):
            exp += sys.argv[i]

        ans = eval(exp)
        print(ans)

        return ans

    except ValueError:
        print('Invalid expression')
        return -1
    except ArithmeticError:
        print('Expression must contain only "+", "-", "*" or "/"')
        return -1
    except AttributeError:
        print('Expression must contain only 3 parameters')
        return -1

if __name__ == '__main__':
    calculate()