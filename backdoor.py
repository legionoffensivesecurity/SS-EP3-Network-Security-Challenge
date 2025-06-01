import subprocess

def execute_commands():
    """Executes commands received as input and prints the output."""
    print("AUTORIZED HACKERS ONLY!. Type 'exit' to quit.")

    while True:
        # Custom prompt
        command = input("hacked/$/>> ").strip()

        if command.lower() == "exit":
            print("DONE! Closing the shell...")
            break
        elif not command:
            continue
        else:
            try:
                # Execute the received command
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                output = result.stdout + result.stderr
                if not output:
                    print("Command executed successfully with no output.")
                else:
                    print(output)
            except Exception as e:
                print(f"Error: {str(e)}")

def main():
    execute_commands()

if __name__ == "__main__":
    main()
