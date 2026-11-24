# HandIn user guide

## Lecturer feature

### Start the app

From the repository folder, install the dependencies, initialize the local database, and start Flask:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
flask --app app init-db
flask --app app run
```

The seeded lecturer accounts are `achieng@handin.test` and `otieno@handin.test`. Both use the development password `password123`.

### Review your courses and assignments

1. Open the local app and sign in with a lecturer account.
2. The lecturer dashboard lists only the courses assigned to that lecturer, followed by the assignments for those courses.
3. Each assignment row shows its deadline, how many students have submitted, and how many submissions already have a grade.
4. Select **View students** to see every student enrolled in the assignment's course, including students who have not submitted.
5. The table shows each student's submission status and time. Expand **View text response** to read a typed response. File submissions are indicated as attachments; the local storage path is not shown.
6. If a grade and feedback have been saved, they appear in the final column. Grading or changing grades is handled by the grading workflow.

### Create an assignment

1. Select **Create assignment** on the lecturer dashboard.
2. Choose one of your courses, enter a title, and set a deadline.
3. Add optional instructions and select **Create assignment**.
4. The dashboard confirms creation and lists the new assignment. If a field is invalid, the form keeps the values so you can correct them.

Lecturers can create assignments only for courses assigned to their account. Opening another lecturer's assignment URL returns a not-found page.

### Seeded course examples

- Dr. Achieng Odhiambo (`achieng@handin.test`) teaches CS101.
- Mr. Otieno Kamau (`otieno@handin.test`) teaches DB201 and WEB210.
