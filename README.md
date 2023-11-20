# Personal-To-Do-List-Manager-Programming-EI_Study
----> This To-Do List Manager program allows users to manage tasks by adding new tasks, marking them as completed, deleting tasks, and viewing tasks based on completion status. The code has distinct classes (Task and ToDoList) to encapsulate functionalities related to individual tasks and managing the to-do list.

**Code Quality and Structure:**
**Class Structure:** The Task class represents an individual task with its properties and methods. ToDoList class manages a collection of tasks and user interactions.

**Encapsulation:** The task data and methods are encapsulated within the Task class.

**User Interaction:** The main program loop handles user input and invokes methods on the ToDoList instance.

**Implementation of Functional Requirements:**
**Adding Tasks:** The add_task method allows users to add tasks with descriptions and optional due dates.

**Marking Tasks as Completed:** mark_completed enables users to mark pending tasks as completed.

**Deleting Tasks:** delete_task lets users remove tasks from the list.

**Viewing Tasks:** view_tasks offers options to view all tasks or filter based on completion status.

**Design Patterns and Error Handling:**

**Memento Pattern:** While the Memento Pattern isn't explicitly implemented, it could be applied to allow undo/redo functionality.

**Builder Pattern:** Though not explicitly used, the Task class constructor is handling optional attributes (due date).

**Error Handling:** Basic error handling is implemented, such as validating user inputs.

**File Handling:**
**Loading and Saving Tasks:** Tasks are loaded from and saved to a file (tasks.txt) to persist the to-do list between sessions.

**Possible Improvements:**

**Memento Pattern:** Implementing undo/redo functionality using a stack of mementos to track changes.

**Builder Pattern:** Creating a separate builder class for tasks with more complex creation logic.

**Error Handling Enhancement:** More robust error handling for user inputs to prevent unexpected crashes.
**Enhanced User Interface:** Enhance the user interface for better user experience.

**Explanation of Choices and Trade-offs:**
The code maintains simplicity for understanding but might need enhancements for scalability.
Usage of datetime for due dates might require more error handling to handle invalid date inputs.
