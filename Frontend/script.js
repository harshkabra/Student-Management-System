
// =============================
// ADD STUDENT
// =============================

const form = document.querySelector("form");


form.addEventListener("submit", async function (event) {

    event.preventDefault();


    const studentId =
        document.getElementById("studentId").value;


    const studentName =
        document.getElementById("studentName").value;


    const studentAge =
        document.getElementById("studentAge").value;


    const studentCourse =
        document.getElementById("studentCourse").value;


    const studentData = {

        id: Number(studentId),

        name: studentName,

        age: Number(studentAge),

        course: studentCourse

    };


    try {

        const response = await fetch(
            "http://127.0.0.1:8000/students",
            {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(studentData)

            }
        );


        const data = await response.json();


        console.log(data);


        if (response.ok) {

            alert("Student added successfully!");

            form.reset();

            // Refresh student list
            loadStudents();

        } else {

            alert(data.detail);

        }

    } catch (error) {

        console.error(error);

        alert("Could not connect to FastAPI server.");

    }

});



// =============================
// LOAD ALL STUDENTS
// =============================

async function loadStudents() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/students"
        );


        const students = await response.json();


        console.log(students);


        const tableBody =
            document.querySelector("tbody");


        tableBody.innerHTML = "";


        students.forEach(function (student) {

            const row =
                document.createElement("tr");


            row.innerHTML = `

                <td>${student[0]}</td>

                <td>${student[1]}</td>

                <td>${student[2]}</td>

                <td>${student[3]}</td>

                <td>

                    <button
                        onclick="editStudent(
                            ${student[0]},
                            '${student[1]}',
                            ${student[2]},
                            '${student[3]}'
                        )">

                        Edit

                    </button>


                    <button
                        onclick="deleteStudent(${student[0]})">

                        Delete

                    </button>

                </td>

            `;


            tableBody.appendChild(row);

        });


    } catch (error) {

        console.error(error);

    }

}



// =============================
// DELETE STUDENT
// =============================

async function deleteStudent(studentId) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this student?"
    );


    if (!confirmDelete) {

        return;

    }


    try {

        const response = await fetch(
            `http://127.0.0.1:8000/students/${studentId}`,
            {
                method: "DELETE"
            }
        );


        const data = await response.json();


        if (response.ok) {

            alert("Student deleted successfully!");

            // Refresh student list
            loadStudents();

            // Clear search result
            clearSearch();

        } else {

            alert(data.detail);

        }

    } catch (error) {

        console.error(error);

        alert("Could not connect to FastAPI server.");

    }

}



// =============================
// EDIT STUDENT
// =============================

async function editStudent(
    studentId,
    oldName,
    oldAge,
    oldCourse
) {

    const newName =
        prompt("Enter new name:", oldName);


    if (newName === null) {

        return;

    }


    const newAge =
        prompt("Enter new age:", oldAge);


    if (newAge === null) {

        return;

    }


    const newCourse =
        prompt("Enter new course:", oldCourse);


    if (newCourse === null) {

        return;

    }


    const updatedStudent = {

        id: studentId,

        name: newName,

        age: Number(newAge),

        course: newCourse

    };


    try {

        const response = await fetch(
            `http://127.0.0.1:8000/students/${studentId}`,
            {

                method: "PUT",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify(updatedStudent)

            }
        );


        const data = await response.json();


        if (response.ok) {

            alert("Student updated successfully!");

            loadStudents();

            // Search result ko bhi refresh karna
            searchStudent();

        } else {

            alert(data.detail);

        }

    } catch (error) {

        console.error(error);

        alert("Could not connect to FastAPI server.");

    }

}



// =============================
// LOAD STUDENTS WHEN PAGE OPENS
// =============================

loadStudents();



// =============================
// SEARCH STUDENT
// =============================

async function searchStudent() {

    const studentId =
        document.getElementById("searchStudentId").value;


    if (studentId === "") {

        alert("Please enter Student ID.");

        return;

    }


    try {

        const response = await fetch(
            `http://127.0.0.1:8000/students/${studentId}`
        );


        const data = await response.json();


        const searchResult =
            document.getElementById("searchResult");


        if (response.ok) {

            searchResult.innerHTML = `

                <div class="student-result">

                    <h3>Student Found</h3>


                    <p>
                        <strong>ID:</strong>
                        ${data.id}
                    </p>


                    <p>
                        <strong>Name:</strong>
                        ${data.name}
                    </p>


                    <p>
                        <strong>Age:</strong>
                        ${data.age}
                    </p>


                    <p>
                        <strong>Course:</strong>
                        ${data.course}
                    </p>


                    <br>


                    <button
                        onclick="editStudent(
                            ${data.id},
                            '${data.name}',
                            ${data.age},
                            '${data.course}'
                        )">

                        Edit

                    </button>


                    <button
                        onclick="deleteStudent(${data.id})">

                        Delete

                    </button>

                </div>

            `;

        } else {

            searchResult.innerHTML = `

                <div class="student-not-found">

                    <p>${data.detail}</p>

                </div>

            `;

        }


    } catch (error) {

        console.error(error);

        alert("Could not connect to FastAPI server.");

    }

}



// =============================
// CLEAR SEARCH
// =============================

function clearSearch() {

    document.getElementById("searchStudentId").value = "";

    document.getElementById("searchResult").innerHTML = "";

}
