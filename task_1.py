def remove_parentheses(text):
    result = ""
    is_inside = False
    for i in range (len(text)-1:
        if text[i] == '(':
            is_inside = True
            result += ''
        elif text[i] == ')' and text[i+1] == " ":
            is_inside = False
        elif not is_inside:
            result += letter
    return result
            
    
text = "(Nie) jest tak zle"
print (remove_parentheses(text))
