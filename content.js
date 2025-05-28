console.log("✅ BS Detector active.");

const MIN_LENGTH = 500;
const API_URL = "https://web-production-da137.up.railway.app/summarize";

// Scan for long posts every 2 seconds
setInterval(() => {
  const posts = document.querySelectorAll('[data-ad-preview="message"]');

  posts.forEach((post) => {
    const text = post.innerText;

    if (text.length > MIN_LENGTH && !post.classList.contains("bs-injected")) {
      injectButton(post, text);
      post.classList.add("bs-injected");
    }
  });
}, 2000);

function injectButton(postElement, postText) {
  const button = document.createElement("button");
  button.textContent = "🧠 Summarize BS?";
  button.style.cssText = `
    margin-top: 8px;
    background-color: #ff69b4;
    color: white;
    border: none;
    border-radius: 6px;
    padding: 6px 12px;
    font-size: 14px;
    cursor: pointer;
  `;

  button.addEventListener("click", () =>
    handleSummarize(postElement, postText)
  );
  postElement.appendChild(button);
}

async function handleSummarize(postElement, postText) {
  // Create summary box
  const summaryBox = document.createElement("div");
  summaryBox.textContent = "🧠 Summarizing...";
  summaryBox.style.cssText = `
    margin-top: 10px;
    background: rgba(0,0,0,0.7);
    color: white;
    padding: 10px;
    border-radius: 8px;
    font-size: 14px;
  `;
  postElement.appendChild(summaryBox);

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: postText }),
    });

    const data = await res.json();

    if (data.error) {
      summaryBox.textContent = "❌ Error: " + data.error;
    } else {
      summaryBox.innerHTML = `
        <strong>Summary:</strong> ${data.summary}<br/>
        <strong>BS Meter:</strong> ${data.bs_score}% 💩
      `;
    }
  } catch (err) {
    summaryBox.textContent = "❌ Failed to summarize.";
    console.error(err);
  }
}
