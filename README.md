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
│       ├── tests/
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

[Include instructions on how to use the application once it's set up]

## API Documentation

[Include link to API documentation or brief overview of main endpoints]

## Testing

To run the tests:

```
cd backend/node
npm test

cd backend/python
python -m unittest discover tests
```

## Contributing

[Include guidelines for contributing to the project]

## License

[Include your chosen license information]

## Contact

[Your Name] - [your.email@example.com]

Project Link: https://github.com/DesmondKarani/Final_Project_Backend
```

