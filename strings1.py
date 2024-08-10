#lex_auth_012693825794351104168
def find_common_characters(msg1,msg2):
    #Remove pass and write your logic here
    common = ""
    for alpha in msg1:
        if alpha in msg2 and alpha not in common:
            common += alpha
    return common

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)