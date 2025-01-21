def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"---- Begin report of {book_path} ----")
    getreport(text)
    print(f"---- End report ---")

def get_numwords(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["count"]

def get_characters(text):
    countchar = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in countchar:
                countchar[char] += 1
            else:
                countchar[char] = 1
    
    return countchar

def getreport(text):
    print(f"{get_numwords(text)} words found in the document\n")
    
    sortletterlist = []
    countchar = get_characters(text)
    for key in countchar:
        a = {'letter': key, 'count': countchar[key]}
        sortletterlist.append(a)
    
    sortletterlist.sort(reverse=True, key=sort_on)
    for i in sortletterlist:
        print (f"The '{i["letter"]}' character was found {i["count"]} times")
    

main()