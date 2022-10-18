
def test(string: str):
    if len(string) == 1:
        return string[0]
    return test(string[1:]) + string[0]


print(test('Yago'))
