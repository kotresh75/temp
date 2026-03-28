# Continuous Internal Evaluation - CIE - III
### Conducted at the end of 12th week

**Submitted to:** Training Supervisor & Cohort Owner  
**Submitted by:** [Your Name]  
**Registration No:** [Your Registration Number]  
**Date:** 28/03/2026

---

## Part A: Assessment of On Job Training (OJT) - 2 (50 Marks)

**Assigned Job Role:** Full Stack Application Developer (Intern)

### 1. Intern's Ability to Apply Skill and Technical Knowledge on OJT-2

During the final phase of the On-the-Job Training (spanning Weeks 9 to 12), the focus shifted entirely from learning isolated tools to performing complex, full-scale system integrations and initiating the capstone project. My ability to apply technical acumen was showcased in advanced architectural domains:

#### 1.1 Advanced Frontend Integration & Routing
- **Single Page Navigation:** Successfully applied knowledge of `react-router-dom` to architect a seamless navigation experience across multiple system views (Dashboard, Add Asset, Settings) without any browser reloads.
- **Asynchronous Synchronization:** Effectively utilized `useEffect` hooks to trigger network calls precisely during the React component lifecycle, keeping the client UI constantly synchronized with the remote database state.
- **Complex UI/UX Styling:** Applied advanced Tailwind CSS utility classes to design sleek, fully responsive data grids, modern form input components, and intuitive system alerts tailored for mobile and desktop environments.

#### 1.2 API Architecture and System Refactoring
- **Codebase Refactoring:** Demonstrated solid engineering skills by analyzing the legacy codebase and refactoring monolithic routing logic into separated, clean Controller files (`Controllers/assetController.js`).
- **Network Security:** Applied backend configuration skills to diagnose and successfully bypass complex Cross-Origin Resource Sharing (CORS) errors between the separate React local server and the Express API server.
- **Endpoint Design:** Actively planned and documented comprehensive RESTful API endpoints required for the main capstone project prior to writing any execution code.

#### 1.3 Database Structuring (MongoDB)
- **Schema Planning:** Applied technical design skills to whiteboard complex relational models within a NoSQL structure, carefully planning out how disparate data points would interact within the capstone database.
- **Automated Queries:** Transitioned from manual database inputs via MongoDB Compass to executing robust, automated Mongoose server queries (`.find()`, `.findById()`) driven completely by frontend HTTP requests.

### 2. Intern's Performance on Assigned Tasks and Project

My performance transitioning into the project phase was characterized by rapid development velocity and an uncompromised focus on structural stability:

#### 2.1 Timeline Execution and Project Scaffolding
- Consistently executed the required milestones, leading the initiative to scaffold the new, clean project repository. This included setting up the root folder structures, initializing Node environments, and independently spinning up the React boilerplate ahead of schedule.
- Successfully completed deep integration tasks: wiring up previously static React 'Add Employee/Asset' forms to process dynamic database insertions via the actual Express backend.

#### 2.2 Rigorous Debugging and Testing
- Achieved high performance by thoroughly testing all newly architected CRUD endpoints. By executing rigorous network tests via Postman before connecting the frontend, I eliminated potential backend bottlenecks and prevented frustrating UI bugs.
- Rapidly resolved network failures by actively utilizing the Chrome Network Developer Tools, intercepting failed payload requests, and analyzing HTTP headers to diagnose system disconnections.

#### 2.3 Collaborative Development Practices
- Continued to showcase strong collaborative habits by utilizing Git for all capstone structural updates, providing meaningful commit messages, and ensuring my working branch remained uncorrupted before team reviews.

### 3. Extent of Intern's Ability to Add Value to the Organization

During this critical development phase, I added extensive value to the organization by taking proactive technical ownership over project planning:

#### 3.1 Driving Architectural Blueprinting
- Added significant structural value by leading the Schema and API endpoint planning sessions. I physically documented the required software blueprint on technical whiteboards before development began, ensuring the entire team shared a unified vision of the database goals.

#### 3.2 UI/UX Modernization
- Directly improved the visual standard of the internal management tools. By researching CSS documentation and meticulously integrating modern Tailwind framework styles over raw HTML, I elevated the application from a "rough prototype" into a professional, enterprise-grade interface.

