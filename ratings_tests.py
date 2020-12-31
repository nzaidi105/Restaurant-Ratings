""" Tests the functions from restaurant_ratings_generator"""

from restaurant_ratings_generator import Zomato_Data
from Zomato_Data import df_specifics, input_rating, df_cleaner, df_match 
from unittest import mock
import builtins
import pytest



def test_df_specifics():
    assert filter in ['Aggregate rating'] == 1.5 == False
    assert filter in ['Aggregate rating'] > 2.5 == True
    assert filter in ['Aggregate rating'] < 2.5 == False
       
def test_input_rating(capsys):
    with mock.patch("builtins.input", side_effect=["Dallas",
                                                 "American", "3","4.2"]):
            assert input_rating() == ["Dallas", "American", "3","4.2"]
            captured = capsys.readoutter()
            assert captured.out == ("Please select correct options as specfifed")
            
    with mock.patch("builtins.input", side_effect=["Atlanta",
                                                 "Seafood", "2","4.9"]):
            assert input_rating() == ["Atlanta", "Seafood", "2","4.9"]
            captured = capsys.readoutter()
            assert captured.out == ("Please select correct option as specfifed")
            
    with mock.patch("builtins.input", side_effect=["Boston",
                                                 "Asian", "2","4.4"]):
            assert input_rating() == ["Boston", "Asian", "2","4.4"]   
            captured = capsys.readoutter()
            assert captured.out == ("Please select correct option as specfifed")     
      
def test_df_cleaner(self):
    assert "No available Cuisine Name" in self.zomato_df2['Cuisine'] == True
    assert "No available Location" in self.zomato_df2['City'] == True
    assert "No available Price" in self.zomato_df2['Price'] == True
    assert "No available rating" in self.zomato_df2['Aggregate rating'] == True
    assert "No available Restaurant Name" in self.zomato_df2['Restaurant Name'] == True    


def test_df_match(self):
        
    if self.clean_df2 == self.clean_df[([self.clean_df['City'] == 'Atlanta']) &
                                       ([self.clean_df['Price range'] == '1']) &
                                       ([self.clean_df['Aggregate rating'] == '4'])]:
        assert df_match(len(self.clean_df2) == 'The Varsity')
        
    if self.clean_df2 == self.clean_df[([self.clean_df['City'] == 'New York']) &
                                       ([self.clean_df['Price range'] == '4']) &
                                       ([self.clean_df['Aggregate rating'] == '4.3'])]:
        assert df_match(len(self.clean_df2) == 'CookShop Babbo Daniel')
        
    if self.clean_df2 == self.clean_df[([self.clean_df['City'] == 'Washington DC']) &
                                       ([self.clean_df['Price range'] == '2']) &
                                       ([self.clean_df['Aggregate rating'] == '4.2'])]:
        assert df_match(len(self.clean_df2) == 'Georgetown Cupcake')
   




