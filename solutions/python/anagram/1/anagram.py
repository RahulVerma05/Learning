def find_anagrams(word, candidates):
    final_list = []
    word = word.lower()
    for i in range(len(candidates)):
        if candidates[i].lower() != word and len(candidates[i]) == len(word):
            if sorted(word) == sorted(candidates[i].lower()):
                final_list.append(candidates[i])
    return final_list
