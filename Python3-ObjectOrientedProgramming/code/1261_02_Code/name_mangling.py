class SecretString:
    '''A not-at-all secure way to store a secret string.'''

    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase

    def decrypt(self, pass_phrase):
        '''Only show the string if the pass_phrase is correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return ''

def main():
    secret_string = SecretString("ACME: Top Secret", "antwerp")
    print(secret_string.decrypt("antwerp"))
    print(secret_string.__plain_string)
if __name__ == "__main__":
    main()