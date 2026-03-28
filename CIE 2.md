# Continuous Internal Evaluation - CIE - II
### Conducted at the end of 8th week

**Submitted to:** Training Supervisor & Cohort Owner  
**Submitted by:** [Your Name]  
**Registration No:** [Your Registration Number]  
**Date:** 28/03/2026

---

## Part A: Assessment of On Job Training (OJT) - 1 (50 Marks)

**Assigned Job Role:** Full Stack Web Developer (Intern)

### 1. Intern's Ability to Apply Skill and Technical Knowledge on OJT-1

Over the past four weeks (spanning Weeks 5 to 8) of the On-the-Job Training, I focused primarily on transitioning from foundational frontend design to dynamic, data-driven web development. My ability to actively apply technical knowledge was demonstrated across several key development domains:
- **Frontend Interactivity (React.js):** Applied React concepts to build interactive, reusable UI components. I successfully utilized React hooks (like `useState` and `useEffect`) to manage component state and handle form inputs dynamically without causing page reloads.
- **Styling and Responsiveness:** Applied Tailwind CSS alongside semantic HTML to ensure all developed web components were mobile-responsive and aligned with modern industry design standards.
- **Backend Infrastructure (Node.js & Express.js):** Successfully transitioned into backend development by setting up local Node servers. I applied conceptual knowledge of HTTP methods to build functional RESTful API routing using the Express framework.
- **Database Management (MongoDB):** Applied data storage concepts by integrating a NoSQL database. I utilized Mongoose to define strict database schemas (e.g., Employee or Asset models) and executed essential CRUD operations to permanently persist data sent from the React frontend.

### 2. Intern's Performance on Assigned Tasks and Project

My performance during this OJT evaluation period has remained consistent, with a heavy focus on timely task execution, active problem-solving, and adherence to clean coding principles:
- **Task Execution:** Successfully completed weekly developmental milestones. This included building isolated frontend interfaces and independently wiring them to local backend APIs. A major accomplishment was completing an interactive form that effectively transmits real-time data to a MongoDB collection.
- **Problem Solving:** Actively used debugging tools such as the Chrome Network tab and Postman to troubleshoot CORS errors and API failures, showcasing a strong capability to independently resolve logical and network bugs.
- **Collaboration & Best Practices:** Actively participated in technical reviews with mentors. I ensured all codebase elements were organized cleanly into modular files (separating routes, controllers, and UI components) and consistently relied on Git for version control to safeguard the collaborative project history.

### 3. Extent of Intern's Ability to Add Value to the Organization

Despite being in a trainee phase, I prioritized delivering tangible value to the engineering team and contributing positively to the organization's collaborative environment:
- **Internal Tool Development:** Prototyped functional internal management tools (such as an Asset Tracking dashboard model). By translating manual data entry processes into digitized, full-stack web applications, I demonstrated how internal operational efficiency could be improved for the company.
- **Team Collaboration:** Fostered a productive team environment by engaging in peer-testing sessions with fellow interns. I assisted in identifying UI bugs in overlapping projects and exchanged constructive technical feedback, reducing the QA testing burden.
- **Process Documentation:** Added value by actively documenting API routes and database schemas in readable formats. This set a solid, structured foundation for the upcoming capstone project phase, benefiting both the training supervisors evaluating the code and future cohort members requiring reference material.

---

## Part B: Use Case Documentation (30 Marks)

**Task Context:** Working on the internal data management tool (e.g., Asset/Employee Tracker) as a Full Stack Intern.

### Use Case: Add New Asset/Record to the System

**1. Use Case Name:** Create Document Entry  
**2. Primary Actor:** End User / System Administrator  
**3. Preconditions:** 
- The React frontend application is loaded in the browser.
- The Express.js backend server is running and actively connected to the MongoDB database cluster.

**4. Brief Description:** 
This use case outlines the step-by-step interaction of a user inputting new data into the web application, the system subsequently processing that incoming payload, and permanently storing the validated record within the database.

**5. Main Success Scenario (Normal Flow):**
1. **User Action:** The user navigates to the "Add New Record" route within the React frontend dashboard.
2. **User Action:** The user strictly fills out the required input fields (e.g., Item Name, Category, Value) and clicks the "Submit" data button.
3. **System Response (Frontend):** React captures the `onChange` events, stores the input within its local state (`useState`), and prevents the default browser reload upon submission.
4. **System Response (Frontend):** React initiates an asynchronous HTTP `POST` request (using `fetch` or `axios`), transmitting the JSON data payload to the Express.js backend API endpoint.
5. **System Response (Backend):** The Express router intercepts the `POST` request and forwards the payload to the specific controller logic.
6. **System Response (Database):** The backend validates the incoming data against the predefined Mongoose Schema. It then executes a `.save()` command to securely store the new document directly in MongoDB.
7. **System Response (Backend):** Upon successful storage, the server returns a `201 Created` HTTP status code back to the client frontend, along with the newly saved database object.
8. **System Response (Frontend):** React updates the UI state to display a success alert ("Record added successfully!") and dynamically refreshes the visual data table to instantly present the new entry to the user.

**6. Alternative Flow (Error Handling):**
- *Step 6a (Validation Failure):* If the user submits incomplete or improperly formatted fields, the Express backend rejects the save operation. The server responds with a `400 Bad Request` HTTP status. 
- *Step 6b (Frontend Hand-off):* The React frontend catches this 400 error and dynamically displays a localized warning alert to the user (e.g., "Error: Please fill all required fields correctly."), retaining the inputted data within the form so the user can easily perform corrections.

**7. Postconditions:**
A new transactional record is permanently, securely registered within the NoSQL database and immediately rendered visible on the user’s dashboard feed.
