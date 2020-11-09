class Decipher:

    def __init__(self, message=""):  # initialising an empty string message
        self.message = message

    def getMessage(self):
        return self.message

    def messageFind(self, filename):
        """
        Algorithm:
        Open the file that is passed and read the characters line by line. A check to include only characters between a to z and A to Z, considering the sensitivity.
        When a new line is found using ascii code the word id concatenated to string 1 and the rest of the characters in the new line are concat to string 2.
        A maximum number function is created to find the max between two numbers. Then the function to find the lcs is created where first the m and n are set to the length
        of the strings. Then a loop is started to fill up the dynamic programming table, matrix is set using the length of the two string. Then the base case is set where the
        first row and column is set to 0. Then there is a check to see whether the characters are the same, if same then the table is filled with 1 + the value at the cross,
        and if the characters do not match then add the maximum of the value above or to the left. Then the sequence itself is reached by backtracking through the table.
        The i and j are set to the lengths of the strings, then a while loop is executed, and checks if the two characters are the same then, concat it to the empty string and
        decrement the i and j counter to go cross, else choose a path where the value is larger. The message is stored in the instance variable created.
        :param filename: file that is passed to the function
        precondition: a text file
        post-condition: message stored in an instance variable
        Time Complexity: O(nm) worst case, where m is the length of string 1 and n is the length of string 2
        Space complexity: O(nm) worst case, where m is the length of string 1 and n is the length of string 2
        :return: no return
        """
        with open(filename, 'r') as encryptedFile:  # opening the file
            readFile = encryptedFile.read()  # read the file

        mainString = ''  # empty string to store the characters from the file
        newString = ''  # temporary empty string
        str1 = ''  # split the words
        str2 = ''  # split the words

        for line in readFile:  # concatenating the lines of the file. O(N)
            mainString += line
        for character in range(len(mainString)):  # looping through the main string. O(mn)
            if 97 <= ord(mainString[character]) <= 122 or 65 <= ord(
                    mainString[character]) <= 90:  # checking if the character is alphabets only
                newString += mainString[character]  # concatenating to a temp string
            if ord(mainString[character]) == 10:  # checking for a new line
                str1 += newString  # concat the characters before the new line
                newString = ''  # initialise the string to empty
        if len(newString) != 0:  # concat the last word in to str2 if it is not empty
            str2 += newString

        def max_num(a, b):  # created a function to find the maximum number. o(n)
            if a > b:
                return a
            return b

        def lcs(first, second):  # function to find the longest common subsequence

            """
            Algorithm: The function takes in two string and finds the length of the strings. Then the matrix is created, then a loop starts to fill the table in bottom up way.
            The position of up, left and cross are initialised. Then the base case is defined. If there is a match in words add one to the value of the cross, else take the max
            of the left or up on the current position. Then the sequence itself is reached by backtracking through the table. The i and j are set to the lengths of the strings,
            then a while loop is executed, and checks if the two characters are the same then, concat it to the empty string and decrement the i and j counter to go cross,
            else choose a path where the value is larger. The message is stored in the instance variable created.
            :param first: string 1
            :param second: string 2
            precondition: two strings
            post-condition: returns the lcs
            Time Complexity: O(nm) worst case, where m is the length of string 1 and n is the length of string 2
            Space complexity: O(nm) worst case, where m is the length of string 1 and n is the length of string 2
            :return: returns string of lcs
            """

            m = len(str1)  # assigned m to length of the first string
            n = len(str2)  # assigned n to length of the second string
            matrix = []  # empty list to create the matrix

            for i in range(m + 1):  # creating the matrix
                row = []  # empty list to append
                for j in range(n + 1):
                    row.append(0)  # append the row to the size required
                matrix.append(row)

            for i in range(m + 1):  # loop to fill the matrix in bottom up way
                for j in range(n + 1):

                    up = matrix[i - 1][j]  # reach the above matrix
                    left = matrix[i][j - 1]  # reach the matrix left
                    cross = matrix[i - 1][j - 1]  # reach the cross of matrix

                    if i == 0 or j == 0:  # base case
                        matrix[i][j] = 0
                    elif first[i - 1] == second[j - 1]:  # if there is a match then
                        matrix[i][j] = 1 + cross  # take one and add to the value of the cross
                    else:
                        matrix[i][j] = max_num(up,
                                               left)  # if no match then take the max of the previous row or previous column

            message = ''  # empty string to store the sequence
            i = m  # setting i to len of str1
            j = n  # setting j to length of str2
            while i > 0 and j > 0:
                if first[i - 1] == second[j - 1]:  # if there is a match
                    i -= 1
                    j -= 1
                    message = first[i] + message  # concat the character to the message
                elif matrix[i - 1][j] > matrix[i][
                    j - 1]:  # if the characters not same then approach the larger value path
                    i -= 1  # move a row up
                else:
                    j -= 1  # move a column left
            return message

        self.message = lcs(str1, str2)  # store the message in the instance variable

        # basic backtracking idea only referenced from https://www.geeksforgeeks.org/printing-longest-common-subsequence/

    def wordBreak(self, filename):
        """
        Algorithm:
        The dictionary file is first read and then the words are concatenated as a main string. It is pre processed according to the characters from A to Z and a to z.
        then the words are concat to the temp string. From the temp string, it checks if there is a new line if a new line is found it appends the word to the empty list,
        the temp list is initialised to empty. Then the loop goes through till the last word is appended to the list. The length of the message and and the longest word
        in the dictionary is assigned. The matrix is created where the rows are the length of the message and the columns are the length of the longest word in the dictionary.
        The loop is started on the length of message and the length of the longest word in dictionary. On every iteration a set of word is  checked through slicing to the dictionary
        file if there is a match "1" is set to the matching position else a "0" is set if no match is found. The negative start is possible when extracting the start of the message
        to avoid it a "0' is set to the matrix. The backtracking basically looks from the last row if there is a "1" initialised it looks for the start and stop index and concats that
        word to the final string, then it initialises the temp string back to empty for the new word. If the word is not matching to the dictionary the extra words are added after the flag
        to the final string, since the algorithm was concatenating empty string at the end so I did length -1 to avoid the empty string

        precondition: reads in the dictionary text file
        post-condition: stores the message
        :param filename: a text file which is passed to the function
        Time Complexity: O(kM.NM) where k is the length of the message, M is the length of the longest word in dictionary and N are the words in the dictionary.
        Space Complexity: O(kM) where k is the length of the message and M is the length of the longest word in the dictionary.
        :return: no return
        """

        with open(filename, 'r') as encryptedFile:  # opening the file
            readFile = encryptedFile.read()  # read the file

        mainString = ''  # empty string to store the characters from the file
        newString = ''  # temporary empty string
        myList = []  # split the words

        for line in readFile:  # concatenating the lines of the file. O(N)
            mainString += line
        for character in range(len(mainString)):  # looping through the main string. O(mn)
            if 97 <= ord(mainString[character]) <= 122 or 65 <= ord(
                    mainString[character]) <= 90:  # checking if the character is alphabets only
                newString += mainString[character]  # concatenating to a temp string
            if ord(mainString[character]) == 10:  # checking for a new line
                myList.append(newString)  # concat the characters before the new line
                newString = ''  # initialise the string to empty
        if len(newString) != 0:  # concat the last word in to str2 if it is not empty
            myList.append(newString)

        message = self.message  # assigning message

        k = len(message)  # length of the message
        m = max(len(w) for w in myList)  # length of the longest word in the dictionary file
        matrix = []

        for i in range(k):  # creating the matrix
            row = []  # empty list to append
            for j in range(m + 1):
                row.append(0)  # append the row to the size required
            matrix.append(row)

        for i in range(k):  # filling the matrix table starting with the length of the message
            for j in range(1,
                           m + 1):  # second counter j which loops from 1 to the length of the longest word in dictionary

                start = (i + 1) - j
                end = i + 1
                # slicing = substring(start, end)
                slicing = message[
                          start:end]  # slicing the string to get the sets of values to be checked with the dictionary file
                if start >= 0:  # start of the index could be negative so only positive start is considered
                    if slicing in myList:  # searching for the current set of strings in dictionary if they are present
                        matrix[i][j] = 1  # if a match is found then the matrix gets updated to 1
                    else:
                        matrix[i][j] = 0  # if no match is found in the dictionary then the matrix is updated to 0
                else:
                    matrix[i][j] = 0  # if the start is with negative then set the current position to 0

        mainList = []

        row = len(message) - 1
        final = ""
        temp = ""
        while row >= 0:                                     # starts a while loop on the row
            flag = True                                     # starts a flag for thw words nor stored
            for col in range(len(matrix[row])-1, -1, -1):     # it starts from the last column to the first row
                if matrix[row][col] == 1:                   # if the matrix has word stored
                    if len(temp) != 0:
                        final = temp + " " + final          # append the word in the final string
                        temp = ""                           # empty the string for next word
                    start = row - col + 1                   # to get the start index of the word
                    end = row + 1                           # to get the end index of the word
                    str = message[start:end]                # slicing the message
                    final = str + " " + final               # putting a space after word complete
                    mainList.append(str)
                    row -= col                              # decrementing the row
                    flag = False
                    break
            if flag:                                        # if words not stored in matrix
                start = row
                end = row + 1
                temp = message[start:end] + temp            # append the word not in the matrix
                row -= 1                                    # decrement the row
        if len(temp) != 0:
            final = temp + " " + final                      # append the word in the final string

        self.message = final[0:len(final)-1]                # since the last character appending is an empty string


if __name__ == "__main__":
    # fileName = "encrypted_2.txt"
    # function1 = Decipher()
    # function1.messageFind(fileName)
    # newFile = "dictionary_2.txt"
    # function1.wordBreak(newFile)

    inputFile = "encrypted.txt"                                                                   # opening the input file
    dictionaryFile = "dictionary.txt"                                                             # opening the dictionary file
    print("The name of the file, contains two encrypted texts : " + inputFile)                    # Initial output for input file
    print("The name of the dictionary file : " + dictionaryFile)                                  # initial output for the dictionary file
    print("---------------------------------------------------------------------")
    function = Decipher()
    function.messageFind(inputFile)
    print("Deciphered message is " + function.message)                                            # printing the instance variable stored
    try:                                                                                          # try and except on file not found
        function.wordBreak(dictionaryFile)
        print("True message is " + function.message)
    except FileNotFoundError:
        print("True message is " + function.message)
    print("---------------------------------------------------------------------")
    print("Program end")
