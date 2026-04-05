## Continuous Internal Evaluation- CIE -III conducted at the end of 12th week

| Sl No | Assessment of On Job Training (OJT)-2 + use case2 | Marks |
| :---: | :--- | :---: |
| 1 | Select another job role of his/her interest in an organization or role assigned by the training supervisor for next Four weeks and submit a report to the training supervisor and copy to cohort owner focusing on:<br><br>1. Intern's ability to apply the skill and technical knowledge on OJT-2<br>2. Intern's performance on assigned tasks and project<br>3. Extent of Intern's ability to add value to the organization through internship | 50 |
| 2 | Documenting of another Use case on a task where he is working as intern | 30 |
| | **Total** | **80** |

**Note:**
1. CIE-III shall be assessed by the Industrial Training Supervisor using companies' assessment Tools/Rubrics
2. Cohort owner shall assist the Industrial Training Supervisor during assessment of CIE-III

---

# CIE 3 Report

**Job Role Assigned:** Full Stack Web Developer Intern  
**Project Allocated:** Online Complaint Management System  
**Organization:** Rlogic Technologies  

## 1. Intern's Ability to Apply Skill and Technical Knowledge on OJT-2

During the On Job Training (OJT-2), I elevated my technical responsibilities by engineering an **Online Complaint Management System**. This project tested my ability to handle complex user matrices and data classification using the MERN stack. My technical applications included:

*   **Frontend Routing & Client Logic:** 
    *   **React Router Dom & State:** Engineered isolated views safeguarding Admin routes (`/admin/dashboard`) from Standard User routes (`/student/complaints`). Utilized localized Context API to prevent endless API polling for user permissions.
    *   **Tailwind CSS Interfaces:** Developed highly polished modal popups and responsive grid boards ensuring long text inputs (e.g., grievance descriptions) render effectively on smartphones without breaking the viewport logic.
*   **Express API & Data Validation:** 
    *   **Node.js Server Mechanics:** Crafted advanced RESTful endpoints (e.g., `POST /api/complaints/new`, `PUT /api/complaints/:id/status`) manipulating JSON payloads inherently mapped to HTTP verbs.
    *   **Authorization Middleware:** Implemented rigorous server-side restrictions confirming that only authorized personnel with valid JWT tokens could manipulate operational status blocks (like resolving a ticket).
*   **NoSQL Schema Engineering:** 
    *   **MongoDB Document Structuring:** Built a highly scalable database capable of storing text-heavy variables natively. Established strict Mongoose schemas explicitly limiting status parameters to 'Open', 'Pending', or 'Closed' strictly enforcing accurate data entry.

## 2. Intern's Performance on Assigned Tasks and Project

Following Rlogic Technologies' strict corporate methodology, I executed all project modules systematically to deliver a fully functional portal:

*   **Phase 1 - Requirement Analysis & Scope:** 
    *   Defined absolute boundaries mapping Standard User privileges against Universal Administrator overriding abilities.
    *   Constructed logical Data Flow Diagrams and ER maps to visualize how an active grievance text block interacted securely with the administrative core without exposing victim details unnecessarily.
*   **Phase 2 - Relational Modeling & Backend:** 
    *   Initialized the central MongoDB Atlas cluster, engineering specific Collections to store varied arrays of complaints categorized by immediate urgency (Infrastructure, IT Support, Administrative).
*   **Phase 3 - Asynchronous Integration:** 
    *   Programmed optimized Axios fetch calls ensuring that when an Administrator shifted a complaint from 'Open' to 'Resolved', the React interface immediately updated its color-coded label without requiring a browser refresh.
*   **Phase 4 - Stress Testing & Security:** 
    *   Deployed Postman to conduct rigorous API checks, actively attempting forceful token hacks. Successfully mapped the backend to reject invalid access arrays throwing direct `401 Unauthorized` errors.

