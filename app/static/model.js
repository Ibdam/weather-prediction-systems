document.addEventListener("DOMContentLoaded", () => {
  const rainPredictionForm = document.getElementById("rainPredictionForm");

  // Handle form submission
  rainPredictionForm.addEventListener("submit", (event) => {
      event.preventDefault();

      // Capture input data
      const formData = new FormData(rainPredictionForm);
      const data = {};
      formData.forEach((value, key) => {
          data[key] = value;
      });

      // Simulate prediction logic (replace with real logic)
      alert("Prediction submitted successfully! We'll analyze your data.");
      console.log("Submitted Data:", data);
  });
});
