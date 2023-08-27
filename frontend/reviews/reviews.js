document.getElementById("feedback-form").addEventListener("submit", function (event) {
    event.preventDefault();

    // Fetch form data
    const formData = new FormData(event.target);

    // You can send this data to your server using AJAX or fetch API
    // Example:
    fetch("url-to-your-server-endpoint", {
      method: "POST",
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        // Handle success or display a thank you message
        alert("Thank you for your feedback!");
        // Clear the form
        event.target.reset();
      })
      .catch(error => {
        console.error("Error submitting feedback:", error);
        alert("An error occurred while submitting your feedback. Please try again later.");
      });
  });