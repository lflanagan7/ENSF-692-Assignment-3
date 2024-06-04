# school_data.py
# Laurel Flanagan
#
# A terminal-based application for computing and printing statistics based on given input.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Array variable to store 3D array with full data set 
full_data = np.concatenate([[year_2013.reshape(20,3)], [year_2014.reshape(20,3)], [year_2015.reshape(20,3)], [year_2016.reshape(20,3)], [year_2017.reshape(20,3)], [year_2018.reshape(20,3)], [year_2019.reshape(20,3)], [year_2020.reshape(20,3)], [year_2021.reshape(20,3)], [year_2022.reshape(20,3)]])

# Dictionary variable to store all school names and corresponding indices in full_data
school_names_indices = {"Centennial High School" : 0, "Robert Thirsk School" : 1, "Louise Dean School" : 2, 
                "Queen Elizabeth High School" : 3, "Forest Lawn High School" : 4, "Crescent Heights High School" : 5,
                "Western Canada High School" : 6, "Central Memorial High School" : 7, "James Fowler High School" : 8, 
                "Ernest Manning High School" : 9, "William Aberhart High School" : 10, "National Sport School" : 11, 
                "Henry Wise Wood High School" : 12, "Bowness High School" : 13, "Lord Beaverbrook High School" : 14, 
                "Jack James High School" : 15, "Sir Winston Churchill High School" : 16, "Dr. E. P. Scarlett High School" : 17, 
                "John G Diefenbaker High School" : 18, "Lester B. Pearson High School" : 19}

# Dictionary variable to store all school codes and corresponding indices in full_data
school_codes_indices = {"1224" : 0,  "1679" : 1, "9626" : 2, "9806" : 3, "9813" : 4, "9815" : 5, "9816" : 6, "9823" : 7, "9825" : 8, "9826" : 9, "9829" : 10,
                "9830" : 11, "9836" : 12, "9847" : 13, "9850" : 14, "9856" : 15, "9857" : 16, "9858" : 17, "9860" : 18, "9865" : 19}

# Dictionary variable to store all school years and corresponding indices in full_data
school_years_indices = {"2013" : 0, "2014" : 1, "2015" : 2, "2016" : 3, "2017" : 4, "2018" : 5, "2019" : 6, "2020" : 7, "2021" : 8, "2022" :9}

# Dictionary variable to store all school grades aand corresponding indices in full_data
school_grades_indices = {"Grade 10" : 0, "Grade 11" : 1, "Grade 12" : 2}


class School:
    """A class used to create a School object. 
        Attributes:
        school_name (str): String that represents the school's name. Default String is updated based on user input. 
        school_index (int): Integer that represents the school's index within the full_data array. Default Integer is updated based on user input. 
        school_code (str): String that represents the school's code. Default String is updated based on user input. 

    """
    def __init__(self):
        self.school_name = ''
        self.school_index = 0
        self.school_code = ''

    def update_school(self, user_input):
        """update_school: Update the name, index, and code associated with the school object based on user input, as
        long as the user input is included in one of the school_codes_indices or school_names_indices dictionaries. 

        Args:
            user_input (str): String entered by user that represents either the school name or the school code. 

        Returns: 
            None
        """
        if user_input.isdigit and (user_input in school_codes_indices):
            self.school_index = school_codes_indices[user_input]
            self.school_code = user_input
            self.school_name = get_school_name(self.school_index)

        elif user_input.isalpha and (user_input in school_names_indices):
            self.school_index = school_names_indices[user_input]
            self.school_name = user_input
            self.school_code = get_school_code(self.school_index)


def get_school_name(school_index):
        """get_school_name: Finds the school name within the school_names_indices dictionary (the key) 
        based on the school index (the value). 

        Args:
            school_index (int): Integer that represents the school index. 

        Returns:
            key (str): String that represents the school name. 
        """
        for key, value in school_names_indices.items():
            if school_index == value:
                return key


def get_school_code(school_index):
        """get_school_code: Finds the school code within the school_codes_indices dictionary (the key)
        based on the school index (the value). 

        Args:
            school_index (int): Integer that represents the school index. 

        Returns:
            key (str): String that represents the school code. 
        """
        for key, value in school_codes_indices.items():
            if school_index == value:
                return key 


def mean_enrollment(year_index, school_index, grade_index):
    """mean_enrollment: Calculates the mean of the enrollment values (using NaN-safe function) within the 
    full_data array based on the specified indices for subarray views. 

    Args:
        year_index (int or slice()): Can be either an integer that represents the specified year index or a slice object.
        school_index (int or slice()): Can be either an integer that represents the specified school index or a slice object. 
        grade_index (int or slice()): Can be either an integer that represents the specified grade index or a slice object. 

    Returns:
        mean_enrollment_int (int): An integer that represents the mean enrollment value. 

    """
    mean_enrollment = np.nanmean(full_data[year_index, school_index, grade_index])
    mean_enrollment_int = int(mean_enrollment)
    return mean_enrollment_int


def total_enrollment(year_index, school_index, grade_index):
    """total_enrollment: Calculates the sum of the enrollment values (using NaN-safe function) within the 
    full_data array based on the specified indices for subarray views. 

    Args:
        year_index (int or slice()): Can be either an integer that represents the specified year index or a slice object.
        school_index (int or slice()): Can be either an integer that represents the specified school index or a slice object. 
        grade_index (int or slice()): Can be either an integer that represents the specified grade index or a slice object. 

    Returns:
        total_enrollment_int (int): An integer that represents the total enrollment value. 

    """
    total_enrollment = np.nansum(full_data[year_index, school_index, grade_index])
    total_enrollment_int = int(total_enrollment)
    return total_enrollment_int


