## ADDED Requirements

### Requirement: core-structure
The system must follow a Feature-First directory structure, separating core infrastructure from domain-specific modules.

#### Scenario: Verify directory layout
- **WHEN** the backend is bootstrapped
- **THEN** directories for `app/core`, `app/db`, and `app/modules` must exist.

### Requirement: db-connectivity
The system must connect to a PostgreSQL database using SQLModel and handle migrations with Alembic.

#### Scenario: Run migrations
- **WHEN** the command `alembic upgrade head` is executed
- **THEN** the database schema must be created or updated successfully.

### Requirement: unit-of-work-pattern
The system must implement the Unit of Work pattern to ensure atomic transactions across multiple repositories.

#### Scenario: Atomic operation
- **WHEN** a service operation uses the UoW context manager
- **THEN** all database changes must be committed only if no exceptions occur, or rolled back otherwise.

### Requirement: base-repository
The system must provide a generic base repository with standard CRUD methods (get, list, create, update, delete).

#### Scenario: Generic CRUD
- **WHEN** a domain repository inherits from `BaseRepository`
- **THEN** it must have access to methods for fetching, listing, and persisting its associated model.

### Requirement: mandatory-seed-data
The system must include a script to seed roles, order statuses, and payment forms.

#### Scenario: Run seed script
- **WHEN** the `seed.py` script is executed
- **THEN** the `Rol`, `EstadoPedido`, and `FormaPago` tables must be populated with mandatory values.
