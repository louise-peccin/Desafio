import gspread
from google.oauth2.service_account import Credentials
import math

# Google Sheets API Configuration
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "desafioteknarocks-849c357d5fd4.json"
SPREADSHEET_ID = "1Siswf9gqZm45XJXx1HbSUCNTRPbhxqhHQPZ2w5x5W64"

# Authentication with Google Sheets
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPE)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

data = sheet.get_all_values()

# Checks if there are at least 3 rows (header + data)
if len(data) < 3:
    print("Error: The spreadsheet does not contain enough data.")
    exit()

# Remove the header
data = data[3:]

TOTAL_CLASSES = 60
situations = []

for row in data:
    try:
        # Checks if the row has the expected number of columns before processing
        if len(row) < 5:
            raise ValueError("Incomplete row in the spreadsheet.")

        student_name = row[1].strip()
        absences = int(row[2].strip())

        # Converting the grades
        p1 = float(row[3].replace(",", ".")) / 10  # Convert comma to period and scale to 10
        p2 = float(row[4].replace(",", ".")) / 10
        p3 = float(row[5].replace(",", ".")) / 10

        avg = (p1 + p2 + p3) / 3  # Calculate the average

        if absences > TOTAL_CLASSES * 0.25:
            situation = "Failed for absence"
            final_grade_needed = ""

        elif avg < 5:
            situation = "Failed for grade"
            final_grade_needed = ""

        elif 5 <= avg < 7:
            situation = "Final Exam"
            final_grade_needed = max(0, math.ceil((10 - avg) * 2))

        else:
            situation = "Approved"
            final_grade_needed = ""

        situations.append([situation, final_grade_needed])

    except Exception as e:
        print(f"Error processing student {row[1] if len(row) > 1 else 'Unknown'}: {e}")
        situations.append(["Erro", ""])

# Updates the spreadsheet with the results, correcting the order of the arguments
update_range = f"G4:H{len(situations) + 4}"
sheet.update(range_name=update_range, values=situations)

print("Update completed successfully!")
