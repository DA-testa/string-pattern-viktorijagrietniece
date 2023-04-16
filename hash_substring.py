# python3

def read_input():
  
    input_type = input().rstrip()
    
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
        return (pattern, text)
    
    elif input_type == 'F':
        with open("tests/06", "r") as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
        return (pattern, text)
    
    else:
        print("error")
        return
   
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    occurrences = []
    
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i : i + pattern_len]:
            occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = hash(text[i + 1 : i + pattern_len + 1])
    return occurrences
   
    
  

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
