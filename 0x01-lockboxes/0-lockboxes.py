#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    m = len(boxes)
    visible_boxes = set([0])
    notVisible_boxes = set(boxes[0]).difference(set([0]))
    while len(notVisible_boxes) > 0:
        boxIdx = notVisible_boxes.pop()
        if not boxIdx or boxIdx >= m or boxIdx < 0:
            continue
        if boxIdx not in visible_boxes:
            notVisible_boxes = notVisible_boxes.union(boxes[boxIdx])
            visible_boxes.add(boxIdx)
    return m == len(visible_boxes)