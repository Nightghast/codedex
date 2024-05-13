const memeArray = [
    "https://i.imgur.com/bSi4xLb.png",
    "https://i.imgur.com/6y0G7N0.png",
    "https://i.imgur.com/LXnRao1.png",
    "https://i.imgur.com/Qqoxh1N.png"
  ];

const captionsArray = [
    "When people ask me stupid questions, it is my legal obligation to give a sarcastic remark.",
    "I’m not saying I hate you, what I’m saying is that you are literally the Monday of my life.",
    "Silence is golden. Duct tape is silver.",
    "I am busy right now, can I ignore you some other time?",
    "Find your patience before I lose mine."
]

const imgElem = document.getElementById("random-meme");
const headElem = document.getElementById("random-caption");
const butElem = document.getElementById("generator-button");

butElem.addEventListener("click", function() {
    const rndmIndex = Math.floor(Math.random() * memeArray.length)
    const rndmIndex2 = Math.floor(Math.random() * captionsArray.length)
    imgElem.src = memeArray[rndmIndex];
    headElem.innerText = captionsArray[rndmIndex2];
})