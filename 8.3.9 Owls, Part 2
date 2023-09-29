def owl_count():
    count = 0
    report = []
    text = input("Enter a Sentence: ")
    text= text.lower()
    for index, word in enumerate(text.split()):
        if word.find("owl") > -1:
            count += 1
            report += [index,]
    print("They were " + str(count) + """ words that contained "owl".""")
    print("They occurred at indices: " + str(report))
    
owl_count()
