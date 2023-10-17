def start(llm_chain):
    choice = "start"

    while True:
        try:
            response = llm_chain.predict(human_input=choice)

            if not "RateLimitError" in response:
                print(response.strip())

            if "The End." in response:
                break

            choice = input("Your reply: ")
        except KeyboardInterrupt:
            break

    print("End game.")
    print("Thank you for playing!")