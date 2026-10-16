# Reflection Questions

1. Why must a loop variable often be updated inside a while loop?

        We must update a loop variable inside a while loop to prevent an infinite loop otherwise the loop
        will run infinite time at the same value.

2. Can a while loop execute zero times? Give an example from this worksheet.

        Yes, the while loop can execute zero times.
        '''
        Ex) count = 7

        while count < 5:
            print("Hello")
            count += 1

        print("Finished")
        '''

3. What is the difference between updating a variable before print() and after print()?

        When you update a variable before print the loop will print new (updated) value but when you print
        the value before updating it, loop will print the previously stored value.

4. How can you recognize a possible infinite loop by reading the code?

        If the loop doesn't updates it's value in it's body or it's variable moves away from end value, I 
        can recognize it as possible infinite loop.

5. Why should you trace the condition again after every update?

        We should always trace the condition again after every update to prevent infinite loops.
