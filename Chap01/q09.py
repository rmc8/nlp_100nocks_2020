def shuffle_word(word):
    word_length = len(word)
    if word_length <= 4:
        return word
    
    shuffle = ""
    rnd_num = "".join(str(n) for n in range(word_length))
    for i in set(rnd_num):
        num = int(i)
        shuffle += word[num]
    return shuffle


if __name__ == "__main__":
    text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    ans = [shuffle_word(w) for w in text.split()]
    print(ans)
