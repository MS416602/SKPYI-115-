subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]

sentences = [(sub + " " + verb + " " + obj) for sub in subjects for verb in verbs for obj in objects]

for sentence in sentences:
    print(sentence)
