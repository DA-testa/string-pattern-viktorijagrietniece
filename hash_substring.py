# python3

def read_input():
    pattern = ''
    text = ''
    input_type = input().rstrip()
    if input_type == 'i':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'f':
        with open("tests/06", "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
 
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    p = len(pattern)
    t = len(text)
    base = 256
    mod = 10**9 + 7
    hash_pattern = 0
    hash_text = 0
    power = 1
    
    for i in range(p):
       hash_pattern = (hash_pattern * base + ord(pattern[i])) % mod
       hash_text = (hash_text * base + ord(text[i])) % mod
       power = (power * base) % mod
    for i in range(t - p + 1):
         if hash_pattern == hash_text and text[i:i + p] == pattern.lower():
             occurrences.append(i)
         if i < t - p:
             hash_text = (base * (hash_text - ord(text[i]) * power) + ord(text[i + p])) % mod
             hash_text = (hash_text + mod) % mod
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
