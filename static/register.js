//event listerner waits for html to load


//reggistering new user


document.addEventListener("DOMContentLoaded", () => {

    const registerForm = document.getElementById("registerForm");
    console.log("registerForm is:", registerForm);

    //event listener to wait for user to submit form
    registerForm.addEventListener("submit", (event) => {

        event.preventDefault(); // Prevent the default form submission behavior
        console.log("Form submitted!");

        //we gather data from the form
        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;


        //create user object to pass to api
        const userData = {
            username: username,
            email: email,
            password: password
        };

        //call the register function to send data to api
        fetch('http://127.0.0.1:5000/api/register', {
                method: 'POST',
                headers: {
                    //tells server is sending json
                    'Content-Type': 'application/json'
                },
                //sends the user data as json
                body: JSON.stringify(userData)
            })
            //cconvert response to json
            .then(response => response.json())

        //handles what comes back from the api
        .then(data => {
            console.log('Success:', data);

            if (!data.error) {
                console.log('Redirecting to login page...');
                window.location.href = '/login';
            } else {
                console.log('Registration failed:', data.error);
                alert('Registration failed: ' + (data.error || 'Unknown error'));
            }
        })

        //if there is an error with the fetch
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred during registration. Please try again later.');
        });
    });
});


//end of registering new user


//start of login existing user
document.addEventListener("DOMContentLoaded", () => {

    const loginForm = document.getElementById("loginForm");

    loginForm.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent the default form submission behavior
        //get the data

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        //make an object for user data

        const loginData = {
            username: username,
            password: password
        };

        //send to api
        fetch('http://127.0.0.1:5000/api/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(loginData)
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json(); //of response is ok convert to json




            })
            .then(data => {
                console.log('Login Success:', data);

                if (data.access_token) {
                    // Store the token in local storage 
                    localStorage.setItem('access_token', data.access_token);

                    // Redirect to homepage
                    window.location.href = '/';
                } else {
                    alert('Login failed: ' + data.error);
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                alert('An error occurred during login. Please try again later.');
            });
    });
});

//end of login existing user

//checking if user is logged in
const token = localStorage.getItem('access_token');
if (token) {
    console.log('User is logged in with token:', token);
    document.getElementById('profileSection').innerHTML = "Welcome, Chris!";
} else {

    console.log('User is not logged in');
    document.getElementById("profileSection").innerHTML = '<a href="/login">Sign in</a>';
}