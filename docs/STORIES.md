# STORIES.md  

## Overview  
This document captures the product backlog for **identity‑sheet**, a spreadsheet‑management tool that replaces traditional positional cell references (e.g., A1, B2) with **identity‑based references** (e.g., `Revenue.Q1`, `Employee[John].Salary`). The stories are organized into epics, prioritized for an MVP, and each includes clear acceptance criteria.

---

## Epics & Story Map  

| Epic | Description | MVP Priority |
|------|-------------|--------------|
| **E1 – Core Identity System** | Define, store, and resolve immutable identities for rows, columns, and cells. | 1 |
| **E2 – Spreadsheet UI** | Interactive web UI for creating sheets, assigning identities, and editing values. | 2 |
| **E3 – Formula Engine** | Compute cell values using identity‑based formulas. | 3 |
| **E4 – Validation & Error Handling** | Detect broken references, circular dependencies, and type mismatches. | 4 |
| **E5 – Data Import / Export** | CSV/Excel import with identity mapping; export to common formats preserving identities. | 5 |
| **E6 – Collaboration & Permissions** | Multi‑user editing, change tracking, and role‑based access control. | 6 |
| **E7 – Integration & API** | REST/GraphQL API for programmatic access and embedding in other tools. | 7 |

---

## MVP Story Set (E1‑E5)

### **E1 – Core Identity System**

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **E1‑01** | **As a sheet creator, I want to define a unique identity for each column, so that formulas can reference columns by name instead of letters.** | - UI field “Column Identity” appears when adding a column.<br>- Identity must be unique within the sheet (case‑insensitive).<br>- System stores identity in schema and exposes it via `GET /sheets/:id/columns`.<br>- Attempting to duplicate an identity shows a clear error message. |
| **E1‑02** | **As a sheet creator, I want to assign an identity to each row (or record), so that I can reference rows semantically.** | - Row identity can be entered when adding a row or edited later.<br>- Identity uniqueness enforced per sheet.<br>- Row identity is persisted and displayed in the row header.<br>- API endpoint `GET /sheets/:id/rows` returns `{id, identity, values}`. |
| **E1‑03** | **As a developer, I want a deterministic resolver that maps an identity string (e.g., `Revenue.Q1`) to a concrete cell, so that the engine can evaluate formulas reliably.** | - Resolver function `resolve(identityPath: string): CellReference` exists.<br>- Supports dot (`.`) and bracket (`[ ]`) notation for nested identities.<br>- Returns a 404‑style error if any segment is missing.<br>- Unit tests cover happy path, missing identity, and ambiguous matches. |
| **E1‑04** | **As a user, I want the system to prevent deletion of an identity that is still referenced elsewhere, so that I avoid breaking formulas.** | - Delete action is disabled when the identity has dependents.<br>- “Force delete” option shows a warning with a list of affected formulas.<br>- After forced deletion, dependent formulas are marked with `#REF!` error. |

### **E2 – Spreadsheet UI**

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **E2‑01** | **As an end‑user, I want a clean grid view that shows both the identity label and the cell value, so that I can understand the sheet at a glance.** | - Column header displays `Identity (Letter)` (e.g., `Revenue (R)`).<br>- Row header displays row identity.<br>- Hovering over a cell shows a tooltip with its full identity path.<br>- Grid is scrollable and responsive down to 768 px width. |
| **E2‑02** | **As a sheet editor, I want inline editing of cell values while preserving the underlying identity reference, so that I can quickly update data without leaving the grid.** | - Double‑click opens an inline editor.<br>- Editing does not alter the cell’s identity path.<br>- On commit, dependent formulas recalculate instantly.<br>- Validation errors appear inline (red border + message). |
| **E2‑03** | **As a power user, I want a “Reference Picker” dialog that lets me browse available identities when writing a formula, so that I avoid typos.** | - Triggered via `=` key or formula bar “fx” button.<br>- Shows searchable tree of sheet identities (columns → rows → cells).<br>- Selecting an item inserts its full identity string into the formula field.<br>- Picker can be dismissed with `Esc`. |
| **E2‑04** | **As a new user, I want an onboarding tutorial that explains identity‑based referencing, so that I can adopt the new paradigm quickly.** | - Modal walkthrough appears on first sheet creation.<br>- Covers: defining identities, using the Reference Picker, and reading error messages.<br>- Users can replay tutorial from the Help menu.<br>- Completion is recorded in local storage to suppress future auto‑launch. |

### **E3 – Formula Engine**

| # | User Story
