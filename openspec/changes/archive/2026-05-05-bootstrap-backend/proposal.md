## Why

The foundation of the Food Store project must be established to support a scalable, maintainable, and testable architecture. This change introduces the initial scaffolding and infrastructure patterns (layered architecture, Feature-First, Unit of Work) required by the technical specification to ensure consistency across all future domain modules.

## What Changes

- **Project Structure**: Organization of the repository into `backend` and `frontend` directories.
- **Backend Core**: Initialization of a FastAPI application with modular routing.
- **Persistence Layer**: Setup of SQLModel with PostgreSQL connection and Alembic for migrations.
- **Architectural Patterns**:
  - Implementation of the **Unit of Work (UoW)** pattern to manage database transactions atomically.
  - Implementation of a generic **BaseRepository** to abstract database access.
  - Setup of the layered flow: Router -> Service -> UoW -> Repository -> Model.
- **Infrastructure**:
  - Environment variable management using Pydantic Settings.
  - CORS configuration for frontend/backend communication.
  - Basic rate limiting setup with slowapi.
- **Data Seeding**: Initial script for mandatory system data (Roles, Order Statuses, Payment Methods).

## Capabilities

### New Capabilities
- `backend-base`: Scaffolding of the FastAPI application, database integration, and implementation of the core architectural patterns (UoW, Repositories).

### Modified Capabilities
- None

## Impact

This is the initial bootstrap; it affects the entire repository structure and defines the conventions for all subsequent backend development.
