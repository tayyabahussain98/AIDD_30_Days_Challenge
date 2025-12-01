# Tasks: Simple Calculator

**Input**: Design documents from `/specs/1-simple-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: The plan includes creating unit and end-to-end tests.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create `calculator_logic.py` for core logic
- [x] T002 Create `main.py` for Streamlit application
- [x] T003 Create `tests/unit/` directory for unit tests
- [x] T004 Create `tests/e2e/` directory for end-to-end tests
- [x] T005 Install project dependencies (`streamlit`, `pytest`) using `uv pip install streamlit pytest`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Implement basic arithmetic functions (`add`, `subtract`, `multiply`, `divide`) in `calculator_logic.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: The user can perform basic arithmetic operations (addition, subtraction, multiplication, division) using the calculator application and see the correct result.

**Independent Test**: The ability to input two numbers, select an operation, and display the correct result can be fully tested independently of other features.

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T007 [US1] Create unit tests for `add`, `subtract`, `multiply`, `divide` functions in `tests/unit/test_calculator_logic.py`

### Implementation for User Story 1

- [x] T008 [US1] Implement Streamlit UI elements for number inputs (`st.number_input`) in `main.py`
- [x] T009 [US1] Implement Streamlit UI elements for operation buttons (`st.button` for +, -, *, /) in `main.py`
- [x] T010 [US1] Implement Streamlit UI element for the "Equals" button (`st.button`) in `main.py`
- [x] T011 [US1] Implement Streamlit UI element for result display (`st.text` or `st.write`) in `main.py`
- [x] T012 [US1] Integrate `calculator_logic.py` functions with Streamlit UI to perform calculations in `main.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Clear Calculator State (Priority: P2)

**Goal**: The user wants to clear the current inputs and displayed result to start a new calculation.

**Independent Test**: The "Clear" functionality can be tested independently by performing a calculation and then verifying that the clear button resets the state.

### Implementation for User Story 2

- [x] T013 [US2] Implement Streamlit UI element for the "Clear" button (`st.button`) in `main.py`
- [x] T014 [US2] Implement logic to reset input fields and result display when "Clear" is clicked in `main.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T015 Handle division by zero error in `calculator_logic.py` to return an error message instead of crashing.
- [x] T016 Implement graceful handling for non-numeric input in `main.py` (Streamlit's `st.number_input` handles this, but ensure robustness).
- [x] T017 Create end-to-end tests for the full calculator application, covering all user stories and edge cases in `tests/e2e/test_calculator_app.py`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (none currently marked, but T001-T004 could be conceptually parallel).
- Once Foundational phase completes, user stories can conceptually start in parallel (if different developers).
- Different user stories can be worked on in parallel by different team members.

---

## Parallel Example: User Story 1

```bash
# All tasks for User Story 1 can be executed sequentially by one developer
# or T007 (tests) could run in parallel with T008-T011 (UI elements) by different developers.
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
