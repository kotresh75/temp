# Full Stack Development Internship - Weekly Tasks & Daily Log

**Overview**  
This document outlines the daily logs and weekly tasks for a 16-week Full Stack Development Internship program.

---

## Week 1: Company Onboarding, Environment Setup & Agile Basics
**Weekly Objective:** Complete onboarding, set up the development environment, and integrate into the company's Agile team structure. 
- **Day 1:** **Company Onboarding & Agile Introduction** - Attended onboarding sessions, reviewed company Agile methodologies, and joined the daily standup.
- **Day 2:** **Understanding the Project Domain** - Studied the business domain, architecture patterns, and the product backlog for the intern project assignment.
- **Day 3:** **Development Environment Setup** - Installed and configured required development tools: Visual Studio Code, Git, Node.js, and Java SDK.
- **Day 4:** **Git & Version Control Workflow** - Cloned the company repository, learned branching strategies, and created a test pull request.
- **Day 5:** **Sprint Planning & User Stories** - Participated in sprint planning, reviewing user stories and understanding the Design Thinking behind upcoming UI features.

---

## Week 2: Front End Foundation & HTML/CSS Refactoring
**Weekly Objective:** Understand the existing company front end architecture and update legacy HTML/CSS structures.
- **Day 1:** **Codebase Familiarization (Front End)** - Navigated the existing frontend repository, identifying core HTML files and CSS styles.
- **Day 2:** **HTML Semantic Updates** - Refactored older code snippets to use semantic HTML5 elements for better accessibility.
- **Day 3:** **CSS Processing & Styling** - Used CSS Processors (Sass/Less) to update legacy stylesheets according to the company's new UI/UX design principles.
- **Day 4:** **Responsive Design Implementation** - Implemented Flexbox and Bootstrap components to ensure the assigned module is fully responsive.
- **Day 5:** **Code Review & Finalizing UI** - Pushed frontend changes to GitHub, requested a code review from a senior developer, and resolved comments.

---

## Week 3: JavaScript Implementation & DOM Manipulation
**Weekly Objective:** Add interactivity to the assigned frontend module using vanilla JavaScript before transitioning to frameworks.
- **Day 1:** **JavaScript State & DOM** - Wrote vanilla JavaScript functions to handle basic DOM manipulation within the assigned web application module.
- **Day 2:** **Handling User Events** - Implemented event listeners across form inputs, utilizing JavaScript objects to format collected data.
- **Day 3:** **Data Formatting & JSON** - Created scripts to parse and format mock JSON data simulating backend API responses.
- **Day 4:** **ES6 Refactoring** - Refactored old JavaScript code using modern ES6 features (Arrow functions, Map, `let`/`const`) to meet company coding standards.
- **Day 5:** **Sprint Demo & Retrospective** - Presented the functional, interactive HTML/JS module during the sprint demo and participated in the retrospective.

---

## Week 4: Introduction to React.js Integration
**Weekly Objective:** Transition the vanilla JavaScript/HTML module into a fully componentized React.js application.
- **Day 1:** **React Architecture Overview** - Attended a senior developer session on how React.js is utilized within the company's web application.
- **Day 2:** **Componentizing UI** - Broke down the previously built HTML module into reusable React functional components and JSX.
- **Day 3:** **Props & State Management** - Implemented React state hooks to manage data flow locally within the newly created components.
- **Day 4:** **Dynamic Rendering** - Used the JavaScript `map` function within JSX to dynamically render lists of data (e.g., product lists or user tables).
- **Day 5:** **Integrating Bootstrap with React** - Replaced standard CSS with React-Bootstrap library components to streamline the UI design. Pushed code for review.

---

## Week 5: Advanced React & API Consumption
**Weekly Objective:** Connect the frontend React application to mock external services and handle complex state.
- **Day 1:** **API Integration Strategy** - Studied the company's approach to REST APIs, HTTP methods, and data payload structures.
- **Day 2:** **Fetching Data (Front End)** - Used the `fetch` API (or Axios) inside React `useEffect` hooks to pull data from a mock company endpoint.
- **Day 3:** **Asynchronous Handling & Promises** - Handled asynchronous loading states, errors, and promise resolutions within the React UI gracefully.
- **Day 4:** **Form Handling in React** - Built a complex form component capturing user inputs, validating them, and structuring the POST request payload.
- **Day 5:** **TypeScript Introduction** - Reviewed an existing company project written in TypeScript to understand how strong typing prevents runtime errors.

---

