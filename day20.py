def insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return
    top = stack.pop()
    insert_sorted(stack, element)
    stack.append(top)
def sort_stack(stack):
    if not stack:
        return
    top = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, top)
user_input = input("Enter stack elements separated by spaces: ")
stack = list(map(int, user_input.split()))
sort_stack(stack)
print("Sorted stack:", stack)