# Full Stack Web Development Internship - Weekly Tasks & Daily Log

## Week 1: Onboarding, Office Culture & Workstation Setup
**Weekly Objective:** Familiarize with the office environment, set up the physical workstation, and understand basic corporate etiquette.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Orientation & Introduction | Reached the office. Attended the HR orientation, received the intern ID card, and met the assigned mentor (a Senior Software Engineer). |
| **Day 2** | Desk Setup & Software Installation | Set up the physical desk. Guided by the mentor to install necessary tools: VS Code, Google Chrome, Node.js, and Git. |
| **Day 3** | Understanding the Tech Stack | Attended a high-level walkthrough session where a senior dev explained the MERN stack architecture used in the company's internal tools. |
| **Day 4** | Basic Version Control (Git) | Practiced basic Git commands locally. The mentor explained the difference between `git commit` and `git push` using a whiteboard. |
| **Day 5** | Team Lunch & Shadowing | Joined the engineering team for an introductory lunch at the office cafeteria. Shadowed the mentor during the afternoon to see how they use Jira for task management. |

## Week 2: HTML5 & CSS3 Review (Curriculum Focus)
**Weekly Objective:** Review front-end fundamentals as per the diploma syllabus, applying them to small, assigned tasks.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Semantic HTML | Given a small text document by the mentor and tasked with structuring it using proper semantic HTML5 tags (e.g., `<article>`, `<header>`). |
| **Day 2** | CSS Styling Basics | Applied basic CSS to the HTML document. Learned about the company's color palette and typography guidelines. |
| **Day 3** | The Box Model in Practice | Attended a 30-minute desk-side session where a junior developer explained margins, padding, and borders using the browser's Inspect Element tool. |
| **Day 4** | Simple Layouts with Flexbox | Refactored the CSS to use Flexbox. Struggled initially, but a colleague helped explain how `justify-content` works. |
| **Day 5** | Responsive Design Basics | Added simple media queries to make the assigned layout look acceptable on mobile screen sizes. Mentor reviewed the code and provided feedback. |

## Week 3: JavaScript Fundamentals (ES6)
**Weekly Objective:** Solidify core JavaScript concepts required for React, moving beyond basic scripts to structured logic.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Variables & Data Types | Reviewed `let`, `const`, and basic data types. Wrote simple scripts to manipulate strings and arrays based on a practice set provided by the lead dev. |
| **Day 2** | Functions & Arrow Syntax | Practiced writing standard functions and converting them into ES6 arrow functions, a requirement for the company's codebase. |
| **Day 3** | DOM Manipulation - Part 1 | Wrote a script to change text content and background colors on a dummy HTML page when a button is clicked. |
| **Day 4** | Event Listeners | Expanded the previous day's script to include form validation (e.g., checking if an email input contains '@') before submission. |
| **Day 5** | Friday Sync & Demo | Demonstrated the small interactive form to the mentor during the weekly 1-on-1 feedback session. |

## Week 4: Introduction to React.js Concepts
**Weekly Objective:** Understand the basics of component-based architecture by building small, isolated UI elements under supervision.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | What is React? | Shadowed a frontend developer who explained the concept of the Virtual DOM and why the company uses React for its dashboards. |
| **Day 2** | Setting up React (Vite) | Guided by a junior dev to set up a new React project using Vite instead of Create React App, noting the faster build times. |
| **Day 3** | Creating First Components | Rebuilt the HTML form from Week 3 as a set of basic, static React functional components (Header, Form, Footer). |
| **Day 4** | Understanding Props | Learned how to pass static data (like titles and default generic user info) from a parent component down to child components. |
| **Day 5** | Code Walkthrough | Sat with the mentor to review a small section of the company's actual React codebase to see how Props are used in production. |

## Week 5: React State and Basic Interaction
**Weekly Objective:** Learn how to make React components interactive using basic state management.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Introduction to `useState` | Added a simple counter feature to the practice React app to understand how the `useState` hook works. |
| **Day 2** | Handling Form Inputs | Updated the React form to be "controlled" by React state, logging the user's input to the console on every keystroke. |
| **Day 3** | Conditional Rendering | Implemented basic logic to show a "Settings" section only if a simulated user is marked as an 'admin' in the component's state. |
| **Day 4** | Working with Arrays in State | Created a basic To-Do list component. Learned how to add new items to an array in React state without mutating the original array. |
| **Day 5** | Mentor Code Review | Submitted the To-Do list code to an internal intern GitHub repository. The mentor reviewed the PR and suggested minor naming convention improvements. |

