document.getElementById('add-task-btn').addEventListener('click', function() {
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');
    
    if (taskInput.value.trim() !== "") {
        const li = document.createElement('li');
        li.textContent = taskInput.value;
        taskList.appendChild(li);
        taskInput.value = "";
    } else {
        alert("Please enter a task!");
    }
});

document.getElementById('task-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        document.getElementById('add-task-btn').click();
    }
});