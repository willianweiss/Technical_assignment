# Website Data Scraper

This command-line application scrapes website URLs provided via standard input and extracts logo image URLs and phone numbers found on the sites.

## Prerequisites

- Docker (for running the application using a container)
- Python 3.10 or above (for running the application in a virtual environment)
- Make (optional, for simplified command execution)
- Virtual Environment (recommended for Python dependency management)

## Installation and Setup

### Running with Docker using Make

1. **Build the Docker Image**
   Use this command to build the Docker image for the application:` 

make build

 ``2. **Run the Application**
To run the application using a list of URLs from a file called `websites.txt`, use the following command:`` 

make run

### Alternative Commands

- **Access Bash Inside the Container**
If you need to access the bash shell inside the container for debugging or manual testing, use this command:` 

`make bash`

- **Stop Running Containers**
To stop all containers associated with this application, you can use:` 

`make down`

- **Clean up Docker**
To remove all containers, unused images, and networks associated with the application, use:` 

`make clean`

### Running Locally with a Virtual Environment

1. **Create a Virtual Environment**
 Navigate to the project directory and create a virtual environment:` 

`python3 -m venv venv`

2. **Activate the Virtual Environment**
Before installing dependencies and running the application, activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On MacOS/Linux:
  ```
  source venv/bin/activate
  ```

3. **Install Dependencies**
Install all required Python libraries using:` 

`pip install -r requirements.txt`

4. **Run the Application**
Run the application directly with Python using:` 

`cat websites.txt | python src/main.py`

``Ensure your `websites.txt` file is in the same directory and formatted with one URL per line. Results will be printed in JSON format to your console.

## Usage

After setting up the environment, you can run the application using the `cat websites.txt | python src/main.py` command within the activated virtual environment. Results will be outputted in JSON format directly to your console.

### Explanation of Additions

-   **Virtual Environment Setup**: Detailed instructions for setting up a Python virtual environment are provided to help isolate dependencies and avoid conflicts with system-wide Python packages.
-   **Dependency Installation**: Guidance on how to install required libraries within the virtual environment.
-   **Execution Instructions**: Clear instructions on how to run the application locally using the virtual environment, which is particularly useful for development and testing purposes.