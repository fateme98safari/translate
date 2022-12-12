import gtts

def read_from_file():
    global words_bank
    f=open("my-project\session8\Translate.txt" , "r")
    temp=f.read().split("\n")
    words_bank=[]
    for i in range(0,len(temp),2):
        my_dict={'en':temp[i] , 'fa':temp[i+1]}
        words_bank.append(my_dict)
        print(words_bank)
    f.close()
    
def show_menu():
    print("welcome to my Translator")
    print("1- Translate En to Fa")
    print("2- Translate Fa to En")
    print("3- Add new word to database")
    print("4- Exit")
    
def translate_en_to_fa():
   translate=[]
   words_bank=[]
   result=[]
   user_text=input("write your English text: ")
   user_words=user_text.split(".")
   for i in user_words:
    w = i.split(" ")
    result= result + w
   print(result)
   for user_word in result:
      for word in words_bank:
       print(user_word)
       print(word)
       if user_word==word['en']:
            print(word['fa'])
            translate=word['fa'] + translate
            break
     else:
        print(user_word)
     x=gtts.gTTS(translate , lang = "ar" , slow=False)
     x.save("session8/favoice.mp3")

   

def translate_fa_to_en():
    translate=[]
    user_text=input("write your farsi text: ")
    user_words=user_text.split(".")
    for i in user_words:
        w=i.split(" ")
        result= result+w
    for user_word in result:
       for word in words_bank:
          if word['fa']==user_word:
            print(word['en'])
            translate= translate + word['en']
            break
    else:
           print(word['en'])
    x1=gtts.gTTS(translate , lang = "en" , slow=False)
    x1.save("session8/favoice.mp3")

def Add_new_word_to_database():

    new_word_en=input("enter new word in English: ")
    new_word_fa=input("enter new word in Farsi: ")
    f=open("my-project\session8\Translate.txt" , "a")
    f.write(new_word_en)
    f.write("\n")
    f.write(new_word_fa)
    f.close()
    

while 1==1:  

        show_menu()

        user_choice=int(input("select of this menu: "))
        if user_choice==1:
           translate_en_to_fa()

        elif  user_choice==2:
            translate_fa_to_en()

        elif user_choice==3:
            Add_new_word_to_database()

        elif user_choice==4:
            exit(0)