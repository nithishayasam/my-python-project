# an encryption method that shifts the letters of the alphabet by a certain number of positions
# encrypts and decrypts messages with colored output, session history , and file saving capabilities
from colorama import Fore, Style, init
init(autoreset=True)
session_history = []


def encrypt(message, shift):
    result= ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit():
            result += chr((ord(char) - ord('0') + shift) % 10 + ord('0'))   
        else:
            result += char
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

def brute_force(message):
    results = []
    print(Fore.CYAN + "Brute Force Results:")
    for shift in range(1,26):
        print(Fore.YELLOW +f"Shift{shift}:{decrypt(message,shift)}")  

def save_to_file():
    if not session_history:        
        print(Fore.RED + "No session history to save.")
        return
    try:
        with open("cipher_history.txt","w") as f:
            f.write("=== Caesar Cipher Session History ===\n\n")
            for entry in session_history:
                f.write(f"{entry}\n")
        print(Fore.GREEN + "Session history saved to 'cipher_history.txt' successfully!")
    except Exception as e:
        print(Fore.RED + f"Error saving session history: {e}")

def show_history():
    if not session_history:
        print(Fore.RED + "No session history found.")
        return
    print(Fore.CYAN + "\n Session History:")
    for entry in session_history:
            print(Fore.YELLOW + entry)      


def get_shift():
    while True:
        try:
            shift=int(input(Fore.WHITE + "Enter the shift value (1-25): "))                    
            if 1 <= shift <= 25:
                return shift
            else:
                print(Fore.RED + "Invalid input! Please enter a number between 1 and 25.")
        except ValueError:        
            print(Fore.RED + "Invalid input! Please enter a valid number.")
def get_choice():
    while True:
            answer= input(Fore.WHITE +"Do you want to (E)ncrypt, (D)ecrypt, or (B)rute force? ").strip().upper()
            if answer in ['E','D','B']:
                return answer
            else:
                print(Fore.RED + "Invalid choice! Please enter E, D, or B.")

def get_yes_no(prompt):
    while True:
        answer = input(Fore.WHITE + prompt).strip().lower()
        if answer in ['yes',"no"]:
            return answer
        print(Fore.RED + "Invalid input! Please enter 'yes' or 'no'.")

if __name__ == "__main__":                   
     print(Fore.CYAN + Style.BRIGHT + "==== welcome to caesar cipher====")
     while True:
         print()
         try:
             message = input(Fore.WHITE + "Enter your message: ").strip()

             if not message:
               print(Fore.RED + "Message cannot be empty! Please enter a valid message.")
               continue 

             choice = get_choice()
             if choice == "B":
                 brute_force(message)
                 session_history.append(f"Brute Force:|Message: {message}")
             else:
                 shift = get_shift()
                 if choice == "E":
                     result = encrypt(message, shift)
                     print(Fore.GREEN + f"Encrypted Message: {result}")
                     session_history.append(f"Encrypted:|Message: {message}|Shift: {shift}|Result: {result}")
                 elif choice == "D":             
                        result = decrypt(message, shift)
                        print(Fore.GREEN + f"Decrypted Message: {result}")
                        session_history.append(f"Decrypted:|Message: {message}|Shift: {shift}|Result: {result}")
             print()
             show_history()
         except KeyboardInterrupt:
             print(Fore.RED + "\nInterrupted!")
             break    
         except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")
            continue
         print()
         again = get_yes_no("Do you want to perform another operation? (yes/no): ")
         if again == "no":
             save = get_yes_no("Do you want to save the session history? (yes/no): ")
             if save == "yes":
                save_to_file()
             print(Fore.CYAN + "Thank you for using the Caesar Cipher! Goodbye!") 
             break 