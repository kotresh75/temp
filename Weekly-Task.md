# Full Stack Development Internship - Weekly Tasks & Daily Log (In-Office)

**Overview**  
This document outlines the daily logs and weekly tasks for a 16-week Full Stack Development Internship program operating fully **offline/in-office**. Designed specifically for a Diploma or Undergraduate student, the focus is on building a strong MERN stack foundation while experiencing the true startup hustle and tech-park culture of Namma Bengaluru.

---

## Week 1: Office Onboarding, Setup & The Bengaluru Hustle
**Weekly Objective:** Settle into the office space, set up the physical workstation, and get introduced to the team's in-person agile workflow.
- **Day 1:** **Welcome to the Office** - Navigated Silk Board/ORR traffic to reach the office. Collected the company ID card, laptop, and welcome kit. Attended the physical orientation in the boardroom over filter coffee.
- **Day 2:** **Desk Setup & Tooling** - Set up the dual-monitor workstation. Installed VS Code, Node.js, and Git. Met the desk neighbors and the assigned tech mentor.
- **Day 3:** **Whiteboarding Version Control** - Booked a small meeting room with the mentor for a physical whiteboarding session on Git branching (creating, committing, pushing).
- **Day 4:** **Cloning & Team Lunch** - Cloned the company codebase. Joined the team for an authentic "Oota" (lunch) at a nearby Darshini to break the ice with the senior devs.
- **Day 5:** **The Stand-up Circle** - Participated in the first daily in-person stand-up circle on the engineering floor. Learned how tasks are tracked physically on the Kanban board and Jira.

---

## Week 2: Front-End Foundation (HTML & CSS)
**Weekly Objective:** Master front-end structure by collaborating with the design team across the floor.
- **Day 1:** **Semantic HTML & SEO** - Read through the company's UI guidelines. Walked over to the SEO team's bay to understand why semantic tags matter for ranking.
- **Day 2:** **CSS3 & Box Model** - Practiced laying out basic pages. Sat next to a front-end UI developer to observe how they structure their CSS classes.
- **Day 3:** **Flexbox in the Real World** - Replicated the company's internal dashboard layout using CSS Flexbox.
- **Day 4:** **QA Lab Device Testing** - Built a responsive layout and walked into the physical QA device lab to test it natively on various Android and iOS test phones.
- **Day 5:** **Friday Tech Talk** - Attended the weekly all-hands tech talk in the cafeteria. Got the first PR (Pull Request) reviewed in person by the lead developer.

---

## Week 3: JavaScript Core & The DOM
**Weekly Objective:** Add interactivity to web pages using vanilla JavaScript before relying on libraries.
- **Day 1:** **JS Fundamentals** - Reviewed core syntax (`let`/`const`, arrays, objects). Solved algorithmic problems on an actual whiteboard.
- **Day 2:** **DOM Manipulation** - Wrote scripts to change background colors and text dynamically on the test website.
- **Day 3:** **Event Listeners** - Added click and hover events to buttons. Debugged issues by showing the browser console directly to a colleague.
- **Day 4:** **ES6+ Syntax** - Refactored old code to use arrow functions and destructuring based on the company's physical styling guide printed on the desk.
- **Day 5:** **Pair Programming** - Grabbed a chai from the pantry and did a 2-hour pair programming session on a single keyboard with a fellow intern to build a dynamic task list.

---

## Week 4: Introduction to React.js
**Weekly Objective:** Transition to component-based UI development using React.js.
- **Day 1:** **React Architecture** - Attended a workshop in the training room led by a React specialist. Learned about JSX and the Virtual DOM.
- **Day 2:** **Componentizing the UI** - Broke down the vanilla JS project into reusable React components.
- **Day 3:** **Props & Data Flow** - Practiced passing data from parent components down to child components.
- **Day 4:** **State Management (`useState`)** - Converted static components into interactive ones using the `useState` hook. 
- **Day 5:** **Team Code Review** - Presented the React component structure on the big screen during the Friday engineering sync.

---

