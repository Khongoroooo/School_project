const loginBtn = document.getElementById("loginBtn");
const loginText = document.getElementById("loginText");

loginBtn.onclick = () => {
  // Харагдах эсэхийг toggle хийх
  if (loginText.style.display === "block") {
    loginText.style.display = "none";
  } else {
    loginText.style.display = "block";
  }
};
