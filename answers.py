def modify_file():
 
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the output file: ")
    
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        modified_content = content.upper()
        
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"File successfully modified and saved as {output_filename}")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{input_filename}'.")
    except IOError as e:
        print(f"An error occurred while handling the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    modify_file()
