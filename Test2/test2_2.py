# Create a dictionary to remember words and their counts
word_counts = {}
with open("test2_2.txt") as input_file:

    for line in input_file:
        words = line.split(

        )
        for word in words:
            word = word.strip(".,!?\"'()[]{}")
            word = word.lower()

            if len(word) == 4:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

for word in word_counts.keys():
      print(f"{word} {word_counts[word]}")


