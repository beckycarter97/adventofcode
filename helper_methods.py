def sortDictionaryByKey(dictionary, reversed = False):
    return sorted(dictionary.items(), key=lambda x:x[1], reverse=reversed)