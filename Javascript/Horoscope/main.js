let birthMonth = "January"
let fortunes = [
    "You will have great success this year!",
    "Expect some unexpected surprises!",
    "Your hard work will pay off soon.",
    "Stay positive and good things will come your way.",
    "New opportunities will arise in the near future.",
    "Take risks and you will be rewarded.",
    "Be patient, good things take time to unfold.",
    "Travel plans are on the horizon."
];
let rndm = Math.floor(Math.random() * fortunes.length);


console.log("You birth month is " + birthMonth)

if (birthMonth === "January") {
  console.log("Your symbol is a CAPRICORN ♑  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "February") {
  console.log("Your symbol is a Aquarius ♒  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "March") {
  console.log("Your symbol is a Pisces ♓  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "May") {
  console.log("Your symbol is a Taurus ♉  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "June") {
  console.log("Your symbol is a Gemini ♊  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "July") {
  console.log("Your symbol is a Cancer ♋  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "August") {
  console.log("Your symbol is a Leo ♌  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "September") {
  console.log("Your symbol is a Virgo ♍  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "October") {
  console.log("Your symbol is a Libra ♎  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "November") {
  console.log("Your symbol is a Scorpio ♏  and your fortune says "+ fortunes[rndm])
} else if (birthMonth === "December") {
  console.log("Your symbol is a Sagittarius ♐  and your fortune says "+ fortunes[rndm])
}
