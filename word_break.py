def word_break(remaining_string, words, result = ""):
    if not remaining_string:
        print(result.strip())
        return

    for i in range(1, len(remaining_string) + 1):
        prefix = remaining_string[:i]

        if prefix in words:
            word_break(remaining_string[i:], words, result + prefix + " ")

words = ["this", "th", "is", "famous", "Word", "break", "b", "r", "e", "a", "k", "bre", "brea", "ak", "problem"]
input_string = "Wordbreakproblem"

word_break(input_string, words)
