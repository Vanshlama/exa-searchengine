from exa_py import Exa

# Initialize Exa with your API key
exa = Exa("API_KEY=sk-12345_your_real_key_here")

# Run the program in a continuous loop so you can search multiple times
while True:
    query = input("Search here (or type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break
    # Make a search request to Exa
    response = exa.search(
        query,
        num_results=5
    )
    # Loop through the results and print only Title + URL
    for result in response.results:
        print(f"Title: {result.title}")
        print(f"URL: {result.url}\n")
