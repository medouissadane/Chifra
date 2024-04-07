import string
alpha_lower=string.ascii_lowercase
alpha_upper=string.ascii_uppercase

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def chifra(user_word,n):
    chifra_word=[]
    for letter in user_word:
        # **********************************************
        if letter in alpha_lower:
            
            index_latter=alpha_lower.index(letter)
            new_index=index_latter+n

            if new_index>25:
                chifra_word.append(alpha_lower[index_latter+(n-1)-25])
                
            else:
                chifra_word.append(alpha_lower[new_index])


        # **********************************************
        elif letter in alpha_upper:
            
            index_latter=alpha_upper.index(letter)
            new_index=index_latter+n

            if new_index>25:
                chifra_word.append(alpha_upper[index_latter+(n-1)-25])
                
            else:
                chifra_word.append(alpha_upper[new_index])

        else:
            chifra_word.append(letter)

    print("".join(chifra_word))

user_word=input("Enter a message: ")
n=int(input("dakhal lcod: "))

chifra(user_word,n)  