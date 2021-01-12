import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
import sys

class Zomato_Data: 
    """ Class that reads in data from a csv file, specifies which columns to be 
    added to a dataframe, then takes user input based off this dataframe, and 
    eventually executes to provide a user with the best possible dining
    options"""
    def __init__(self,filename):
        """ 
        Function that reads in csv file, instatinates attributes,
        and transfers to data frame
            Args:
                Filename (csv) - csv file containing restaraunt data
                Side effects: 
                    Sets attribute for Zomato DataFrame
        """
        self.filename = filename
        zomato_df = pd.read_csv(self.filename, encoding = "utf-8") 
        cols = ['Restaurant Name','City','Cuisines','Price range',
                'Aggregate rating','Rating text']
        self.zomato_df2 = zomato_df[cols] 
        self.Input_List=[]
        
        
    def df_specifics(self):
        """
        A function that creates a specified DF with the best rated
        resturants(2.5 stars and above) based off of city and cuisine 
            Returns:
                clean_df (df) - new dataframe with specified and sorted columns
        """  
        filter = self.zomato_df2[self.zomato_df2['Aggregate rating'] > 2.5]
        clean_df = filter.sort_values(by ='City', ascending = False)
                
        return clean_df
        
                        
    def input_rating(self):
        """
        A function that takes input from the user based off
        specifications set then validates each of these values 
        (calling input_parser after each input)
         Args:
            city (list/df) - input var taking in
                              the user's location prefrence
            cuisine (list/df) - input var taking in
                              the users cuisine prefrences
            Price (list/df) - input var taking in
                              the users price range prefence  
            Ratings (list/df) - input var taking in 
                                the star reviews prefrence  
         Returns:
            Input_list (list) - List of all the user inputted values  
        """
        while True:
            try:
                city = input("Specify City: ")
                self.city = city
                self.Input_List.append(self.city)
                break
            except ValueError:
                print("Sorry! City not recognized, try again!")                
        
        while True:
            try:
                cuisine = input("Specify Cuisine(s): ")
                self.cuisine = cuisine
                self.Input_List.append(self.cuisine)
                break
            except ValueError:
                print("Sorry! Cuisine(s) not recognized, try again!")

        while True:
            try:
                price = input("What is your price range? (0-5) ")
                self.price = str(price)
                self.Input_List.append(self.price)
                break
            except ValueError:
                print("Please input a numerical value (0-5)")   
                
        while True:
            try:
                rating = input("Desirable stars? (0-5) ")
                self.rating = str(rating)
                self.Input_List.append(self.rating)
                break
            except ValueError:
                print("Please input a numerical value (0-5)")
                       
        return self.Input_List
    
    def df_cleaner(self):
        """
        Takes the raw Df and cleans it up
        for presentation quality
        Return:
            self.clean_df (dataframe): the cleaned up dataframe 
         """
        self.zomato_df2['Cuisines'] = self.zomato_df2['Cuisines'].replace([''],
                                                    'No available Cuisine Name')
        self.zomato_df2['City'] = self.zomato_df2['City'].replace([''],
                                                    'No available Location')
        self.zomato_df2['Price range'] = self.zomato_df2['Price range'].replace([''],
                                                        'No available Price')
        self.zomato_df2['Aggregate rating'] = self.zomato_df2['Aggregate rating'].replace([''],
                                                        'No available rating')
        self.zomato_df2['Restaurant Name'] = self.zomato_df2['Restaurant Name'].replace([''],
                                                'No available restaurant name')
        
        clean_df = self.df_specifics()
            
        return clean_df
    
    def df_match(self):
        """
        Pulls the DF from clean_df found in the df_specifics 
        function and the List from input_rating compares them, searching for
        any and all matches
         Returns:
            clean_df2 (DF) - A dataframe with resulting matches
                             from the input_list
        """
        
        clean_df = self.df_cleaner()
        self.clean_df2 = clean_df[
            (clean_df['City'] == self.Input_List[0]) &
            (clean_df['Cuisines'] == self.Input_List[1])&
            (clean_df['Price range'] <= int(self.Input_List[2])) &
            (clean_df['Aggregate rating'] >= float(self.Input_List[3]))]
                 
        self.clean_df2.sort_values(by =['Cuisines','Aggregate rating','City'],
                                   ascending = False)
        return self.clean_df2.head()   

        
    def data_visualizer(self):
        """
        Using Pandas print out the df produced in df_match()
        
        """
        df = self.clean_df2.head(5)
        plt.bar(df['Restaurant Name'], df['Aggregate rating'],
                align= "center", color= "red")
        plt.ylabel("Rating")
        plt.xlabel("Restaurant Name")
        plt.title('Highest Rated Resturants Based on Specifications')
        plt.show()


def main(filename):
    """
    Calls all the functions above and returns output based 
    off of user specifications
    """
    specific_data = Zomato_Data(filename)
    specific_data.df_specifics()
    specific_data.input_rating()
    specific_data.df_match()
    specific_data.data_visualizer()
    print("Here are your top options based off specification!")
    print(specific_data.clean_df2)
    
    
    
def parse_args(arglist):
    """
    Parses command line arguments, specifically the dataset
        Returns:
            arglist - parsed arguments from the dataset
    """
    parser = ArgumentParser()
    parser.add_argument("filename",
                        help="the name of the file that has the Yelp data")
    
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)

