class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        target_set,postfix = ['a', 'e', 'i', 'o', 'u'],'ma'

        AorB = lambda word: word + postfix if word[0].lower() in target_set else word[1:] + word[0] + postfix
            
        C = lambda word,index: word + 'a' * (index + 1)

        return " ".join([C(AorB(word), index) for index, word in enumerate(sentence.split())])
