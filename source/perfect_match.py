men = ['Xavier', 'Yancey', 'Zeus']
ladies = ['Amy', 'Bertha', 'Clare']
man_preference = [[1, 2, 3],
                  [2, 1, 3],
                  [1, 2, 3]]
lady_preference = [[2, 1, 3],
                   [1, 2, 3],
                   [1, 2, 3]]

matches = [-1 for i in range(0, len(men))] 

while -1 in matches:
    for i, man in enumerate(men):
        if matches[i] == -1:
            # current man has no matching 
            for j, lady in enumerate(ladies):
                if not(j in matches) or (matches[j] > lady_preference[j][i]):
                    matches[j] = i
                    break

for i, match in enumerate(matches):
    print('{0} - {1}'.format(ladies[i], men[match]))