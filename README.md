# Restaurant-Ratings
An explanation of the purpose of each file in your repository:

zomatos.csv is a csvfile that contains data from Zomato API. This data was sourced from kaggle and it contains information used to match user input to aggregated ratings. The dataset contains entries that has information on resturants around the world. testscript.py is the test script file that is used to test python script. ratings_generator.py contains the specified functions for this project, where based on user input sourced recommendations of resturants are displayed.

Clear instructions on how to run your program from the command line:

python(3) restaurant_ratings_generator.py zomato.csv

User will be prompted to enter a specific location (City) (with a capital first letter), Cuisine ( With a capital first letter)(feel free to be creative), Price range (0-5), and desireable star ratings (0-5). Example [Dallas, American, 4,5].

After the user specifies their input values, the top 5 results of the resturants in the specified city will be displayed in a PQ dataframe showing the statistics of price range and aggregate rating. Additionally, a bar graph depicting which restaurants have the highest rating will be displayed.
