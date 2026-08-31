# Live Market Currency Tracker
#### Video Demo:  (https://youtu.be/pq0aBmLxKXg)
#### Description: 
The Live market currency tracker is used with automated with python application to fetch, process and log real time currency exchange rate live data in market_data.csv. The core objective of this project is to provide a data pipeline that take a user target currency, validate it against live global market, extract the conversion rate, and save the result for use in the future.

The idea behind this project is that in modern age, having access to fast automated data pipeline is very critical, so this program reach out directly to an external api, no need to manually check the exchange rate, and can be print in terminal, while also saving in .csv file

**`project.py`**: This is the main file of the application. the main() is the main function that run lots of other function and code, it is where it take data from request library then validate the data and log the output
**`test_project.py`**: This is where I automatically test the project. using the pytest to run the unit test with the helper function from project.py to make sure that everything is working like I intended
**`requirements.txt`**: A list of what to pip install (requests and pytest) in the terminal
**`market_data.csv`**: A generated csv file from csv library, if it doesn't exist in the first place, the program will create and write the header row, every time the program run successfully, it will append a new row containing Timestamp,Base,Target,Rate

**1. Separation of Concerns (Pure Functions):**
the program was design to be a single, top to bottom program. however this active design choice was made to extract the core logic into isolated helper function (`clean_currency`, `validate_currency`, and `extract_rate`). to disconnect it from live market currency tracker, so that the function can take input and return an output without side effect from changing data.

**2. Offline Unit Testing:**
I separated the logic into pure function so that I was able to write code for test_project.py more effectively. the major challenge for my design is how to test the live api without the test to be crashing if the internet went down. so my solution was to directly hard code the dictionary data directly into my pure function during the testing of my project, so that pytest can be made sure to run check anytime, while also proving that the logic work without relying on the external network.

**3. Graceful Error Handling & Data Persistence:**
I use sys.exit() to make sure that if someone ask or request for a currency that doesn't exist the program will shut down with an error message

### How to Run the Program
By default, the program will run with thai baht (THB). if you want to target a specific currency, you can do so in command-line argument by running python project.py -t ("Your currency")

### Challenges and Learnings
building this project was a significant step for my learning experience, partly when it come to finding the library and the testing part
