import streamlit as st

# Initialize the to-do list in session state
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = ["clean", "room", "study"]

# Set up the page
st.set_page_config(page_title="To-Do List App", page_icon="✅")
st.title("📝 To-Do List")

# Sidebar for actions
with st.sidebar:
    st.header("Actions")
    action = st.radio("Choose an action:", ["Show List", "Add Task", "Remove Task"])

# Main content area
if action == "Show List":
    st.subheader("Your Current To-Do List")
    if not st.session_state.todo_list:
        st.warning("Your to-do list is empty!")
    else:
        for i, task in enumerate(st.session_state.todo_list, 1):
            st.checkbox(f"{i}. {task}", key=f"task_{i}")

elif action == "Add Task":
    st.subheader("Add a New Task")
    new_task = st.text_input("Enter task to add:")
    if st.button("Add Task"):
        if new_task:
            st.session_state.todo_list.append(new_task)
            st.success(f"'{new_task}' has been added to your list!")
            st.rerun()  # Refresh to show updated list
        else:
            st.warning("Please enter a task")

elif action == "Remove Task":
    st.subheader("Remove a Task")
    if not st.session_state.todo_list:
        st.warning("Your to-do list is empty!")
    else:
        # Show current list with checkboxes for removal
        tasks_to_remove = []
        for task in st.session_state.todo_list:
            if st.checkbox(task, key=f"remove_{task}"):
                tasks_to_remove.append(task)
        
        if st.button("Remove Selected Tasks"):
            for task in tasks_to_remove:
                st.session_state.todo_list.remove(task)
            if tasks_to_remove:
                st.success(f"Removed {len(tasks_to_remove)} task(s)")
                st.rerun()  # Refresh to show updated list
            else:
                st.warning("No tasks selected for removal")

# Always show the current list in the main view
st.divider()
st.subheader("Current To-Do List")
if st.session_state.todo_list:
    cols = st.columns(3)
    for i, task in enumerate(st.session_state.todo_list):
        cols[i%3].write(f"✅ {task}")
else:
    st.info("No tasks in your list. Add some tasks to get started!")