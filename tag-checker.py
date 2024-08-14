"""
Tag Checker Problem
Author: Fiona Marie Bautista
Date: 14/08/2024
------------------------------
> Description:
    A program that checks whether a given paragraph is tagged correctly. 

> Input:
    A paragraph of text (single line)

>Output:
    - For Correctly tagged paragraphs: "Correctly tagged paragraph"
    - For Incorrectly tagged paragraphs: "Expected <expected tag> found <unexpected tag>"

> Constraints:
    - valid tags are denoted by angular brackets with a single uppercase character, e.g. <A> and </A>,
        other variants will be ignored.

> Assumptions:
    - An input is defined as a single line of text despite the length.
    - A collection of inputs is delimited by newline characters.
    - The input paragraph can contain other symbols encased in angular brackets that 
        will not be considered valid tags.
    - The input paragraph has at least one valid tag.
    - A tag does not enclose null content, e.g. <A> Hi! </A> is valid, <A></A> is not.
    - Valid tags will not contain attributes, e.g. <A id="1"></A>
    - The tag checker outputs the first mismatch found, 
        regardless of the length of the paragraph.
"""

import sys
import re

def tag_checker(tags):
    """
    This function checks the logical order of the valid tags found in a paragraph.

    Input: 
        tags (list): a list of valid tags in a paragraph
    Output:
        str: a message indicating whether the paragraph is correctly tagged or not
    
    """

    # We use a stack to keep track of the tags' chronology
    stack = []

    # Iterate through the list of tags
    for tag in tags:
        # if we encounter a closing tag, we check the following:
        if tag[0] == "/":
            # if the stack is not empty and the closing tag matches the last tag in the stack
            if stack and stack[-1] == tag[1]:
                stack.pop()
            # if the stack is empty, the closing tag is unexpected
            elif len(stack) == 0:
                return f"Expected # found <{tag}>"
            # if the closing tag does not match the last tag in the stack
            else:
                return f"Expected </{stack[-1]}> found <{tag}>"
        # if we encounter an opening tag, we add it to the stack
        else:
            stack.append(tag)
    # check if we have any tags left in the stack that were not closed
    if len(stack) > 0:
        return f"Expected </{stack[-1]}> found #"

    return "Correctly tagged paragraph"

# Read the input paragraph
input_paragraph = sys.stdin.readline().strip()

while input_paragraph != "":
    # the regex pattern will only match tags with singular uppercase letters enclosed in angular brackets
    tags = re.findall(r'(?<!<)<(/?[A-Z])>(?!>)', input_paragraph)

    # assures that the input paragraph has at least one valid tag
    if len(tags) > 0:
        print(tag_checker(tags))

    # get the next input
    input_paragraph = sys.stdin.readline().strip()
    