# Bitcoin_TXT
Sends a message to your phone when the price of Bitcoin goes above or below a certain price.
The code pulls data from coindesk's API.  It then parses through data to get the USD rate of Bitcoin.  (The rest of the code repeats every hour indefinately).
Once the desired data is extracted, the code checks to see if bitcoin hits a certain price.  That data is sent to an excel file and saved. If the price is outside of a certain range, the program automatically goes to a texting website and sends a message. 
