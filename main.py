nric = input('Enter an NRIC number: ')

letter = ['S', 'T', 'F', 'G']
ST_alphabet = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
FG_alphabet = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']
weight = [2, 7, 6, 5, 4, 3, 2]
sum = 0

if nric[0] in letter and nric[1:8].isdigit() and nric[-1].isalpha() and len(nric) == 9:

  for i in range (len(nric)-2):
    sum += int(nric[i+1]) * weight[i]

  if nric[0] == "T" or nric[0] == "G":
    sum += 4

  remainder = sum % 11

  if nric[0] == "S" or nric[0] == "T":
    checkdigit = ST_alphabet[remainder]
  else:
    checkdigit = FG_alphabet[remainder]

  if nric[-1] == checkdigit:
    print("NRIC is valid.")
  else:
    print("NRIC is invalid.")

else:
  print("NRIC is invalid.")
