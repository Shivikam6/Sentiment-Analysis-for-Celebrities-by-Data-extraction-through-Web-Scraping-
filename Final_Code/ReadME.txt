Steps to run the project code:

1. Python 2.7 is required to run the code and ChromeDriver (which is already present in the folder).

2. Application.py - Runs the whole application at Once. It will run Visualization.py and Twitter_Analysis.py.

3. Twitter_Analysis.py - Calls FamousBirthday_data.py and IMDB_data.py to receive the celebrity names and it then fetches tweets for the celebrities and performs Sentiment Analysis using TextBlob. 

4. Visualization.py - Calls FamousBirthday_file.py and IMDB_file.py to receive the celebrity names, profession and rank and performs Data Visualization for the celebrities which are common on IMDb and Famous Birthdays website.

5. FamousBirthday_data.py - Web Scrapes the celebrity names from Famous Birthday website to passes it to Twitter_Analysis.py for Sentiment Analysis.

6. IMDB_data.py - Web Scrapes the celebrity names from IMDb website and passes the it to Twitter_Analysis.py for Sentiment Analysis.

7. FamousBirthday_file.py - Web Scrapes Celebrity name, Profession and Rank from FamousBirthday website and stores the data in famousbirthday.csv file.

8. IMDB_file.py - Web Scrapes celebrity name, Profession and Rank from IMDb website and stores the data in imdb.csv file.

9. Tableau Visualization - imdb.csv and famousbirthday.csv files are imported to Tableau to get number of professions according to the ranks for both the websites (screenshots of the Tableau output are attached).