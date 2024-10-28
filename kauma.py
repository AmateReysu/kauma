import json
import base64

def block2poly(uid, args):
    
    coefficients = []
    
    decoded_bytes = base64.b64decode(args)
    decoded_bits = ''.join(format(byte, '08b') for byte in decoded_bytes)
    print(len(decoded_bits))
    print(decoded_bits)
    for i in range(0, len(decoded_bits)):
        if decoded_bits[i] == "1":
            coefficients.append((8*(i//8)) + (7 - i%8))
    return {uid: {"coefficients":coefficients}}
            

with open("tests.json", "r") as file:
    data = json.load(file)

if __name__ == "__main__":
    test_cases = data.get("testcases", {})
    output = {"responses":{}}
    
    for t in test_cases:
        result = block2poly(t, test_cases[t]["arguments"]["block"])
        print(result)
        output["responses"].update(result)
        
with open("output.json", "w") as file:
    json.dump(output, file, indent=4)