## 3. Extent of Intern's Ability to Add Value to the Organization Through Internship

The complete implementation of the digital Complaint Management workflow provided massive logistical upgrades to legacy operational frameworks:

*   **Resolved Institutional Bottlenecks:** Replaced archaic physical drop-boxes and unstructured email chains completely. This ensured grievances like hardware failures or infrastructure issues were electronically acknowledged immediately, eliminating the risk of lost paper trails.
*   **Maximized Triage Efficiency:** Enabled an interactive ticketing dashboard that allowed administrators to sort and tackle "High Priority" items immediately, massively enhancing operational turnaround speeds.
*   **Modern Data Accountability:** Fostered a transparent electronic record ecosystem. By utilizing strict schema structures, end-users logged complaints accurately, bypassing disjointed manual cross-department communications permanently.

---

## 2. Documenting of another Use case on a task where he is working as intern

**Use Case Title:** Elevating and Resolving a High-Priority Infrastructure Complaint  
**Primary Actor:** Administrative Officer / Systems Manager  
**Secondary Actor:** Standard User (Student / Employee) and Backend MongoDB Database  
**Goal:** Successfully review an incoming, high-priority institution complaint (e.g., Faulty Air Conditioning or Broken Laboratory Equipment) and update its resolution status efficiently within the system.

**Pre-conditions:**
1. A Standard User (e.g., "Rahul K.") has successfully submitted a new complaint ticket categorized as `Infrastructure`.
2. The Administrator is logged into the Online Complaint Management System possessing the `ADMIN` JWT token successfully stored in local memory.
3. The ticketing dashboard is successfully connected to the MongoDB backend.

**Main Success Scenario (Flow of Events):**
1. **Initiation:** The Administrator accesses the secure `/admin/dashboard` URL route on their browser.
2. **Data Polling:** The React application sends an asynchronous `GET` request (`/api/complaints/all`), fetching all current active grievance documents from MongoDB.
3. **Observation:** The Administrator identifies a red-highlighted "High Priority" ticket in the list:
   *   `Ticket_ID`: "RL-COMP-9902"
   *   `Subject`: "Computer Science Lab 3 Air Conditioning Failure"
   *   `Status`: "Open"
4. **Action Trigger:** The Administrator clicks the "Review & Act" contextual button attached to the specific ticket row.
5. **Modification:** A modal overlays the screen viewing the full problem description. The Administrator changes the dropdown menu from `Status: Open` to `Status: Resolved (Fixed by Vendor)`.
6. **Submission:** The Administrator confirms the modifications and clicks the "Update Status" button.
7. **Network Transport:** The React frontend constructs an HTTP `PUT` request targeting `/api/complaints/RL-COMP-9902/status` attaching the Administrator's JWT inside the `Authorization` header securely ensuring only they performed this override.
8. **Server-Side Validation:** The Express.js routing middleware decodes the JWT confirming authorization. It then validates if the string "Resolved (Fixed by Vendor)" is explicitly allowed inside the Mongoose schema constraints.
9. **Database Commit:** The server instructs the driver to formally update the `COMPLAINTS` document. MongoDB overwrites the status string natively returning a clear success object.
10. **UI Hydration:** Express fires a `200 OK` response. React immediately intercepts this updating the dashboard locally. The ticket "RL-COMP-9902" turns green and moves gracefully into the "Archived / Resolved" column seamlessly.

**Alternate Flows (Exceptions):**
*   ***Unauthorized Entry (Step 8):*** If a Standard User hacks the UI attempting to fire the `PUT` request to close their own ticket abruptly, the Express server middleware immediately rejects the `Authorization` header returning a `403 Forbidden` response. The UI renders a red "Access Denied" toast alert.

**Post-conditions:**
*   The complaint resolution metric is permanently recorded with a timestamp indicating exact administrative action.
*   The original user who filed the ticket checking their portal will instantly view their issue securely flagged as resolved.
