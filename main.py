from random import randint, shuffle
from math import floor

AppConfigs = {
    "debug": True
}

testedQuestions = []
testedResults = []


def BubbleSort(array:list):
    passes = []
    last = len(array)
    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < last-1: #-1 to now go overflow
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swapped = True
            i+=1
        last-=1
        if(AppConfigs["debug"]): print(f"Bubble Sort #{len(passes)+1}: {array}")
        passes.append(array.copy())
    return passes                


def InsertionSort(array:list):
    passes = []
    first = 1
    last = len(array)-1
    positionOfNext = last-1
    while positionOfNext >= first:
        next = array[positionOfNext]
        current = positionOfNext
        while (current < last) and (next > array[current+1]):
            current+=1
            array[current-1] = array[current]
        array[current] = next
        positionOfNext-=1
        if(AppConfigs["debug"]): print(f"Insertion Sort #{len(passes)+1}: {array}")
        passes.append(array.copy())
    return passes

def SelectionSort(array:list):
    passes = []
    endUnsorted = len(array)-1 #-1 to not go out of range
    while endUnsorted > 1:
        i = 0
        max = array[i]
        posMax = i
        while i < endUnsorted:
            i+=1
            if array[i] > max:
                max = array[i]
                posMax = i
        temp = array[posMax]
        array[posMax] = array[endUnsorted]
        array[endUnsorted] = temp
        endUnsorted -=1
        if(AppConfigs["debug"]): print(f"Selection Sort #{len(passes)+1}: {array}")
        passes.append(array.copy())
    return passes

#
## 
#

def Title(msg:str):
    len(msg.split())
    titleMarker = "============="
    print(f"\n{titleMarker[round(len(msg)/2):]} {msg} {titleMarker[round(len(msg)/2):]}")

def ValidateUserInputNumbers(userInput:str, maxMenuNumberOption:int, excludeZero = False):
    validInput = False
    if (userInput.isnumeric() and int(userInput) <= maxMenuNumberOption and int(userInput) >= 0):
        if(excludeZero and userInput=="0"):
            validInput = False
        else:
            validInput = True
    if(AppConfigs["debug"]): print(f"> validInput: {validInput}")
    return validInput

def GenerateRandomArray(length:int = 7):
    newArray = []
    for i in range(length):
        newArray.append(randint(0,99))
    if(AppConfigs["debug"]): print(f"> GenerateRandomArray: {newArray}")
    for i in range(5): shuffle(newArray) # obfuscate the array
    return newArray

def FormatArrayToStr(array:list):
    arrayStr = "|"
    for i in array:
        if i >= 10: arrayStr+=f" {i} |"
        else: arrayStr+=f"  {i} |"
    return arrayStr

def Correct(array:list):
    testedQuestions.append(array)
    testedResults.append(True)

def Incorrect(array:list):
    testedQuestions.append(array)
    testedResults.append(False)

def InputAnswer(answerNum:int, answer):
    print("0. Return to Menu")

    ans = input("Answer: ")
    while (ValidateUserInputNumbers(ans, 4) is False):
        ans = input("Invalid Input!\nAnswer: ")

    if ans == f"{answerNum}": return 1
    elif ans == "0": return 2
    else: return 0

def ShuffleAnswers(answers:list, answer:list):
    #shuffle(answers)

    
    dupAnswers = []
    checkIndex = 0
    for ans in answers:
        isDup = False
        for item in dupAnswers: 
            if ans != item: isDup=False
            else: isDup=True
        
        if isDup: 
            if AppConfigs["debug"]: print(f"SHUFFLING ANSWER DETECTED: {ans}")
            shuffle(ans)
            if AppConfigs["debug"]: print(f">>> {ans}")
            
        else: dupAnswers.append(ans)
            

        if ans == answer: shuffle(ans)
            #answers[checkIndex] = ans 
        

        checkIndex+=1
    
    return answers

def ShowAnswerOptions_ArrayContents(answerNum:int, array:list, passIndex:int, answer:list, useAlgo:int, hardMode):
    answers = []
    
    if useAlgo == 1: 
        answers.append(BubbleSort(array.copy())[passIndex+1])
        answers.append(InsertionSort(array.copy())[passIndex])
        answers.append(SelectionSort(array.copy())[passIndex])
    elif useAlgo == 2: 
        answers.append(BubbleSort(array.copy())[passIndex])
        answers.append(InsertionSort(array.copy())[passIndex+1])
        answers.append(SelectionSort(array.copy())[passIndex])
    elif useAlgo == 3: 
        answers.append(BubbleSort(array.copy())[passIndex])
        answers.append(InsertionSort(array.copy())[passIndex])
        answers.append(SelectionSort(array.copy())[passIndex+1])
    
    ShuffleAnswers(answers.copy(), answer.copy())
    if AppConfigs["debug"]: print(f"Correct answer: {answer}\nWrong answers: {answers}")
    answers.insert(answerNum-1, answer) #sometimes inserts answer into wrong pos???
    if AppConfigs["debug"]: print(f"Inserted correct answer at #{answerNum}:\n- {answers}")
    for i in range(len(answers)):
        print(f">>  {i+1}.      {FormatArrayToStr(answers[i])}")

