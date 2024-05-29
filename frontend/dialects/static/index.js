function startProgress() {
    var buttonContainer = document.getElementById("buttonContainer");
    var loadingContainer = document.getElementById("loadingContainer");
    var outputContainer = document.getElementById("outputContainer");
    var progressBar = document.getElementById("progressBar");
    var width = 0;
    var interval = setInterval(frame, 50); // Increase the width every 50 milliseconds

    // Show the button container
    buttonContainer.style.visibility = "visible";
    // Show the loading container
    loadingContainer.style.display = "block";

    function frame() {
        if (width >= 100) {
            clearInterval(interval);
            // Hide the loading container
            loadingContainer.style.display = "none";
            // Show the output container
            outputContainer.style.display = "block";
            // Display the output file
            displayOutputFile();
            // Show the download button
            downloadButton.style.display = "block";
        } else {
            width++;
            progressBar.style.width = width + "%";
            if (width === 100) {
                // Call the function to display the output file
              displayOutputFile();
              // Show the download button
              downloadButton.style.display = "block";  
            }
        }
    }
}


function displayOutputFile() {
  // Replace 'file.pdf' with the path to your file
  var outputFileUrl = '/home/talha/turbo-dialect/verilog/pe.v';
  var outputFile = document.getElementById("outputFile");
  
  outputFile.src = outputFileUrl;
  alert("File is ready for download");

}

function downloadFile() {
  // var downloadButton = document.getElementById("downloadButton");
  var fileUrl = '/home/talha/turbo-dialect/verilog/pe.v'; // Replace with the correct URL
  
  var link = document.createElement('a');
  link.href = fileUrl;
  link.download = fileUrl.split('/').pop();
  
  document.body.appendChild(link);
  
  link.click(); // Programmatically trigger the download
  document.body.removeChild(link); // Clean up the temporary link element
}

// Function to display the first popup
window.onload = function() {
  var popup1 = document.getElementById('popup1');
  popup1.style.display = 'block';
}

// Function to close the first popup and display the second popup
function closePopup1() {
  var popup1 = document.getElementById('popup1');
  popup1.style.display = 'none';
  var popup2 = document.getElementById('popup2');
  popup2.style.display = 'block';
}

// Function to close the second popup
function closePopup2() {
  var popup2 = document.getElementById('popup2');
  popup2.style.display = 'none';
}