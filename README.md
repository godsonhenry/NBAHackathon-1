NBA Hackathon project. https://hackathon.nba.com
Description from NBA website:
When are teams eliminated from playoff contention? Using the results for the 2016-17 regular season as a test case for your quantitative solution, please generate the date that each team was eliminated from playoff contention. We are purely looking for a date when a team was eliminated from playoff consideration, not any specific seed. Please note that your solution should generate the dates automatically, and should use code-based or Excel-based tools. To aid your work, click on this LINK (https://ak-static-int.nba.com/wp-content/uploads/sites/2/2017/06/NBA_Tiebreaker_Procedures.pdf) for a .pdf file of the NBA Tiebreaker rules and an .xlsx file with the following three tabs 1) Divisions for the 2016-17 Season, 2) The game results for the 2016-17 NBA Regular Season, 3) A sample that includes the correct formatting for your final submission. Please note that teams that qualified for the playoffs should be labeled "Playoffs" and the date a team is eliminated should be reported in text format, not Excel Date format.

To run the project:

python Elimination.py --excel_file Analytics_Attachment.xlsx Division_Info 2016_17_NBA_Scores

This project requires openpyxl https://openpyxl.readthedocs.io/en/default/
