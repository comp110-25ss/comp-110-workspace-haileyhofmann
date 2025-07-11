"""Practicing user input, elif, and variable assignments."""

forecast: str = input("What is the weather?")
if forecast == "rainy":
    print("Bring a jacket.")
else:
    if forecast == "sunny":
        print("Bring sunglasses.")
    else:
        print("I don't have any advice for you :)")
