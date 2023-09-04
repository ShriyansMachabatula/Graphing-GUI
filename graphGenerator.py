# Shriyans Machabatula(501180685), Sarankan Srikaran(501095498), Vashikar Sasikumar(501165930), Mohammad Afseh(501183348)

# Run the main.py file to see the graphs and the data

import csv  # This is a library that allows us to read csv files and convert them into lists and dictionaries
# This is a library that allows us to make graphs, it is important for things like making graphs for surveys and other data
import matplotlib.pyplot as plt

# Graph 1


def Usage():
    # open the csv file and read the data
    # This line of code opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        # This line of code converts the data into a list
        reader = csv.DictReader(csvfile)
        age_data = []  # This line of code creates an empty list
        use_data = []  # This line of code creates an empty list
        for row in reader:  # This for loop iterates through each row in the data
            # This line of code appends the age of the person to the age_data list
            age_data.append(int(row['How old are you?']))
            use_data.append(  # This line of code appends the frequency of usage of ChatGPT to the use_data list
                row['How often do you use ChatGPT for academic purposes'])  # This line of code appends the frequency of usage of ChatGPT to the use_data list
    # create a dictionary to count the frequency of each usage category
    use_counts = {}
    for use in use_data:
        if use in use_counts:  # This if statement checks if the usage category is in the use_counts dictionary
            use_counts[use] += 1
        else:  # This else statement is executed if the usage category is not in the use_counts dictionary
            use_counts[use] = 1
    # create a dictionary to count the frequency of each age category
    age_counts = {}
    for age in age_data:
        if age in age_counts:
            age_counts[age] += 1
        else:  # This else statement is executed if the age category is not in the age_counts dictionary
            age_counts[age] = 1
    # create a bar graph of the usage data
    plt.bar(range(len(use_counts)), list(use_counts.values()), align='center')
    plt.xticks(range(len(use_counts)), list(use_counts.keys()))
    plt.xlabel('Usage Frequency')
    plt.ylabel('Number of Participants')
    plt.title('ChatGPT Usage Survey Results')
    # adjust layout and show the graph
    plt.tight_layout()
    plt.show()

# Graph 2


def UsageByAge():

    counterOftens = [0, 0, 0, 0, 0]  # Should be in order from 18 - 22
    # x-axis -> age groups
    # y-axis -> user frequency
    ages = [18, 19, 20, 21, 22]  # This line of code creates a list of ages
    # This line of code opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        # This line of code converts the data into a list
        data = list(csv.reader(csvfile))[1:]
        for row in data:
            if int(row[1]) == 18:  # This if statement checks if the age of the person is 18
                # This if statement checks if the frequency of usage is often or very often
                if (row[6]) == "Often" or row[6] == "Very Often":
                    counterOftens[0] += 1
            if int(row[1]) == 19:  # This if statement checks if the age of the person is 19
                if (row[6]) == "Often" or row[6] == "Very Often":
                    counterOftens[1] += 1
            if int(row[1]) == 20:
                if (row[6]) == "Often" or row[6] == "Very Often":
                    counterOftens[2] += 1
            if int(row[1]) == 21:
                if (row[6]) == "Often" or row[6] == "Very Often":
                    counterOftens[3] += 1
            if int(row[1]) == 22:
                if (row[6]) == "Often" or row[6] == "Very Often":
                    counterOftens[4] += 1
    plt.bar(ages, counterOftens)
    # Setting labels and title
    plt.xlabel('Age Groups')
    plt.ylabel('Number of People that use ChatGPT Often')
    plt.title('Often ChatGPT Usage by Age Group')
    # Displaying the bar graph
    plt.show()

# Graph 3


