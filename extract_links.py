from googlesearch import search

def google_search(query, num_results=5):
    try:
        # Perform a Google search and print the results
        for result in search(query, num_results=num_results):
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'YourQuery' with the actual query you want to search for
google_search('django')
