let currentInput = document.querySelector(".currentInput");
let outputScreen = document.querySelector(".outputScreen");
let buttons = document.querySelectorAll("button");
let erasebtn = document.querySelector("#erase");
let clearbtn = document.querySelector("#clear");
let evaluate = document.querySelector("#evaluate");
let realTimeScreenValue = [];

clearbtn.addEventListener("click", () => {
  realTimeScreenValue = [""];
  outputScreen.innerHTML = 0;
  currentInput.className = "currentInput";
  outputScreen.className = "outputScreen";
  outputScreen.style.color = " rgba(150, 150, 150, 0.87)";
});

buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    if (!btn.id.match("erase")) {
      realTimeScreenValue.push(btn.value);
      currentInput.innerHTML = realTimeScreenValue.join("");

      if (btn.classList.contains("num_btn")) {
        outputScreen.innerHTML = eval(realTimeScreenValue.join(""));
      }
    }

    if (btn.id.match("erase")) {
      realTimeScreenValue.pop();
      currentInput.innerHTML = realTimeScreenValue.join("");
      outputScreen.innerHTML = eval(realTimeScreenValue.join(""));
    }

    if (btn.id.match("evaluate")) {
      currentInput.className = "outputScreen";
      outputScreen.className = "currentInput";
      outputScreen.style.color = "white";
    }

    if (typeof eval(realTimeScreenValue.join("")) == "undefined") {
      outputScreen.innerHTML = 0;
    }
  });
});