## Week 6: Introduction to Node.js & Server Basics
**Weekly Objective:** Transition to the backend learning phase, understanding how a basic server runs locally.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Client-Server Architecture | Attended a whiteboard session outlining how the React frontend (client) talks to the Node.js backend (server). |
| **Day 2** | Node Setup & `npm` | Initialized a new Node.js project. Learned how to install external packages using `npm` and what the `package.json` file does. |
| **Day 3** | Building a Barebones Server | Wrote a basic "Hello World" server using Node.js built-in `http` module just to understand the raw concept. |
| **Day 4** | Introduction to Express.js | Switched to Express.js. Set up a simple server that responds with JSON data when visiting `localhost:3000/api/status`. |
| **Day 5** | Team Tech Talk | Attended the Friday engineering all-hands meeting in the conference room. Listened to a presentation on the company's new backend microservices architecture (absorbing high-level concepts). |

## Week 7: Building Simple REST API Routes (Express)
**Weekly Objective:** Create basic API endpoints that handle different types of HTTP requests, working closely with backend juniors.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | HTTP Methods (GET, POST) | Shadowed a backend developer creating a new API route. Learned the difference between GET (fetching data) and POST (sending data). |
| **Day 2** | Creating Basic GET Routes | Created endpoints that return static, hardcoded JSON arrays (e.g., a list of mock employee names). |
| **Day 3** | Testing with Postman | Installed Postman. The mentor showed how to use it to test the newly created GET routes without needing a frontend interface. |
| **Day 4** | Handling URL Parameters | Modified the GET route to accept a parameter (e.g., `/api/employee/1`) and return a specific object from the mock array. |
| **Day 5** | Handling POST Data | Created a POST route that accepts JSON data from Postman and `console.log`s the received payload in the terminal. |

## Week 8: Introduction to Databases (MongoDB)
**Weekly Objective:** Understand NoSQL database concepts and learn how to perform basic CRUD operations directly in the database.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Relational vs. NoSQL | Read assigned articles explaining the difference between tables (SQL) and collections/documents (MongoDB). |
| **Day 2** | MongoDB Compass Setup | Installed MongoDB Compass and connected to the company's dedicated local intern database instance. |
| **Day 3** | Basic MongoDB Commands | Practiced basic Mongo shell commands (`insertOne`, `find`) to manually add and view mock user records. |
| **Day 4** | Connecting Express to MongoDB | Guided by the mentor to install `mongoose` and establish a connection from the local Express server to the local database. |
| **Day 5** | Defining a Basic Model | Created a simple Mongoose Schema (e.g., an `Employee` model with Name, Department, and Email fields). |

## Week 9: Connecting API to Database (Backend CRUD)
**Weekly Objective:** Connect the Express routes from Week 7 to the MongoDB database using Mongoose.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Implementing the GET Route (DB) | Updated the GET route to use `Employee.find()` to return real data from the database instead of the hardcoded array. |
| **Day 2** | Implementing the POST Route (DB) | Updated the POST route to create and save a new `Employee` document to MongoDB using the data sent via Postman. |
| **Day 3** | Handling API Errors | Added basic `try...catch` blocks to the routes. Learned how to return a `500 Internal Server Error` status if the database query fails. |
| **Day 4** | Route Organization | Helped the mentor refactor the internship codebase, moving route logic out of `server.js` and into separate controller files for cleaner structure. |
| **Day 5** | End-of-Week Review | Demonstrated the working Postman-to-Database flow to the tech lead during the Friday sync. |

## Week 10: API Integration Basics (Connecting Frontend & Backend)
**Weekly Objective:** Learn how to make the React app communicate with the Node/Express backend locally.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Understanding CORS | Encountered the CORS error when trying to fetch data from React. The mentor explained why browsers block this and how to configure the `cors` package in Express. |
| **Day 2** | Using `useEffect` for Data Fetching | Added a `useEffect` hook to the React app to automatically call the local GET API when the page loads. |
| **Day 3** | Displaying Real Data | Replaced the hardcoded data in the React frontend with the dynamic JSON data fetched from the local MongoDB instance via the API. |
| **Day 4** | Submitting the Frontend Form | Wired up the React "Add Employee" form to send a POST request to the backend, successfully saving new entries to the database. |
| **Day 5** | Debugging Network Issues | Spent an hour with a QA engineer learning how to use the Chrome Network tab to inspect failed API requests. |

## Week 11: Introduction to Bootstrap/Tailwind & UI Polish
**Weekly Objective:** Apply a CSS framework to improve the look of the intern project without writing extensive custom CSS.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | CSS Frameworks Overview | Explored Bootstrap and TailwindCSS documentations. Decided to use Tailwind (or Bootstrap) based on the mentor's recommendation. |
| **Day 2** | Integrating the Framework | Installed and configured the chosen framework within the React internship project. |
| **Day 3** | Styling the Data Table | Applied framework classes to style the raw HTML table displaying the database records, making it look professional. |
| **Day 4** | Styling the Forms | Converted the basic HTML input fields into styled framework components with proper labels and padding. |
| **Day 5** | Responsive Checks | Tested the newly styled application on a physical phone to ensure the tables and forms stack correctly on mobile. |