## Week 6: Back End Fundamentals & Database Design
**Weekly Objective:** Shift focus to the backend, designing database schemas, and understanding core DBMS concepts.
- **Day 1:** **Back End Architecture Review** - Reviewed the architectural flow of how the company routes client commands to the server layer.
- **Day 2:** **DBMS & ACID Properties** - Studied Database Management Systems, ensuring an understanding of ACID principles for secure financial/user transactions.
- **Day 3:** **Relational vs. Non-Relational Review** - Participated in a session comparing SQL databases against NoSQL models like MongoDB.
- **Day 4:** **Schema Design (MongoDB)** - Designed a MongoDB document schema for a new feature (e.g., "User Profiles" or "Order History").
- **Day 5:** **Database Provisioning** - Set up a local MongoDB instance and a basic SQL database to practice creating collections and tables.

---

## Week 7: Building Node.js & Express.js Services
**Weekly Objective:** Develop a robust backend service using Node.js to power the React application.
- **Day 1:** **Node.js Initialization** - Initialized a new backend microservice repository using Node.js and installed necessary dependencies.
- **Day 2:** **Express.js Routing** - Built fundamental Express.js routes to handle generic GET, POST, PUT, and DELETE HTTP requests.
- **Day 3:** **Middleware & Processing** - Implemented basic middleware for logging requests and parsing JSON body payloads.
- **Day 4:** **REST API Implementation** - Standardized the Express routes into a clean REST API structure aligning with company API protocols.
- **Day 5:** **Connecting Node.js to MongoDB** - Integrated the MongoDB driver (or Mongoose) into the Node.js service to save and retrieve real data.

---

## Week 8: Java & Spring Boot Backend Development
**Weekly Objective:** Understand enterprise-grade backend development utilizing Java and Spring Boot.
- **Day 1:** **Java Microservices Overview** - Shadowed a senior backend developer to observe how Java is used for high-performance microservices.
- **Day 2:** **Spring Boot Initialization** - Used Spring Initializr and Apache Maven to configure a new basic Java Spring Boot application.
- **Day 3:** **Creating Spring Controllers** - Wrote a Spring Boot REST Controller replicating the functionality built previously in Node.js.
- **Day 4:** **Implementing Core Logic** - Applied Object-Oriented principles to structure Java service layers separate from the API controllers.
- **Day 5:** **Code Review & Backend Demo** - Submitted the Spring Boot service code for peer review and demoed the working API endpoints to the team.

---

## Week 9: Full Stack Integration (React + Backend + DB)
**Weekly Objective:** Achieve full-stack connectivity by linking the React frontend to the newly built backend API and database.
- **Day 1:** **CORS Configuration & Connectivity** - Configured Cross-Origin Resource Sharing (CORS) on the backend to allow requests from the React app.
- **Day 2:** **End-to-End Data Flow (Read)** - Successfully fetched data from the MongoDB database via the Spring Boot (or Node.js) API and displayed it in React.
- **Day 3:** **End-to-End Data Flow (Write)** - Managed a POST request from the React form, routing it through the API, and verifying insertion into the database.
- **Day 4:** **Full CRUD Completion** - Finished implementing complete End-to-End capabilities for Create, Read, Update, and Delete operations.
- **Day 5:** **Bug Fixing & Optimization** - Debugged network latency issues and optimized exactly how the React components update upon database changes.

---

## Week 10: Security by Design & Authentication
**Weekly Objective:** Implement fundamental security practices and application-level authentication.
- **Day 1:** **Security Principles Overview** - Reviewed the company's guidelines on application security testing and secure design methods.
- **Day 2:** **Implementing Basic Authentication** - Added a simple login endpoint to the backend service to verify user credentials against a database table.
- **Day 3:** **JWT (JSON Web Tokens)** - Integrated JWT generation upon successful login and secured specific backend routes to require the token.
- **Day 4:** **Frontend Route Protection** - Updated the React application to store the JWT securely and block rendering of certain pages if unauthenticated.
- **Day 5:** **Security Refactoring** - Sanitized all database inputs to prevent NoSQL/SQL injection vulnerabilities based on senior developer feedback.

---

## Week 11: Application Testing & Quality Assurance
**Weekly Objective:** Write automated tests and perform manual system validation.
- **Day 1:** **Unit Testing Automation** - Wrote automated unit tests utilizing a testing framework (like Jest or JUnit) for backend utility functions.
- **Day 2:** **Frontend Component Testing** - Implemented basic tests to ensure React components render correctly without crashing.
- **Day 3:** **API Integration Testing** - Used tools like Postman (or Newman scripts) to run automated integration tests against the REST API endpoints.
- **Day 4:** **System & Functional Testing** - Performed manual end-to-end system testing, acting as a user traversing the entire application flow.
- **Day 5:** **Resolving QA Tickets** - Addressed bugs and edge cases flagged during the User Acceptance Testing phase and pushed the fixes.

