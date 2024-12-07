import sys
from request import *

def main():
    print("Witaj na ziemiach murgrabii")
    if(len(sys.argv) == 2):
        print("O prosze! Masz klucz api a wiec zapraszam")
        send_request(sys.argv[1]) 
    else:
        print("Bez Api klucza nie masz tu wladzy, precz!")         

if __name__ == "__main__":
    main()
