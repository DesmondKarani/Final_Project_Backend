# Citation Generator

## Project Overview

This project is a web-based citation generator that allows users to create, save, and manage citations in various styles. It demonstrates proficiency in backend development using MongoDB, Python, Node.js, and MySQL.

## Features

- Generate citations in multiple styles (e.g., APA7, MLA, Chicago)
- User account creation and management
- Save and organize citations
- Custom citation style editor
- PDF parsing for automatic citation generation
- Browser extension for easy citation capture

## Tech Stack

- Backend: Node.js with Express.js
- Database: MongoDB (for flexible data) and MySQL (for relational data)
- Citation Logic: Python
- Frontend: HTML, CSS, JavaScript (basic implementation for testing)

## Project Structure

```
citation-generator/
├── backend/
│   ├── node/
│   │   ├── src/
│   │   │   ├── routes/
│   │   │   ├── controllers/
│   │   │   ├── models/
│   │   │   └── middleware/
│   │   ├── tests/
│   │   └── package.json
│   └── python/
│       ├── citation_logic/
│       ├── database/
│       │   ├── __init__.py
│       │   ├── mongodb_setup.py
│       │   └── mysql_setup.py
│       ├── tests/
│       │   ├── __init__.py
│       │   ├── test_mongodb_setup.py
│       │   └── test_mysql_setup.py
│       └── requirements.txt
├── database/
│   ├── mongodb_scripts/
│   └── mysql_scripts/
├── frontend/
│   ├── public/
│   ├── src/
│   └── package.json
├── docs/
├── .gitignore
├── README.md
└── docker-compose.yml
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/citation-generator.git
   cd citation-generator
   ```

2. Set up the backend:
   ```
   cd backend/node
   npm install
   cd ../python
   pip install -r requirements.txt
   ```

3. Set up the databases:
   - Ensure MongoDB and MySQL are installed and running
   - Run the database setup scripts in the `database/` directory

4. Set up the frontend:
   ```
   cd frontend
   npm install
   ```

5. Start the services:
   ```
   docker-compose up
   ```

## Usage

Soon 🙂

## API Documentation

Soon 🙂

## Testing

To run the tests:

```
cd backend/node
npm test

cd backend/python
python -m unittest discover tests
```

## Contributing

I welcome contributions to my project and I'm grateful for your support! Please read through these guidelines to get started:

### How to Contribute

1. **Fork the Repository**
   - Click the "Fork" button at the top right of the repository page to create a copy of the repository in your GitHub account.

2. **Clone Your Fork**
   - Clone your forked repository to your local machine using:
     ```sh
     git clone https://github.com/yourusername/yourproject.git
     ```

3. **Create a Branch**
   - Create a new branch for your work:
     ```sh
     git checkout -b your-branch-name
     ```

4. **Make Changes**
   - Make your changes to the codebase. Ensure that your code follows the project's style guidelines and includes appropriate documentation and tests.

5. **Commit Changes**
   - Commit your changes with a clear and descriptive commit message:
     ```sh
     git commit -m "Description of changes"
     ```

6. **Push Changes**
   - Push your changes to your fork:
     ```sh
     git push origin your-branch-name
     ```

7. **Open a Pull Request**
   - Go to the original repository and open a pull request. Provide a clear description of your changes and the problem they solve. Link any related issues.

### Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](link-to-code-of-conduct). Please read it to understand the expectations for behavior within this community.

### Reporting Issues

If you find any bugs or have feature requests, please open an issue on GitHub. Provide detailed information about the problem or the feature you are requesting to help me address it effectively.

### Style Guide

- Follow the existing coding style and conventions.
- Write clear, concise comments and documentation.
- Ensure your code is properly formatted. You can use linters and formatters to assist with this.

### Tests

- Add tests for your changes and ensure all existing tests pass.
- Run the test suite using:
  ```sh
  npm test  # will develop a test soon 🙂
  ```

### Get Help

If you need any help or have questions, feel free to open an issue or contact me🙂.

Thank you for your contributions!

## License

This project is licensed under the MIT License

## Contact

Desmond Karani

## Links to Socials
- [GitHub](https://github.com/DesmondKarani)
- [LinkedIn](https://www.linkedin.com/in/desmond-karani-a78359b2/)
- [X](https://x.com/karani_des)
- [Website](🙂)

Project Link: https://github.com/DesmondKarani/Final_Project_Backend
