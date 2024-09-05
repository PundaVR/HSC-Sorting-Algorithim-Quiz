# HSC-Sorting-Algorithim-Quiz
This program tests your knowledge of Bubble, Insertion, and Selection Sorting Algorithims in the same format as the HSC
Still a **work in progress** however so far one style of HSC question out of the 4 are available

### DONE:
- Basic UI/Menu
- Questions:
    - What will the next pass look like
- Show score

### TODO:
- Questions:
    - What algorithim was used based on the example
    - At pass N what algorithim was used
    - Some Passes Completed what is next
- Settings
- Advanced Options (hard mode, array length, question amount)

### BUGS:
- Sometimes answers can be duplicates
- I think some of the sorting algos might be a bit bugged


## HSC Course Specs
### Bubble Sort
```
BEGIN BubbleSort
    Let Last = number of names in the array
    Let Swapped = true
    WHILE Swapped = true
        Let Swapped = false
        Let i = 1
        WHILE i < Last
            IF Name (i) > Name (i+1) THEN
                Swap (Name (i), Name (i+1))
                Let Swapped = true
            ENDIF
            Increment i
        ENDWHILE
        Decrement Last
    ENDWHILE
END BubbleSort 

BEGIN Swap (A, B)
    Let Temp = A
    Let A = B
    Let B = Temp
END Swap 
```
### Selection Sort
```
BEGIN SelectionSort
    Let EndUnsorted = number of names in the array
    WHILE EndUnsorted > 1
        Let i = 1
        Let Max = Name (i)
        Let PosMax = i
        WHILE i <= EndUnsorted
            Increment i
            IF Name (i) > Max THEN
                Let Max = Name (i)
                Let PosMax = i
            ENDIF
        ENDWHILE
        Swap (Name (PosMax), Name (EndUnsorted))
        Decrement EndUnsorted
    ENDWHILE
END SelectionSort


BEGIN Swap (A, B)
    Let Temp = A
    Let A = B
    Let B = Temp
END Swap 
```
### Insertion Sort
```
BEGIN InsertionSort
    Let First = 1
    Let Last = number of elements in the array
    Let PositionOfNext = Last – 1
    WHILE PositionOfNext >= First
        Let Next = Name (PositionOfNext)
        Let Current = PositionOfNext
        WHILE (Current < Last) AND (Next > Name (Current + 1))
            Increment Current
            Let Name (Current – 1) = Name (Current)
        ENDWHILE
        Let Name (Current) = Next
        Decrement PositionOfNext
    ENDWHILE
END InsertionSort 
```