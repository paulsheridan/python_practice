words = [
  "guitar",
  "drums",
  "bass",
  "microphone",
  "keyboard"]
vowels = ['a', 'e', 'i', 'o', 'u']
no_vowels = []

def remove_vowels(each_word):
  each_word = list(each_word)
  for vowel in vowels:
    while vowel in each_word:
      each_word.remove(vowel)
  each_word = ''.join(each_word)
  return each_word

for word in words:
  no_vowels.append(remove_vowels(word))
print(no_vowels) 
