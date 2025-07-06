//Get elements
const startButton = document.getElementById("startButton");
const timerDisplay = document.getElementById("timerDisplay");
const stopButton = document.getElementById("stopButton");
const resetButton = document.getElementById("resetButton");
const authButton = document.getElementById("auth");

//timer variables
let duration = 25 * 60;
let timeLeft = duration;
let timerInterval = null;


// timer functionality starts


startButton.addEventListener("click", () => {
    startTimer();
});

stopButton.addEventListener("click", () => {
    stopTimer();
});

resetButton.addEventListener("click", () => {
    resetTimer();
});

function startTimer() {
    if (timerInterval) {
        clearInterval(timerInterval);
    }

    timerInterval = setInterval(() => {
        timeLeft--;

        timerDisplay.textContent = formatTime(timeLeft);

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            timerInterval = null;
            alert("Time's up!");
        }
    }, 1000);
}


function stopTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
}

function resetTimer() {
    clearInterval(timerInterval); // Stop the timer if it's running
    timerInterval = null;
    timeLeft = duration; // Reset the time
    timerDisplay.textContent = formatTime(timeLeft); // Update the display to show 25:00
}
// Format time in MM:SS

function formatTime(seconds) {
    let minutes = Math.floor(seconds / 60);
    let secs = seconds % 60;
    if (secs < 10) {
        secs = "0" + secs;
    }
    return `${minutes}:${secs}`;
}
//timer functionality ends


// Authorization functionality starts
authButton.addEventListener("click", () => {
    // Simulate an authorization process
    alert("Authorization process started. This is a placeholder.");
});

function SignIn() {

}