def main():
    
    print ("--- Begin the report of books/frankenstein.txt ---")

    print ("Checking the book length...")

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        print (f"This book has {len(words)} words.")

    print ("")
    print ("See the character counts below...")

    charcount_dict = {}
    file_contents_lowercase = file_contents.lower()

    def count_chars(analyzed_text):
        for character in analyzed_text:
            if character not in charcount_dict:
                charcount_dict[character] = 1
            else:
                charcount_dict[character] += 1       

    count_chars(file_contents_lowercase)

    # print (charcount_dict)

    charcount_list = []

    for char in charcount_dict:
        if char.isalpha() == True:
            count = charcount_dict[char]
            single_dict = {
                "char": char,
                "count": count
                }
            charcount_list.append(single_dict)

    def sort_on(dict):
        return dict["count"]
    
    charcount_list.sort(reverse=True, key=sort_on)

    for dict in charcount_list:
        print (f"The < {dict['char']} > character was found {dict['count']} times.")

main()