def ShowAnswerOptions_AlgoType(answerNum:int, passes:list, useAlgo:int, hardMode):
    answers = []
    algorithms = ["Bubble", "Insertion", "Selection", "Binary", "Linear"]
    answer = algorithms[useAlgo-1]
    #order = ["from the right", "from the left"] # NEED TO IMPLEMENT INTO ALGOS
    if useAlgo == 1:
        answers.append(algorithms[1])
        answers.append(algorithms[2])
        answers.append(algorithms[randint(3,4)])
    elif useAlgo == 2:
        answers.append(algorithms[0])
        answers.append(algorithms[2])
        answers.append(algorithms[randint(3,4)])
    elif useAlgo == 3:
        answers.append(algorithms[0])
        answers.append(algorithms[1])
        answers.append(algorithms[randint(3,4)])
            
    if AppConfigs["debug"]: print(f"Correct answer: {answer}\nWrong answers: {answers}")
    answers.insert(answerNum-1, answer) #sometimes inserts answer into wrong pos???
    if AppConfigs["debug"]: print(f"Inserted correct answer at #{answerNum}: {answers}")
    for i in range(len(answers)):
        print(f">>  {i+1}. {answers[i]}")#{FormatArrayToStr(answers[i])}")

        
def ShowAnswerOptions_NextPass(answerNum:int, array:list, passes:list, useAlgo:int, hardMode):
    pass
#
##
#

def Question_AtPassN(answerNum:int, array:list, passes:list, useAlgo:int, hardMode:bool):
    # show unsorted array
    # show array at a random pass
    # show array at an even later pass
    # ask which sort method was beind used (i.e. Insertion Sort (from the right)
    
    passX = randint(1, floor(len(passes)/2))
    passY = randint(floor(len(passes)/2)+1, len(passes)-1)
    if AppConfigs["debug"]: print(f"random pass value: X={passX}, Y={passY}")
    print(f"This table shows the intial contents of an array and the contents \nafter some passes of a valid sorting procedure.")
    print(f"> Initial:  {FormatArrayToStr(array)}\n> Pass X{passX}:  {FormatArrayToStr(passes[passX])}\n> Pass Y{passY}:  {FormatArrayToStr(passes[passY])}")
    print("Which sorting algorithim was used?")
    ShowAnswerOptions_AlgoType(answerNum, passes[1], useAlgo, hardMode)
    result = InputAnswer(answerNum, array)
    
    algo = "null"
    if useAlgo == 1: algo = "Bubble Sort"
    elif useAlgo == 2: algo = "Insertion Sort"
    elif useAlgo == 3: algo = "Selection Sort"
    print(f">> This question used the {algo} algorithim <<") 
    if result == 0: print(f"❌ Wrong! Answer was {answerNum}.")
    elif result == 1: print("✅ Correct!")
    return result


    


def Question_NextPass(answerNum:int, array:list, passes:list, useAlgo:int, hardMode:bool):
    # show unsorted array
    # show first pass
    # ask what is result of next pass

    print(f"This table shows the intial contents of an array and the contents \nafter one pass of a valid sorting procedure.")
    print(f"> Initial:  {FormatArrayToStr(array)}\n> 1st Pass: {FormatArrayToStr(passes[0])}")
    print("What are the contents of the array after the second pass?")
    ShowAnswerOptions_ArrayContents(answerNum, array.copy(), 1, passes[1], useAlgo, hardMode)
    result = InputAnswer(answerNum, array)

    algo = "null"
    if useAlgo == 1: algo = "Bubble Sort"
    elif useAlgo == 2: algo = "Insertion Sort"
    elif useAlgo == 3: algo = "Selection Sort"
    print(f">> This question used the {algo} algorithim <<") # somehow algo ges mixed up? says insertion instead of selection
    if result == 0: print(f"❌ Wrong! Answer was {answerNum}.")
    elif result == 1: print("✅ Correct!")
    return result


