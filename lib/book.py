class Book:
    """Represents a book with a title and page count."""

    def __init__(self, title: str, page_count: int):
    
        if not isinstance(page_count, int):
           print ("page_count must be an integer\n")
        elif page_count < 1:
            print ("page_count must be an integer\n")
        else:        
             self.title = title
             self.page_count = page_count

    def turn_page(self):
    
        print("Flipping the page...wow, you read fast!")
