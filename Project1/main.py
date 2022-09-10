#Word puzzle game

wrong_word_set={'RAEHTF','KABRE','CYROTNU','RENEG','OAERELANP','WRDA','ASTR','PSTO'}
correct_word_set={'FATHER','BRAKE','COUNTRY','GREEN','AEROPLANE','DRAW','STAR','STOP'}

def check_word(input_word):
    user_score=0
    for word in correct_word_set:
        if input_word==word:
            print("\nCorrect\n")
            user_score=1
            break
    else:
        print("\nWrong\n")
        user_score=-1
    return user_score

user_score=0
word_count=0
print()
for word in wrong_word_set:
    print("Arrange the letters to form a valid word:")
    print(word)
    input_word=input().upper()
    user_score+=check_word(input_word)
    word_count+=1
    if word_count>=5:
        break
print("Net score is ",user_score)




