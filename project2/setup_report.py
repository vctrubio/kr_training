import os

'''
To be ran with Make report
Assisted with ai to create seeding data
'''

DIR = 'files/reports'

def create_report_files():
    # Ensure the reports directory exists, create if not
    os.makedirs(DIR, exist_ok=True)

    for i in range(1, 11):
        report_content = f"Sample content for Report {i}. This is just a placeholder."
        file_name = f"report_{i}.txt"
        file_path = os.path.join(DIR, file_name)

        with open(file_path, 'w') as file:
            file.write(report_content)

        print(f"Report file {file_name} created.")

if __name__ == "__main__":
    create_report_files()