def UsageByMajor():
    counterOftens = [0, 0, 0, 0, 0, 0, 0]  # Should be in order of majors
    majors = {  # Dictionary of majors
        'Comp Sci & Engineering': 0,
        'Business and Economics': 1,
        'Mathematics/Stats': 2,
        'Arts': 3,
        'Health Sciences': 4,
        'Social Science and Humanities': 5,
        'Economics': 6
    }
    # This line of code opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        # This line of code converts the data into a list
        data = list(csv.reader(csvfile))
        for row in data:  # This for loop iterates through each row in the data
            # This line of code assigns the major of the person to the major variable
            major = row[4]
            # This if statement checks if the major is in the majors dictionary and if the frequency of usage is often or very often
            if major in majors and row[6] in {'Often', 'Very Often'}:
                # This line of code assigns the index of the major to the index variable
                index = majors[major]
                # This line of code increments the value of the major by 1
                counterOftens[index] += 1
    # This line of code creates a bar graph
    plt.bar(majors.keys(), counterOftens)
    # Setting labels and title
    plt.xlabel('Majors')
    plt.ylabel('Number of People that use ChatGPT Often')
    plt.title('Often ChatGPT Usage by Majors')
    # Displaying the bar graph
    plt.show()

# Graph 4
# Make a graph that shows the usefulness of ChatGPT by major
# x-axis -> major
# y-axis -> usefulness


def UsefulnessByMajor():
    # Should be in order of the majors list
    counterOfUse = [0, 0, 0, 0, 0, 0, 0]
    # This is a dicitionary containing all the majors which we have survey data for and their index in the counterOfUse list
    majors = {
        'Comp Sci & Engineering': 0,
        'Business and Economics': 1,
        'Mathematics/Stats': 2,
        'Arts': 3,
        'Health Sciences': 4,
        'Social Science and Humanities': 5,
        'Economics': 6
    }
    # This line of code opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        # This line of code converts the data into a list
        data = list(csv.reader(csvfile))
        for row in data:  # This for loop iterates through each row in the data
            # This line of code gets the major of the person who took the survey
            major = row[4]
            # This if statement checks if the major is in the majors dictionary and if the person found ChatGPT helpful
            if major in majors and row[7] in {'Helpful', 'Very Helpful'}:
                # This line of code gets the index of the major in the counterOfUse list
                index = majors[major]
                # This line of code increments the value at the index of the major in the counterOfUse list
                counterOfUse[index] += 1
    # This line of code creates a bar graph using the majors as the x-axis and the counterOfUse list as the y-axis
    plt.bar(majors.keys(), counterOfUse)
    # Setting labels and title
    plt.xlabel('Majors')
    plt.ylabel('Number of People that find ChatGPT Helpful')
    plt.title('Usefullness of ChatGPT Usage by Majors')
    # Displaying the bar graph
    plt.show()

# Graph 5


def AcademicImprovment():
    countOfImprovment = [0, 0, 0, 0, 0, 0, 0]  # Should be in order of majors
    majors = {  # Dictionary of majors
        'Comp Sci & Engineering': 0,
        'Business and Economics': 1,
        'Mathematics/Stats': 2,
        'Arts': 3,
        'Health Sciences': 4,
        'Social Science and Humanities': 5,
        'Economics': 6
    }
    # This line of code opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        # This line of code converts the data into a list
        data = list(csv.reader(csvfile))
        for row in data:  # This for loop iterates through each row in the data
            # This line of code gets the major of the person who took the survey
            major = row[4]
            # This if statement checks if the major is in the majors dictionary and if the person's grades have improved using ChatGPT
            if major in majors and row[8] in {'Yes'}:
                # This line of code gets the index of the major in the counterOfUse list
                index = majors[major]
                # This line of code increments the value at the index of the major in the counterOfUse list
                countOfImprovment[index] += 1
    # This line of code creates a bar graph using the majors as the x-axis and the counterOfUse list as the y-axis
    plt.bar(majors.keys(), countOfImprovment)
    # Setting labels and title
    plt.xlabel("Majors")
    plt.ylabel('Number of People who improved their grades using ChatGPT')
    plt.title("Academic Improvment based on ChatGPT")
    # Displaying the bar graph
    plt.show()

