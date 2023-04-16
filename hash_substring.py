# python3

def read_input():
  
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open("tests/06", "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
        return (pattern, text)
    
    else:
        print("error")
        retur n
   
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i : i + pattern_len]:
            occurences.append(i)
        if i < text_len - pattern_len:
            text_hash = hash(text[i + 1 : i + pattern_len + 1])
    return occurences
   
    
  

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
