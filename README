# Technical Test: Tag Checker
## Author: Fiona Marie Bautista
## Date: August 14, 2024

### Description
The following Python program checks for errors in paragraphs containing tags. A valid tag was defined to be a single uppercase character enclosed in angular brackets, paired with its closing tag denoted by a forward slash e.g. `<A> and </A>`.

The program outputs `Correctly tagged paragraph` if no errors were encountered. Otherwise, it prints `Expected <expected> found <unexpected>` for the first mismatch encountered in an input.

### Directory

- **tag-checker.py** is the script in Python
- **mytestcases** is a folder containing the sample inputs (**/tests-in**) and outputs (**/tests-out**)
- **myoutputs** is a folder containing the program outputs

### Running the Program
```
$ python tag-checker.py < [testcase filepath (.txt)] > [output filepath (.txt)]
```

*Example:*

```
$ python tag-checker.py < mytestcases/tests-in/sample.txt > myoutputs/sample-myout.txt
```

To compare the outputs,
```
$ diff [testcase output filepath (.txt)] [output filepath (.txt)]
```

*Example:*
```
$ diff mytestcases/tests-out/sample-out.txt myoutputs/sample-myout.txt   
```
**Note:** The program output contains an extra line at the end of the file.

### Assumptions Considered

- An input is defined as a single line of text of any length.
- A collection of inputs is delimited by newline characters.
- The input paragraph can contain other symbols encased in angular brackets that 
    will not be considered valid tags.
- The input paragraph has at least one valid tag.
- A tag does not enclose null content, e.g. `<A> Hi! </A>` is valid, `<A></A>` is not.
- Valid tags will not contain attributes, e.g. `<A id="1"></A>`
- The tag checker outputs the first mismatch found, 
    regardless of the length of the paragraph.

### Explanation of the Approach

When the program takes in an input, it uses the regex function `re.findall()` to filter out and capture the names of the valid tags, essentially resulting in a chronological list of their occurrence.

*Example*:
```
Input : "<A> This is a <B> fairly simple <//d> <*/> Example </B>! </A>"

Regex output: ['A', 'B', '/A', '/B']

```

At this point, we can simply use a stack which takes in evey open tag we encounter. When we encounter a closing tag, we can check whether the last element in our stack pairs with the closing tag we encountered. If it does, we pop it from the stack and carry on with probing the rest of the paragraph. Otherwise, we print the error message defined. 

In the event that we finish examining our ordered list of tags, and find that our stack still contains elements, this means that these tags were not closed properly. Thus, we output the error message for the last element in the stack which wasn't closed.