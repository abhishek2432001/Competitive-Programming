''' Problem-1=> Circular sentence:A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

For example, "Hello World", "HELLO", "hello world hello world" are all sentences.
Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:

The last character of a word is equal to the first character of the next word.
The last character of the last word is equal to the first character of the first word.
For example, "leetcode exercises sound delightful", "eetcode", "leetcode eats soul" are all circular sentences. However, "Leetcode is cool", "happy Leetcode", "Leetcode" and "I like Leetcode" are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.'''

def isCircularSentence(sentence) -> bool:
    l = sentence.split()
    n = len(l)
    if(n==1):
        return l[0][0]==l[0][-1]
    c = 0
    for i in range(n-1):
        if (l[i+1][0]==l[i][-1]):
            c+=1
    if(l[0][0]==l[n-1][-1]):
        c+=1
    return c==n

'''Problem:2=>2491. Divide Players Into Teams of Equal Skill: You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.'''

def dividePlayers(skill) -> int:
    n = len(skill)
    skill.sort()
    res = 0
    for i in range(n//2):
        if(skill[i]+skill[n-i-1]!=skill[0]+skill[n-1]):
            return -1
        res+=(skill[i]*skill[n-i-1])
    return res