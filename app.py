import streamlit as st

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("🟦📝 Simple To-Do List")
st.markdown("**Stay organized and get things done! 🚀**")

# Input for adding a task
new_task = st.text_input("✍️ Enter a new task:", "")

# Add task button
if st.button("➕ Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.session_state["new_task"] = ""  # Clear input field
        st.experimental_rerun()  # Refresh UI after adding task

# Display tasks
if st.session_state.tasks:
    st.subheader("📌 Your Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.9, 0.1])
        col1.write(f"🔵 {task}")  # Green dot for tasks
        if col2.button("❌", key=i):  # Delete button
            st.session_state.tasks.pop(i)
            st.experimental_rerun()  # Refresh UI after deletion
else:
    st.info("🎉 No tasks yet! Add your first task and boost productivity! 💪")
