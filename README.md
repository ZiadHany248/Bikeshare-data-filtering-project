#Udacity Bikeshare Project

**Description:** In this project, three datasets are provided, each of which contains information about customers of a Bike-renting company: _Bikeshare_.
The user is asked to provide multiple input each of which helps outline which portions of the data They would like to view.


**Functionality:** The user is prompted to provide inputs when they run the program which include: 
- Name of the city
- The month they would like to view
- Day of the week within that month (if provided)

They provide the input through `while` loops which keep running until they provide valid input. At which point a messege pops up notifying them It's moving onto the next
part of the process. Those inputs are embedded in a function that returns `city`, `month` and `day of week` so they can be used later

A new function, `load data`, the inputs to which are the previously provided  city, month and day is used to
1. Open the csv file that corresponds to the city chosen
`df = pd.read_csv(CITY_DATA[city])`
2.  changing the datatype of the column _Start Time_ to datetime using the `to_datetime` method so we can extract the month part from it and the name of the day, too
3.  Having acquired the month, we filter the dataset by that month like such `df = df[df['month'] == month]` 
4.  Within this newly filtered dataset, we filter again by day of week. Since the user may ask to view _all_ days, we create an if loop to ensure a correct dataframe is being put into use like such `if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]`
        
5. The user is then asked if they would like to view some of the data they've filtered. If they enter yes the data is viewed 5 by 5 until they either reach the end of the dataset **or** they type no
6. When they enter no, The code automatically moves on to do specific calculations. Those calculations are:
 - The Most Frequent Times of Travel
 - The most common month for travelling
 - The most common weekday for travelling
 - The most common hour for travelling                        
 - The most common starting station                                             
