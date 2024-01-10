#!/usr/bin/python3
def canUnlockAll(boxes):
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = set()
    visited.add(0)  # The first box is unlocked

    box_stack = [0]  # Start with the first box
    while box_stack:
        current_box = box_stack.pop()

        for key in boxes[current_box]:
            if key < num_boxes and key not in visited:
                visited.add(key)
                box_stack.append(key)

    return len(visited) == num_boxes
