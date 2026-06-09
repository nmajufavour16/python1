"""
1. Take user's score input
2. return A if user's score is 70 and above
3. return B if user's score between 60-69
4. return C if user's score is between 50-59
5. return D is user's score is between 40-49
6. return E if user's score is between 30-39
7. return F if user's score is less than 30
"""

score = float(input("Enter Your Score: "))

if score >= 70 and score <= 100:
    print("Grade: A")
elif score >= 60 and score <= 69:
    print ("Grade: B")
elif score >= 50 and score <= 59:
    print ("Grade: C")
elif score >= 40 and score <= 49:
    print ("Grade: D")
elif score >= 30 and score <= 39:
    print ("Grade: E")
elif score >= 0 and score <= 29:
    print ("Grade: F")
else:
    print(f"Input Score {score}\nMust be between 0 and 100.")