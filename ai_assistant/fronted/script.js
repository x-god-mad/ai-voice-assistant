const activateBtn = document.getElementById('activateBtn');
const responseDiv = document.getElementById('response');
const waveCanvas = document.getElementById('waveCanvas');
const canvasCtx = waveCanvas.getContext('2d');

// Set up canvas dimensions
waveCanvas.width = waveCanvas.offsetWidth;
waveCanvas.height = waveCanvas.offsetHeight;

// Web Audio API variables
let audioContext, analyser, microphone, dataArray;

// Start listening
activateBtn.addEventListener('click', () => {
    const question = prompt("Ask me anything:");
    if (question) {
        fetch('http://127.0.0.1:5000/ask', { // Change URL to your Railway deployment URL
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        })
        .then(response => response.json())
        .then(data => {
            responseDiv.innerText = data.answer || "I couldn't understand. Please try again.";
        })
        .catch(error => {
            console.error('Error:', error);
            responseDiv.innerText = "Error contacting AI backend!";
        });
    }
});
