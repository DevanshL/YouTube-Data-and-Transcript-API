# Contributing to YouTube Data and Transcript API

Thank you for your interest in contributing to the YouTube Data and Transcript API project! We welcome contributions in various forms, including bug reports, feature suggestions, code improvements, documentation updates, and more. This document outlines the guidelines for contributing to the project.

## Getting Started

### 1. Fork the Repository

Before you start working on any changes, please fork the repository to your own GitHub account. You can do this by clicking the "Fork" button at the top right of the repository page.

### 2. Clone the Repository

Clone the forked repository to your local machine:

```bash
git clone https://github.com/YourUsername/YouTube-Data-and-Transcript-API.git
cd YouTube-Data-and-Transcript-API
```

### 3. Create a New Branch

Create a new branch for your feature or bug fix:

```bash
  git checkout -b feature-or-bugfix-name
```

### 4. Set Up Your Environment

* Create a virtual environment:
  ```bash
  python -m venv venv
  ```
  
* Activate the virtual environment:
   * On Windows:
   ```bash
   venv\Scripts\activate
   ```
   * On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```
   
* Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

* Create a Google Cloud project and enable the YouTube Data API v3:

    * Visit the Google Cloud Console.
    * Create a new project (or use an existing one).
    * Enable the YouTube Data API v3 for your project.
    * Create API credentials and obtain your API key.

* Setting Up the config.json File:

    * Create a config.json file in the testing folder of the project.
    * The config.json file should contain your API key. Here’s an example structure:
    ```bash
      {
    "api_key": "YOUR_YOUTUBE_API_KEY"
    }
    ```

## Making Changes

### 1. Code Style and Standards
  * Follow the existing code style in the project.
  * Write clear, concise, and well-documented code.
  * Ensure that your code is tested and that all tests pass before submitting.
    
### 2. Commit Your Changes
  * Commit your changes with a meaningful commit message:
    ```bash
      git add .
      git commit -m "Description of the changes you made"
    ```

### 3. Push to Your Fork
  * Push your changes to your forked repository:
    ```bash
    git push origin feature-or-bugfix-name
    ```
### 4. Submit a Pull Request

  Go to the original repository and submit a pull request (PR) from your forked branch. Please provide a clear description of your changes and reference any related issues.

## Reporting Bugs

If you encounter any bugs, please open an issue in the repository. Include the following information:

* A clear and descriptive title.
* Steps to reproduce the issue.
*Expected and actual behavior.
* Screenshots or code snippets, if applicable.
    
    