## Week 12: Capstone Mini-Project Phase 1 (Planning & Scaffolding)
**Weekly Objective:** Begin a guided, internal capstone project (e.g., a simple internal "Asset Tracker" or "Leave Request App") acting as a practical exam for the syllabus.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Project Briefing | Met with the engineering manager to discuss a simple internal tool project that the intern can build over the next 3 weeks. |
| **Day 2** | Schema Planning | Sat with the mentor to draw the necessary database schema (e.g., an `Asset` collection and an `Employee` collection) on a whiteboard. |
| **Day 3** | API Endpoints Design | Listed out the required API routes on a Google Doc and got them approved by the backend team lead. |
| **Day 4** | Repository Setup | Created a new folder structure for the capstone project. Initialized Git, Node, and React. |
| **Day 5** | Scaffolding the Backend | Set up the Express server, connected it to a new MongoDB database, and defined the initial Mongoose models. |

## Week 13: Capstone Mini-Project Phase 2 (Core Logic Development)
**Weekly Objective:** Build out the core functionality of the capstone project under the guidance of senior developers.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Building the API Routes | Focused entirely on the backend, writing the CRUD routes for the primary resource (e.g., Assets). |
| **Day 2** | Testing the API | Thoroughly tested all new endpoints using Postman to ensure data is saved and retrieved correctly. |
| **Day 3** | Frontend Scaffolding & Routing | Set up React Router to handle navigation between the "Dashboard", "Add Item", and "View Details" pages. |
| **Day 4** | Integrating API (Read) | Connected the frontend Dashboard page to fetch and display the data from the backend. |
| **Day 5** | Pair Programming Session | Did a 1-hour pair programming session with a junior developer to troubleshoot an issue with React state not updating correctly after an API call. |

## Week 14: Capstone Mini-Project Phase 3 (Form Handling & Polish)
**Weekly Objective:** Complete the data entry features and refine the user experience of the capstone project.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Integrating API (Create/Post) | Built the form in React to add new items and successfully wired it to the backend POST route. |
| **Day 2** | Form Validation | Added simple checks in React to ensure the user cannot submit the form with empty required fields before hitting the API. |
| **Day 3** | UI Refinements | Added "Loading..." messages while data is being fetched and simple Success/Error alerts after form submission. |
| **Day 4** | Peer Testing | Exchanged the physical laptop with another intern on the floor to test each other's applications and note down bugs. |
| **Day 5** | Bug Fixing | Addressed the minor bugs found during peer testing (e.g., fixing a misaligned button, correcting an API path typo). |

## Week 15: Documentation & Report Preparation (College Requirement)
**Weekly Objective:** Shift focus from coding to documenting the work done to fulfill the diploma 6th-semester report requirements.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Writing the Project Report (Intro) | Drafted the introduction, objective, and software/hardware requirements section for the college internship report. |
| **Day 2** | Documenting the Architecture | Created simple diagrams showing how the React frontend interacts with the Express backend and MongoDB database. |
| **Day 3** | Taking Screenshots | Captured and formatted screenshots of the working capstone project (Dashboard, Forms, Postman responses) to include in the report. |
| **Day 4** | Writing the Project Report (Implementation) | Documented the key code snippets (like a Mongoose model or a crucial React component) indicating what was learned. |
| **Day 5** | Reviewing the Report | Shared the drafted college report with the office mentor for proofreading and technical accuracy checks. |

## Week 16: Final Review, Handover, and Farewell
**Weekly Objective:** Officially wrap up the project, hand over the code, and complete exit formalities.

| Day | Task | Description |
| :--- | :--- | :--- |
| **Day 1** | Final Code Cleanup | Formatted all code files, removed unused variables and `console.log` statements following the company's clean code practices. |
| **Day 2** | Code Handover | Pushed the final code to the internal intern GitHub repository. Walked the mentor through the project structure. |
| **Day 3** | Internal Team Presentation | Gave a brief 10-minute presentation to the local engineering team, demonstrating the capstone app and discussing the learning experience. |
| **Day 4** | Getting the Certificate | Printed the college report. Obtained the official sign-offs, company seal, and internship completion certificate from HR and the Engineering Manager. |
| **Day 5** | Farewell Lunch | Handed over the company ID and laptop. Celebrated the end of the internship with a farewell lunch treat with the tech team! |
