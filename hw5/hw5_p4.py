##統計116
##鄭雅云 H24126078


def is_balanced_parentheses(expression):
    """檢查括號的數量有沒有match"""
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def contains_unsupported_characters(expression):
    """檢查有沒有非法(?)的符號"""
    allowed_chars = "0123456789+-*/() "
    for char in expression:
        if char not in allowed_chars:
            return True
    return False

def evaluate_expression(expression):
    """處理主要的算式"""
    try:
        # 處理括號不平衡
        if not is_balanced_parentheses(expression):
            return "Error: Unbalanced parentheses."
        
        # 處理符號不合法
        if contains_unsupported_characters(expression):
            return "Error: Unsupported character in expression."
        
        # 處理數字符號匹配問題(就符號前後要有數字)
        previous_char = None
        for char in expression:
            if char in "+-*/" and (previous_char in "+-*/" or previous_char is None):
                return "Error: Operand error. Please check the expression syntax."
            previous_char = char if char != ' ' else previous_char
        
        # 終於可以算結果了，而且竟然有eval這個神奇的函數
        result = eval(expression)
        return result
    
    except ZeroDivisionError:
        return "Error: Division by zero."
    except SyntaxError:
        return "Error: Operand error. Please check the expression syntax."
    except Exception as e:
        return f"Error: {str(e)}"

def main(): ###主程式
    print("Arithmetic Expression Evaluator")
    print("Enter 'q' to quit.")
    
    while True:
        expression = input("Enter an expression: ").strip()
        
        if expression.lower() == 'q':  ###加入.lower()後，大寫Q也可以離開程式
            print("Quitting the program.")
            break
        
        result = evaluate_expression(expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()