#### 3.3 Knowledge Exchange and Diagnostics
- Provided lasting value by diagnosing complex CORS and asynchronous state bugs that occasionally blocked other interns. By sharing these specific debugging solutions during weekly team syncs, I helped reduce the overall downtime across the cohort.

---

## Part B: Use Case Documentation (30 Marks)

**Project Context:** Developing the internal Capstone Tool (e.g., Asset / Inventory Tracker) as a Full Stack Application Intern.

### Use Case: Fetch and Display Dynamic Data Grid

**1. Use Case Name:** Retrieve and Render Dashboard Records  
**2. Primary Actors:** End User / IT Staff Member  
**3. System Under Consideration:** MERN Stack Inventory Tracker Application  

**4. Preconditions:** 
- The React frontend application is completely booted and loaded in the user's browser.
- The Express.js backend server is actively listening on its assigned network port and maintains a stable connection to the remote Node/MongoDB cluster.
- The database collection actively contains at least one formatted data record.

**5. Brief Description:** 
This technical use case outlines the automated systemic interaction occurring the moment a customized dashboard component loads. It details how the React frontend autonomously requests data from the backend API, how the Express server safely queries MongoDB, and the resultant rendering of the live data table without manual user intervention.

**6. Main Success Scenario (Normal Flow):**

| Step | Actor Action | System Response |
| :--- | :--- | :--- |
| 1 | The user clicks the "View Dashboard" link within the application Sidebar Navigation. | React Router intercepts the URL change and mounts the `<Dashboard />` UI component seamlessly without reloading the window. |
| 2 | - | The component's internal `useEffect()` hook triggers autonomously immediately upon the initial mounting phase. |
| 3 | - | The `useEffect()` hook initiates an asynchronous HTTP `GET` request (via `axios`/`fetch`) targeting the specific REST API endpoint (e.g., `/api/assets`). |
| 4 | - | The Express.js routing layer catches the `GET` request, validating the headers and forwarding the call to the localized read Controller. |
| 5 | - | Express executes a Mongoose `.find({})` command asynchronously, querying the targeted MongoDB collection for all existing internal records. |
| 6 | - | The MongoDB core engine processes the query and returns the targeted array of secure Object documents back to the Express server framework. |
| 7 | - | Express parses the returned database payload and fires a `200 OK` HTTP status response wrapping the raw JSON array back down standard web protocols to the awaiting React client. |
| 8 | - | React receives the sanitized payload and processes it, mutating the local `[data, setData]` state hook with the fetched records. |
| 9 | - | The React Virtual DOM compares the state change and instantly re-renders the responsive Tailwind UI Grid, populating the interactive graphical table rows with real, persistent database values for the User to view. |

**7. Alternative Flows (Error Handling):**

- **7.1 Empty Database Collection:**
  - *If* the MongoDB `.find()` query yields a completely empty response (i.e., no records exist yet).
  - *System Response:* The Express backend functions normally, responding with a `200 OK` status, but transmits an empty JSON array `[]`.
  - *Frontend Hand-off:* The React UI maps the array length (`length === 0`). Instead of generating structural errors or empty grids, the UI conditionally renders a user-friendly fallback placeholder component (e.g., "No Items Found. Please Use the 'Add Record' panel to generate data.")

- **7.2 CORS Rejection / Network Unreachable:**
  - *If* the Express API server goes offline, or standard Cross-Origin blocks are forcefully applied.
  - *System Response:* The browser naturally rejects the `fetch` request on the network level.
  - *Frontend Hand-off:* The `catch()` block within the React `useEffect` hook traps the failure. It triggers an error-state hook, replacing the active loading spinners with a high-visibility Red Banner Alert ("Critical Error: Failed to synchronize with the remote database. Contact Admin.").

**8. Postconditions:**
- **Success:** The user successfully observes an updated, accurate visual dashboard representing the current, live contents of the NoSQL database.
- **Failure:** The user is visually warned of a connection failure and prevented from making structural decisions based on outdated UI data caches.

---
**Note:**
1. *CIE-III shall be assessed by the Industrial Training Supervisor using companies' assessment Tools/Rubrics.*
2. *Cohort owner shall assist the Industrial Training Supervisor during assessment of CIE-III.*