def mean_total_enrollment(school_index):
    """mean_total_enrollment: Calculates the mean of total enrollment for the specified school over the
    entire 10-year period. 

    Args:
        school_index (int or slice()): Can be either an integer that represents the specified school index or a slice object. 

    Returns: 
        mean_total_enrollment (int): An integer that represents the mean total enrollment value over 10 years. 

    """
    mean_total_enrollment = (total_enrollment(school_years_indices["2013"], school_index, slice(None)) + total_enrollment(school_years_indices["2014"], school_index, slice(None)) +
                            total_enrollment(school_years_indices["2015"], school_index, slice(None)) + total_enrollment(school_years_indices["2016"], school_index, slice(None)) +
                            total_enrollment(school_years_indices["2017"], school_index, slice(None)) + total_enrollment(school_years_indices["2018"], school_index, slice(None)) +
                            total_enrollment(school_years_indices["2019"], school_index, slice(None)) + total_enrollment(school_years_indices["2020"], school_index, slice(None)) +
                            total_enrollment(school_years_indices["2021"], school_index, slice(None)) + total_enrollment(school_years_indices["2022"], school_index, slice(None))) // 10
    return mean_total_enrollment


def main():
    
    # Create a new School object 
    school = School()

    while True:
        try: 
            # Print Stage 1 requirements here
            print("\nENSF 692 School Enrollment Statistics\n")
            print("Shape of full data array: ", full_data.shape)
            print("Dimensions of full data array: ", full_data.ndim)

            # Prompt for user input
            user_input = input("Please enter high school name or school code or press 'q' to end the program: ")

            # Update the School object data based on user input if the name or code input is within either the school_code_indices or school_names_indices dictionary.
            if (user_input.isdigit and (user_input in school_codes_indices)) or (user_input.isalpha and (user_input in school_names_indices)):
                school.update_school(user_input)

                # Print Stage 2 requirements here
                # Call the appropriate functions defined above or directly perform NumPy computational functions on subarray views to print each of the requested statistics. 
                print("\n***Requested School Statistics***\n")
                print("School Name:", school.school_name + ",", "School Code:", school.school_code)
                print("Mean enrollment for Grade 10: ", mean_enrollment(slice(None), school.school_index, school_grades_indices["Grade 10"]))
                print("Mean enrollment for Grade 11: ", mean_enrollment(slice(None), school.school_index, school_grades_indices["Grade 11"]))
                print("Mean enrollment for Grade 12: ", mean_enrollment(slice(None), school.school_index, school_grades_indices["Grade 12"]))
                print("Highest enrollment for a single grade: ", int(np.nanmax(full_data[:, school.school_index, :])))
                print("Lowest enrollment for a single grade: ", int(np.nanmin(full_data[:, school.school_index, :])))
                print("Total enrollment for 2013: ", total_enrollment(school_years_indices["2013"], school.school_index, slice(None)))
                print("Total enrollment for 2014: ", total_enrollment(school_years_indices["2014"], school.school_index, slice(None)))
                print("Total enrollment for 2015: ", total_enrollment(school_years_indices["2015"], school.school_index, slice(None)))
                print("Total enrollment for 2016: ", total_enrollment(school_years_indices["2016"], school.school_index, slice(None)))
                print("Total enrollment for 2017: ", total_enrollment(school_years_indices["2017"], school.school_index, slice(None)))
                print("Total enrollment for 2018: ", total_enrollment(school_years_indices["2018"], school.school_index, slice(None)))
                print("Total enrollment for 2019: ", total_enrollment(school_years_indices["2019"], school.school_index, slice(None)))
                print("Total enrollment for 2020: ", total_enrollment(school_years_indices["2020"], school.school_index, slice(None)))
                print("Total enrollment for 2021: ", total_enrollment(school_years_indices["2021"], school.school_index, slice(None)))
                print("Total enrollment for 2022: ", total_enrollment(school_years_indices["2022"], school.school_index, slice(None)))
                print("Total ten year enrollment: ", total_enrollment(slice(None), school.school_index, slice(None)))
                print("Mean total enrollment over 10 years: ", mean_total_enrollment(school.school_index))
                
                # Verify if there are any enrollments over 500 within full_data for the specified school.
                # If there are enrollments over 500 at the school, construct a mask to obtain these values and print the median value. 
                if np.any(full_data[:, school.school_index, :] > 500):
                    enrollments_over_500 = full_data[:, school.school_index, :][full_data[:, school.school_index, :] > 500]
                    print("For all enrollments over 500, the median value was: ", int(np.median(enrollments_over_500)))
                else: 
                    print("No enrollments over 500.")


                # Print Stage 3 requirements here
                # Call the appropriate functions defined above or directly perform NumPy computational functions to print each of the requested statistics.  
                print("\n***General Statistics for All Schools***\n")
                print("Mean enrollment in 2013: ", mean_enrollment(school_years_indices["2013"], slice(None), slice(None)))
                print("Mean enrollment in 2022: ", mean_enrollment(school_years_indices["2022"], slice(None), slice(None)))
                print("Total graduating class of 2022: ", total_enrollment(school_years_indices["2022"], slice(None), school_grades_indices["Grade 12"]))
                print("Highest enrollment for a single grade: ", int(np.nanmax(full_data)))
                print("Lowest enrollment for a single grade: ", int(np.nanmin(full_data)))

            # Allow user to end the program by entering 'q'. 
            elif user_input == 'q':
                break
            
        # If user does not enter a school name or code within the school_codes_indices or school_names_indices dictionary, display message to let them know input is invalid.
        # Error is handled so that the program will continue to ask user for inputs. 
            else:
                raise ValueError("You must enter a valid school name or code.")
                
        except ValueError as err:
            print(err) 


if __name__ == '__main__':
    main()