def Question_SomePassesCompleted(answerNum:int, array:list, passes:list, useAlgo:int, hardMode:bool):
    # Show array at a random pass
    # Ask which of the following is a possible result of the next pass
    nextPass = randint(1, len(passes)-2)

    print(f"This table shows an array after an unknown amount of passes with a sorting algorithim.")
    print(f"> Array:    {FormatArrayToStr(passes[nextPass])}")
    print("What are the contents of the array on the next pass?")
    ShowAnswerOptions_ArrayContents(answerNum, array, nextPass, passes[nextPass+1], useAlgo, hardMode)
    result = InputAnswer(answerNum, passes[nextPass+1])
    
    algo = "null"
    if useAlgo == 1: algo = "Bubble Sort"
    elif useAlgo == 2: algo = "Insertion Sort"
    elif useAlgo == 3: algo = "Selection Sort"
    print(f">> This question used the {algo} algorithim <<") # somehow algo ges mixed up? says insertion instead of selection
    if result == 0: print(f"❌ Wrong! Answer was {answerNum}.")
    elif result == 1: print("✅ Correct!")
    return result

def Question_TextBased():
    # After the first pass of a sort, only the last two elements of an array have changed value.
    # Which list identifies all the possible sort methods that could have been used?
    # A. Bubble, Selection
    # B. Bubble, Insertion
    # C. Insertion, Selection <-- ??? i think its this
    # D. Bubble, Selection, Insertion
    pass

def Question(question:int, array:list, hardMode:bool = False):
    result = 0 # 0=False, 1=True, 2=Quit
    answerNum = randint(1,4) 
    useAlgo = randint(1, 3) # NOTE: use 1 as bubble is known to work?
    useQuestion = randint(1,3) # not using 4 yet
    passes = []  
    if useAlgo == 1: passes = BubbleSort(array.copy())
    elif useAlgo == 2: passes = InsertionSort(array.copy())
    elif useAlgo == 3: passes = SelectionSort(array.copy())
    
    print(f"\nQ{question}")

    if useQuestion == 1: result = Question_AtPassN(answerNum, array.copy(), passes.copy(), useAlgo, hardMode)
    elif useQuestion == 2: result = Question_NextPass(answerNum, array.copy(), passes.copy(), useAlgo, hardMode)
    elif useQuestion == 3: result = Question_SomePassesCompleted(answerNum, array.copy(), passes.copy(), useAlgo, hardMode)

    if result!=2: input("Press ENTER to continue...")    

    return result
    
    


#
##
#

def ResetTest():
    testedQuestions.clear()
    testedResults.clear()


def StartTesting(questions:int=10, arrayLength:int=7, hardMode = False): 
    question = 0
    Title("Testing")
    ResetTest()
    isTesting = True
    if hardMode: arrayLength = 10
    while isTesting:
        question+=1
        questionArray = GenerateRandomArray(arrayLength)
        result = Question(question, questionArray, hardMode)

        if result != 2: testedQuestions.append(questionArray.copy())
        if result == 0: testedResults.append(False)
        elif result == 1: testedResults.append(True)
        else: 
            testedResults.append(False)
            isTesting = False

        if question >= questions: isTesting = False
        
        if isTesting is False:
            correctQ = 0
            for i in testedResults:
                if i: correctQ+=1
            Title("RESULTS")
            print(f"> Attempted: {len(testedQuestions)}\n> Correct: {correctQ}\n> OVERALL RESULTS: {correctQ}/{len(testedQuestions)} ({str((correctQ/len(testedQuestions))*100)[:5]}%)")

    
def DisplayResults(hardMode:bool):
    pass

def AdvancedStart(): 
    Title("Advanced Start")
    questionAmountInp = input("How many questions?       :  ")
    hardModeInp = input("Hard difficulty?    y/n   :  (NOT AVAILABLE)")
    questionArrayLengthInp = input("Array length of Questions :  ")


    input("Press ENTER to continue...")  
    StartTesting()

def Settings():
    pass

def Menu():
    while True:
        Title("HSC Sorting Algo Test")
        print("1. Quick Start")
        print("2. Advanced Start")
        print("3. Settings")
        print("0. Quit")
        inp = input("Select an option: ")
        while (ValidateUserInputNumbers(inp, 3) is False):
            inp = input("Invalid Input!\nSelect an option: ")

        # Using python 3.9 when making this so cant use a match statement :(
        if inp == "0": quit()
        elif inp == "1": StartTesting()
        elif inp == "2": AdvancedStart()
        elif inp == "3": Settings()
        

Menu()
#Question_NextPass(3, [57,23,66,99,34,7,43], InsertionSort([57,23,66,99,34,7,43]), 2, False)
#answers = [[1,5,3,1,5],[1,3,7,1,5],[1,3,7,1,5],[3,9,5,8,1]]
#answer = [1,5,3,1,5]
#print(answers)
#answers = ShuffleAnswers(answers.copy(), answer)
#print(answers)