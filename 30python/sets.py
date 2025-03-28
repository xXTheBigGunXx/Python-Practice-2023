from typing import List, Set,Dict

string:str = "I am a teacher and I love to inspire and teach people"
array:List[str] = string.split()

hashset:Set[str] = set(array)

#print(f"String has {len(hashset)} of words in {len(array)} word string.")

hashmap:Dict[str, str] = {"name":"Brisius","color":"Red","age":"10"}
print(hashmap.values())
