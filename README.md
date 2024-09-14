# AssignmentX
AssignmentX is a web-based tool that generates formatted PDF documents from user-provided text and images. It utilizes Flask for the web framework and PIL (Pillow) for image manipulation to produce customized pages based on various templates. The tool supports text styling and page formatting, making it ideal for generating assignments or reports with specific design requirements.

### Features
Web Interface: Allows users to upload files and specify formatting options through a web API.
Customizable Templates: Users can choose from various page templates and fonts.
Text Styling: Supports multiple fonts and color schemes.
PDF Generation: Converts formatted text and images into a downloadable PDF file.
Error Handling: Provides feedback and error messages for invalid inputs.

### A breif idea
We developed this project to mimic accurate handwritten assignment during the first covid lockdown. As we were lazy and our professors asked us to submit hadwritten assignment, instead of writing it :p we developed this project. It was hosted on pythonanywhere from May 2020 - June 2023. We also made an Android app for the same. The project is no longer supported by me or any of my teammates. What we learned from the project - "Study hard and written your own assignment".

If you wish to try it out follow the steps below.

## Installation
### Prerequisites
- Python 3.6 or higher
- Flask
- Pillow
- Requests
- Werkzeug
- Debudding skills

### Setiing Up
1. Clone the repo:
```bash
git clone https://github.com/dedsec995/assignmentx.git
cd assignmentx
```
2. Install Dependencies:
```bash
pip install -r requirements.txt
```
3. Configure the Upload Folder:
Ensure the `UPLOAD_FOLDER` path in `app.py` is correctly set to a writable directory on your system.

4. Run the Application:
```bash
python app.py
```