## Week 5: Advanced React & API Consumption
**Weekly Objective:** Handle external data fetching and routing within the React application.
- **Day 1:** **`useEffect` & Lifecycle** - Learned how to trigger functions when a component mounts to the screen.
- **Day 2:** **Fetching Data** - Used `fetch`/Axios to pull JSON data from the internal staging server located in the local office network.
- **Day 3:** **Mapping Data** - Rendered a list of products dynamically by mapping over the fetched array directly in the UI.
- **Day 4:** **Error Handling** - Built "loading" spinners and error boundaries for when the office WiFi momentarily drops.
- **Day 5:** **React Router** - Sat with the senior frontend team to implement client-side routing, turning the project into a proper Single Page Application (SPA).

---

## Week 6: Back End Fundamentals (Node.js & Express.js)
**Weekly Objective:** Move to the server side by building a foundational Node.js environment.
- **Day 1:** **Server Architecture** - Had a 1-on-1 session with the backend lead over a cup of coffee to understand the client-server lifecycle.
- **Day 2:** **Node.js Initialization** - Created a new `package.json` and installed Express.js.
- **Day 3:** **Express Routing** - Built the first local server listening on port 3000. Handled basic GET and POST requests.
- **Day 4:** **Middleware Basics** - Walked through how middleware executes by adding custom request logging methods to the Express pipeline.
- **Day 5:** **Postman Workshop** - Attended an in-office Postman workshop to learn how backend developers test routes without a frontend.

---

## Week 7: Building RESTful APIs
**Weekly Objective:** Develop standard REST endpoints that the front-end team can consume.
- **Day 1:** **REST Principles** - Learned standard URL naming conventions for endpoints.
- **Day 2:** **CRUD Operations** - Wrote the controller logic to Create, Read, Update, and Delete mock data in memory.
- **Day 3:** **Code Structure** - Refactored the `server.js` file, physically moving routing logic into separate folder structures on the mentor's advice.
- **Day 4:** **Handling Status Codes** - Ensured the API returns the correct 200, 201, 400, and 404 HTTP status codes.
- **Day 5:** **Team Biryani Friday** - Went out for the legendary Meghana Foods biryani with the dev team after successfully pinging all new API routes via Postman.

---

## Week 8: Databases & MongoDB
**Weekly Objective:** Connect the Express server to a NoSQL database to persist data.
- **Day 1:** **NoSQL vs SQL** - Debated database architectures with the backend interns during a lunch break in the cafeteria.
- **Day 2:** **MongoDB Setup** - Connected to the company's sandbox MongoDB Atlas cluster.
- **Day 3:** **Mongoose ODM** - Installed Mongoose and created the first database Schema matching the business requirements.
- **Day 4:** **Writing DB Queries** - Replaced all mock data functions in the backend controllers with actual Mongoose `.find()` and `.save()` operations.
- **Day 5:** **Database Debugging** - Sat over the shoulder of a Senior DBA to see how they check database collections and fix broken documents.

---

## Week 9: Full Stack Integration
**Weekly Objective:** Connect the React frontend to the custom Node/Express backend on the local machine.
- **Day 1:** **CORS Setup** - Faced the infamous CORS error when connecting the frontend to the backend; resolved it with the backend lead's help.
- **Day 2:** **Fetching Own Data** - Updated the React frontend to `fetch()` data from the custom `localhost` API instead of mock servers.
- **Day 3:** **Submitting Forms** - Wired up the "Add Item" form on the frontend to send a POST request saving data to MongoDB.
- **Day 4:** **Network Tab Debugging** - Spent the afternoon with QA learning how to trace dropped packets and slow API responses in the Chrome Network tab.
- **Day 5:** **Environment Variables** - Learned how the company manages `.env` files locally to keep database passwords out of GitHub.

---

## Week 10: State Management & UI Polish
**Weekly Objective:** Elevate the frontend experience using proper state management and styling libraries.
- **Day 1:** **Prop Drilling Identification** - Mapped out the component tree visually on a whiteboard to spot inefficient data passing.
- **Day 2:** **Context API** - Implemented React Context to globally manage user theme preferences (Dark/Light mode).
- **Day 3:** **UI Libraries** - Adopted Bootstrap or TailwindCSS to align the intern project's visuals with the company's internal dashboard styling.
- **Day 4:** **Form Validation** - Added strict front-end validation (preventing empty fields) before allowing the user to hit the backend API.
- **Day 5:** **Design QA** - Had an internal review session where the UI/UX designer provided direct, in-person feedback on button padding and color contrast.

---

