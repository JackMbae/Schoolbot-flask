from school_bot import get_school_response

def run_chat():
    print("SchoolBot: Hello! I can help you with school-related questions. Type 'exit' to quit.")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            print("SchoolBot: Goodbye!")
            break
        response = get_school_response(msg)
        print("SchoolBot:", response)

if __name__ == "__main__":
    run_chat()