# Graph 6


def TrustByMajor():
    # Should be in order of the majors list
    countOfTrust = [0, 0, 0, 0, 0, 0, 0]
    # This is a dicitionary containing all the majors which we have survey data for and their index in the counterOfTrust list
    majors = {
        'Comp Sci & Engineering': 0,
        'Business and Economics': 1,
        'Mathematics/Stats': 2,
        'Arts': 3,
        'Health Sciences': 4,
        'Social Science and Humanities': 5,
        'Economics': 6
    }
    # This line of code opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        # This line of code converts the data into a list
        data = list(csv.reader(csvfile))
        for row in data:  # This for loop iterates through each row in the data
            # This line of code gets the major of the person who took the survey
            major = row[4]
            # This if statement checks if the major is in the majors dictionary and if the person completely trusts ChatGPT
            if major in majors and row[9] in {'Completely trust it'}:
                # This line of code gets the index of the major in the counterOfTrust list
                index = majors[major]
                # This line of code increments the value at the index of the major in the counterOfTrust list
                countOfTrust[index] += 1

    plt.bar(majors.keys(), countOfTrust)
    # Setting labels and title
    plt.xlabel("Majors")
    plt.ylabel('Number of People who Completely Trust ChatGPT')
    plt.title("Trust of ChatGPT by Majors")
    # Displaying the bar graph
    plt.show()

# Graph 7


def UntrustByMajor():
    countOfTrust = [0, 0, 0, 0, 0, 0, 0]  # Should be in order of majors

    majors = {  # Dictionary of majors
        'Comp Sci & Engineering': 0,
        'Business and Economics': 1,
        'Mathematics/Stats': 2,
        'Arts': 3,
        'Health Sciences': 4,
        'Social Science and Humanities': 5,
        'Economics': 6
    }
    # Opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))  # Converts the data into a list
        for row in data:  # Iterates through each row in the data
            major = row[4]  # Gets the major of the person who took the survey
            # Checks if the major is in the majors dictionary and if the person doesn't trust ChatGPT
            if major in majors and row[9] in {'Often double check', "Don't trust it at all"}:
                # Gets the index of the major in the counterOfUse list
                index = majors[major]
                # Increments the value at the index of the major in the counterOfUse list
                countOfTrust[index] += 1

    # This line of code creates a bar graph using the majors as the x-axis and the counterOfUse list as the y-axis
    plt.bar(majors.keys(), countOfTrust)
    plt.xlabel("Majors")
    plt.ylabel("Number of People who that Doubt ChatGPT's accuracy ")
    plt.title("Distrust of ChatGPT by Majors")
    # Displaying the bar graph
    plt.show()

# Graph 8


def UseByGender():
    countOfUse = [0, 0]  # Number of Genders

    genders = {  # Dictionary of the genders and their associated index in the counterOfUse list
        'Male': 0,
        'Female': 1,
    }
    # Opens the csv file and reads the data
    with open('survey_responses.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))  # Converts the data into a list
        for row in data:  # Iterates through each row in the data
            # Gets the gender of the person who took the survey
            gender = row[2]
            # Checks if the gender is in the genders dictionary and if the person uses ChatGPT often
            if gender in genders and row[6] in {'Often', "Very Often"}:
                # Gets the index of the gender in the coutnerOfUse list
                index = genders[gender]
                # Increments the value at the index of the gender in the counterOfUse list
                countOfUse[index] += 1
    # This line of code creates a bar graph using the majors as the x-axis and the counterOfUse list as the y-axis
    plt.bar(genders.keys(), countOfUse)
    plt.xlabel("Genders")
    plt.ylabel("Number of People who use ChatGPT")
    plt.title("Usage of ChatGPT by gender")
    # Displaying the bar graph
    plt.show()