## Week 11: Authentication & Security
**Weekly Objective:** Implement secure user login, hashing, and route protection.
- **Day 1:** **Security Fundamentals** - Attended a strict security briefing in the conference room about handling user data.
- **Day 2:** **Password Hashing** - Used `bcrypt` to ensure passwords are never saved as plain-text in the MongoDB database.
- **Day 3:** **JSON Web Tokens (JWT)** - Generated a JWT upon successful login and sent it back to the client.
- **Day 4:** **Backend Protection** - Wrote custom middleware to block API requests if a valid JWT is not provided in the headers.
- **Day 5:** **Frontend Auth Flow** - Updated the React app to store the token securely and redirect unauthenticated users back to the login screen.

---

## Week 12: Internship Capstone Project - Planning
**Weekly Objective:** Transition from guided tasks to building a complete MERN application from scratch.
- **Day 1:** **Project Pitch** - Pitched 3 project ideas (e.g., an internal tool for HR to track assets, a meeting room booker) to the manager in their cabin.
- **Day 2:** **Architecture Whiteboarding** - Blocked a meeting room for 3 hours, drawing database schemas and UI wireframes on the board.
- **Day 3:** **API Contracts** - Documented the exact JSON payloads the frontend and backend will exchange for the project.
- **Day 4:** **Repo Initialization** - Created the official frontend and backend repositories and set up the branching rules as per company policy.
- **Day 5:** **Sprint 1 Kickoff** - Created Jira tickets for the upcoming week and officially kicked off development.

---

## Week 13: Capstone Project Phase - Core Features
**Weekly Objective:** Heads-down coding in the office to build out the business logic.
- **Day 1:** **Database & Models** - Finalized Mongoose schemas and populated the database with seed data.
- **Day 2:** **Backend Core Routes** - Finished the major CRUD operations for the application's primary resource.
- **Day 3:** **Frontend Base Scaffolding** - Set up React Router and the navigation sidebar.
- **Day 4:** **Dashboard Integration** - Connected the frontend dashboard to the backend API, rendering the real database metrics.
- **Day 5:** **Over-the-Shoulder Review** - Asked a senior engineer to drop by the desk and review the current code structure before the weekend.

---

## Week 14: Capstone Project Phase - Polish & Bug Fixing
**Weekly Objective:** Complete secondary features, handle edge cases, and ensure stability.
- **Day 1:** **Secondary Features** - Implemented search, filtering, and pagination on the main data tables.
- **Day 2:** **UI/UX Refinements** - Added toast notifications for success/error states and ensured mobile responsiveness.
- **Day 3:** **Edge Case Testing** - Swapped laptops with a fellow intern to try and "break" each other's applications physically.
- **Day 4:** **Bug Flushing** - Spent the whole day fixing the issues found during the peer-testing session.
- **Day 5:** **Code Cleanup** - Removed dead code, formatted files, and ensured no sensitive data was accidentally hardcoded.

---

## Week 15: Deployment & Hosting
**Weekly Objective:** Take the application off "localhost" and deploy it to live servers.
- **Day 1:** **Deployment Strategies** - Sat with the DevOps team to understand how they deploy the company's main product.
- **Day 2:** **Backend Deployment** - Successfully deployed the Node/Express backend to Render or Railway.
- **Day 3:** **Frontend Deployment** - Deployed the React frontend build to Vercel or Netlify.
- **Day 4:** **Connecting Live Services** - Updated the frontend environment variables to point to the live backend URL instead of `localhost`.
- **Day 5:** **Production QA** - Tested the live URLs on the office network and personal mobile networks to ensure full connectivity.

---

## Week 16: Handover, Documentation & The Final Pitch
**Weekly Objective:** Document the capstone project, hand it over to the team, and present the final results.
- **Day 1:** **Writing the README** - Wrote comprehensive markdown documentation detailing how to run the project locally.
- **Day 2:** **Code Handover** - Met with the engineering manager in a quiet meeting room to hand over GitHub administrative rights and walk through the codebase.
- **Day 3:** **Presentation Rehearsal** - Hooked up the laptop to the boardroom projector to rehearse the slide deck and live demo.
- **Day 4:** **The Final Demo** - Presented the completed Full-Stack MERN application to the entire engineering team and management during the all-hands meeting.
- **Day 5:** **Exit Interview & Farewell** - Conducted the formal HR exit interview, handed over the physical ID badge/laptop, and celebrated with a final team outing in Indiranagar!
