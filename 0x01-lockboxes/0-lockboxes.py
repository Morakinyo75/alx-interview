def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    keys = boxes[0]
    for key in keys:
        if key < num_boxes:
            unlocked_boxes[key] = True

    for box_index in range(1, num_boxes):
        if not unlocked_boxes[box_index]:
            return False

        keys = boxes[box_index]
        for key in keys:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True

    return all(unlocked_boxes)

boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 2], [3], [4], [0]]
print(canUnlockAll(boxes))  # Output: False