---

## Week 12: Configuration Management & CI/CD Pipelines
**Weekly Objective:** Transition from local development to production-readiness utilizing Continuous Integration tools.
- **Day 1:** **DevOps & Deployment Strategy** - Reviewed the company's DevOps strategy regarding how code moves from GitHub to production servers.
- **Day 2:** **GitHub Actions & CI** - Configured a basic CI/CD pipeline script (e.g., GitHub Actions) to run the automated unit tests whenever code is pushed.
- **Day 3:** **Build Automation** - Automated the "build" process for the React application so the pipeline generates the production-ready static files.
- **Day 4:** **Environment Variables Handling** - Separated configuration (database URIs, secret keys) from code using secure environment variable management.
- **Day 5:** **Pipeline Troubleshooting** - Debugged failing CI builds alongside a DevOps engineer, ensuring stable automated test execution.

---

## Week 13: Containerization using Docker
**Weekly Objective:** Package the full-stack application natively into Docker containers for uniform deployment.
- **Day 1:** **Docker Architecture Training** - Studied Docker principles and how containerization solves the "it works on my machine" problem.
- **Day 2:** **Dockerizing the Backend** - Wrote a standard `Dockerfile` for the Node.js (or Spring Boot) API mapping the appropriate exposure ports.
- **Day 3:** **Dockerizing the Frontend** - Created a multi-stage `Dockerfile` to build the React app and serve its static files using Nginx.
- **Day 4:** **Docker Compose Setup** - Wrote a cohesive `docker-compose.yml` file to spin up the UI, API, and a localized MongoDB container simultaneously.
- **Day 5:** **Local Container Testing** - Shut down all local servers and thoroughly tested the application relying entirely on the Docker Compose network.

---

## Week 14: Kubernetes & Orchestration Concepts
**Weekly Objective:** Move beyond simple containers into enterprise-level orchestration scaling utilizing Kubernetes.
- **Day 1:** **Kubernetes Overview** - Shadowed the DevOps team to understand how Kubernetes orchestrates scaling, self-healing, and networking.
- **Day 2:** **Creating Kubernetes Manifests** - Drafted specific YAML manifest files defining Kubernetes Deployments and Services for the intern application.
- **Day 3:** **Testing with MiniKube** - Spun up a local MiniKube cluster and applied the YAML manifests to deploy the application locally in Kubernetes.
- **Day 4:** **Scaling & Load Balancing** - Scaled the backend deployment to 3 replica pods to observe how Kubernetes balances request traffic natively.
- **Day 5:** **Simulating Pod Failures** - Deleted active pods manually to verify the Kubernetes orchestration self-healing mechanics automatically spin up replacements.

---

## Week 15: Application Monitoring & Disaster Recovery
**Weekly Objective:** Integrate production logging and understand disaster recovery workflows.
- **Day 1:** **Application Monitoring Tools** - Reviewed dashboards in standard application monitoring tools (like Prometheus, Grafana, or Datadog) used by the company.
- **Day 2:** **Centralized Logging Implementation** - Augmented backend API code to output structured JSON logs compatible with centralized logging aggregation.
- **Day 3:** **Performance & Load Metrics** - Evaluated application performance logs to spot database queries causing high latency under load.
- **Day 4:** **Disaster Recovery Planning** - Participated in a disaster recovery tabletop exercise simulating an operational database failure and restoration process.
- **Day 5:** **Automated Alerts Configuration** - Wrote a simple configuration specifying when an alert should trigger (e.g., if the CPU usage of a specific pod exceeds 80%).

---

## Week 16: Project Handover, Documentation, and Final Presentation
**Weekly Objective:** Finalize the internship by wrapping up documentation, performing a final handover, and presenting the completed project.
- **Day 1:** **Final Code Refactoring & Polish** - Completed a final review of the codebase, ensuring it adheres rigidly to company styling, security, and deployment standards.
- **Day 2:** **Internal Documentation** - Wrote extensive markdown documentation detailing the architecture, API routes, and how to run/deploy the module locally.
- **Day 3:** **Preparing the Handover** - Met with the senior developers to conduct a technical handover of the project code, explaining specific logic choices and technical debt.
- **Day 4:** **Presentation Preparation** - Built a short presentation outlining the technologies learned, challenges overcome, and the final state of the application.
- **Day 5:** **Final Demo & Offboarding** - Presented the Full-Stack module to the engineering team and management, formally marking the completion of the internship.
