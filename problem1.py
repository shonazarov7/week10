votes = ["Samarkand", "Bukhara", "Samarkand", "Khiva", "Samarkand", "Bukhara"]
counts={}
# for vote in votes:
#     if vote in counts:
#         counts[vote]+=1
#     else:
#         counts[vote]=1
for vote in votes:
    counts[vote] = counts.get(vote, 0) + 1
print(counts)
print(counts.get("Khiva"))
print(counts.get("Tashkent",0))
