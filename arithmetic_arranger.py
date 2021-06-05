def arithmetic_arranger(problems, solve=False):
    # Check number of problems
    if len(problems) > 5:
      return "Error: Too many problems."
    
    # Split information
    cleandata = []
    for problem in problems:
      cleandata.append(problem.split())

    # Check correctness
    for data in cleandata:
      if data[1] != '+' and data[1] != '-':
        return "Error: Operator must be '+' or '-'."
      try:
        int(data[0])
      except:
        return "Error: Numbers must only contain digits."
      try:
        int(data[2])
      except:
        return "Error: Numbers must only contain digits."
      if len(data[0]) > 4 or len(data[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
      if len(data) > 3:
        return "Error: Problems consist of two numbers and one sign."
    
    # Determine length of problem
    for data in cleandata:
      problem_length = max(len(data[0]), len(data[2])) + 2
      data.append(problem_length)

    # Determine if problems should be solved
    if solve == True:
      for data in cleandata:
        if data[1] == '+':
          solution = str(int(data[0]) + int(data[2]))
          data.append(solution)
        else:
          solution = str(int(data[0]) - int(data[2]))
          data.append(solution)
    
    # Arrange problems
    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    if solve == True:
      line4 = ""
    for i in range(0, len(cleandata)):
      line1 += " " * (cleandata[i][3] - len(cleandata[i][0])) + cleandata[i][0] + " " * 4
      line2 += cleandata[i][1] + " " * (cleandata[i][3] - len(cleandata[i][2]) - 1) + cleandata[i][2] + " " * 4
      line3 += "-" * cleandata[i][3] + " " * 4
      if solve == True:
        line4 += " " * (cleandata[i][3] - len(cleandata[i][4])) + cleandata[i][4] + " " * 4
    
    arranged_problems += line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4]
    if solve == True:
      arranged_problems += '\n' + line4[:-4]

    # Return
    return arranged_problems