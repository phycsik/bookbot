def number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    character_counts = {}
    for ch in text:
        ch = ch.lower()
        if ch not in character_counts:
            character_counts[ch] = 0
        character_counts[ch] += 1    
        #get_character(ch)
    return character_counts

"""def get_character(ch):
    if character_counts[ch] == None:
        character_counts[ch] = 1
    else:   
        character_counts[ch] += 1
   #return character_counts"""

def split_dictionary(dictionary):
    #character_key = {}
    #character_count = {}
    character_total = {}
    char_list = []
    for key in dictionary:
            if key.isalpha() == True:
        #character_key["character:"] = key
        #character_count["count:"] = dictionary[key] 
        #character_total = [
           # {"character:" : key,
            #"count:": dictionary[key]}
                char_list.append({"character:": key, "count:": dictionary[key]})
    #sort_on(character_total)
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    #return character_key, character_count

def sort_on(dictionary):
    return dictionary["count:"]

#sort_on(character_count(split_dictionary(number_of_characters(get_book_text("books/frankenstein.txt")))))   
        
#character_count.sort(reverse=True, key=sort_on)

#d = {"a", 5}

#sort_on(d)

#print(number_of_characters("hello world"))