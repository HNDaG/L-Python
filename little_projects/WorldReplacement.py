def replace(str: str):
    string_to_replace = input("Str_to_replace: ")
    string_replacement = input("Str_replacment: ")
    
    str = str.replace(string_to_replace, string_replacement)
    print(str)



replace(input("Enter string: "))