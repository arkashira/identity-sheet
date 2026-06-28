# Tech Spec: Identity Sheet v1
=====================================

## Stack
---------------

* Language: TypeScript
* Framework: Next.js (for web UI) and Nest.js (for API)
* Runtime: Node.js (14.x) with Docker
* Database: PostgreSQL (13.x) with Docker
* Storage: AWS S3 (for file uploads)

## Hosting
------------

* Primary hosting platform: AWS (EC2, RDS, S3)
* Free-tier-first approach:
	+ Use AWS Free Tier for development and testing
	+ Migrate to paid tier for production
* Secondary hosting platform: DigitalOcean (for load balancing and caching)

## Data Model
--------------

### Tables/Collections

* `users`: stores user information (id, name, email, password)
* `sheets`: stores spreadsheet metadata (id, name, description, created_at, updated_at)
* `cells`: stores cell data (id, sheet_id, row, col, value, created_at, updated_at)
* `references`: stores identity-based references (id, cell_id, sheet_id, created_at, updated_at)

### Key Fields

* `id`: unique identifier for each table/collection (primary key)
* `sheet_id`: foreign key referencing the `sheets` table
* `cell_id`: foreign key referencing the `cells` table

## API Surface
----------------

### Endpoints

1. **GET /sheets**: retrieve a list of available spreadsheets
	* Method: GET
	* Path: /sheets
	* Purpose: retrieve a list of available spreadsheets
2. **POST /sheets**: create a new spreadsheet
	* Method: POST
	* Path: /sheets
	* Purpose: create a new spreadsheet
3. **GET /sheets/{sheetId}**: retrieve a specific spreadsheet
	* Method: GET
	* Path: /sheets/{sheetId}
	* Purpose: retrieve a specific spreadsheet
4. **PUT /sheets/{sheetId}**: update a specific spreadsheet
	* Method: PUT
	* Path: /sheets/{sheetId}
	* Purpose: update a specific spreadsheet
5. **DELETE /sheets/{sheetId}**: delete a specific spreadsheet
	* Method: DELETE
	* Path: /sheets/{sheetId}
	* Purpose: delete a specific spreadsheet
6. **GET /cells/{cellId}**: retrieve a specific cell
	* Method: GET
	* Path: /cells/{cellId}
	* Purpose: retrieve a specific cell
7. **PUT /cells/{cellId}**: update a specific cell
	* Method: PUT
	* Path: /cells/{cellId}
	* Purpose: update a specific cell
8. **DELETE /cells/{cellId}**: delete a specific cell
	* Method: DELETE
	* Path: /cells/{cellId}
	* Purpose: delete a specific cell
9. **POST /references**: create a new identity-based reference
	* Method: POST
	* Path: /references
	* Purpose: create a new identity-based reference
10. **GET /references/{referenceId}**: retrieve a specific identity-based reference
	* Method: GET
	* Path: /references/{referenceId}
	* Purpose: retrieve a specific identity-based reference

## Security Model
-----------------

* Authentication: JSON Web Tokens (JWT) for user authentication
* Authorization: Role-Based Access Control (RBAC) for spreadsheet access control
* Secrets: use environment variables for sensitive data (e.g. database credentials)
* IAM: use AWS IAM for user and role management

## Observability
----------------

* Logging: use Winston for logging and Sentry for error tracking
* Metrics: use Prometheus for metrics collection and Grafana for visualization
* Traces: use OpenTelemetry for distributed tracing

## Build/CI
------------

* Build tool: use Next.js and Nest.js build tools
* CI tool: use GitHub Actions for automated testing and deployment
* Testing: use Jest and Cypress for unit and integration testing
* Deployment: use AWS CodePipeline for automated deployment to production