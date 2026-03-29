const API_URL = window.API_URL || "http://localhost:5000";

// Health check — colour the nav dot
fetch(`${API_URL}/api/health`)
  .then(r => r.ok ? r.json() : Promise.reject())
  .then(() => {
    const dot = document.getElementById("status-dot");
    dot.classList.add("ok");
    dot.title = "API is healthy";
  })
  .catch(() => {
    const dot = document.getElementById("status-dot");
    dot.classList.add("err");
    dot.title = "API unreachable";
  });

// Contact form
document.getElementById("contact-form").addEventListener("submit", async e => {
  e.preventDefault();
  const feedback = document.getElementById("form-feedback");
  const payload = {
    name:    document.getElementById("name").value.trim(),
    email:   document.getElementById("email").value.trim(),
    message: document.getElementById("message").value.trim(),
  };

  try {
    const res = await fetch(`${API_URL}/api/contact`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    if (res.ok) {
      feedback.textContent = data.message;
      feedback.className = "success";
      e.target.reset();
    } else {
      feedback.textContent = data.error || "Something went wrong.";
      feedback.className = "error";
    }
  } catch {
    feedback.textContent = "Network error — please try again.";
    feedback.className = "error";
  }
});
