try:
    file_name = input("enter the name of the file: " "")
    with open(file_name, 'r') as file:
        data = file.read()
        print(data)
        count = len(data.split())   
        print(f"Number of words: {count}")
        upper = data.upper()
        print("Uppercase version:", upper)
    
    
    with open("output.txt", 'w') as output_file:
        output_file.write(f"Number of words: {count}\n")
        output_file.write(f"Uppercase version: {upper}\n")

except FileNotFoundError:
    print("file not found ")

finally:
    file.close()    
       