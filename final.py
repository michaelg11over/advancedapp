COINS = {
    "penny": 1, "pennies": 1,
    "nickel": 5, "nickels": 5,
    "dime": 10, "dimes": 10,
    "quarter": 25, "quarters": 25
}

#coverts
def convert(sentence):
    words = sentence.lower().split()
    amount = 0
    for i in range(len(words)):
        if words[i] in COINS:
            amount += int(words[i - 1]) * COINS[words[i]]
    return f'{amount / 100:.2f}'
 
#test each input
test_cases = [
    ("1 penny and 2 nickels", "0.11"),
    ("4 dimes and 7 quarters", "2.15"),
    ("1 quarter and 3 pennies", "0.28"),
    ("21 pennies and 17 dimes and 52 quarters", "14.91"),
    ("95 dimes and 73 quarters and 22 nickels and 36 pennies", "29.21"),
    ("1 nickel and 17 quarters", "4.30"),
    ("21 nickels and 15 pennies", "1.20"),
    ("1 dime and 1 nickel and 1 penny and 1 quarter", "0.41"),
]
#tells if its passed or failed
for sentence, expected in test_cases:
    result = convert(sentence)
    status = "PASS" if result == expected else "FAIL"
    print(f"[{status}] {sentence} -> {result}")