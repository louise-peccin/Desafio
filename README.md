# Desafio-Tekna.Rocks

## Description
This project aims to process data from a Google Sheets spreadsheet, calculate students' status based on their grades and absences, and record the results in the same spreadsheet.

## Features
- Connection with Google Sheets via API.
- Reading and processing student data.
- Calculation of students' status based on grades and absences.
- Updating the spreadsheet with the results.

## Requirements
- Python 3.x
- `gspread` library
- `google-auth` library

## Configuration
1. Create a project on Google Cloud and enable the Google Sheets API.
2. Generate and download a JSON credentials file.
3. Save the JSON file in the same directory as the script or in a secure location.
4. Replace the value of the `SERVICE_ACCOUNT_FILE` constant with the JSON file path.
5. Replace `SPREADSHEET_ID` with the Google Sheets spreadsheet ID.

## Code Logic
1. Authenticates and accesses the Google Sheets spreadsheet.
2. Reads the spreadsheet data and removes the header.
3. Processes each student:
   - Checks the number of absences.
   - Converts and calculates the grade average.
   - Defines the student's status:
     - "Failed due to absences" if they have more than 25% absences.
     - "Failed due to grades" if the average is less than 5.
     - "Final Exam" if the average is between 5 and 7, calculating the required grade for approval.
     - "Approved" if the average is greater than or equal to 7.
4. Updates the spreadsheet with the results.

## Possible Errors and Solutions
- **Credential error:** Check if the JSON credentials file is correct and saved in the appropriate location.
- **Spreadsheet lacks sufficient data:** Ensure the spreadsheet contains the expected data.
- **Error processing data:** Check if the spreadsheet data is correctly formatted (absences as integers and grades separated by commas or periods).

## Author
Developed by Louise P. Peccin.



