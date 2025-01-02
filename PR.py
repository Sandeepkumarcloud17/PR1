# File creation script
def create_file(file_name, content):
    try:
        # Open the file in write mode (it will create the file if it doesn't exist)
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"File '{file_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    file_name = "example.txt"  # Specify the file name
    content = "Hello, this is a test file created using Python!\nHappy coding!"
    create_file(file_name, content)
