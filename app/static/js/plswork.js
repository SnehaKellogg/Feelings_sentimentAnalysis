// grab references to the input element and the output div
var text = d3.select("#text");
var output = d3.select("#output");

function counter(text) {

  // convert text to lowercase characters (chars)
  var chars = text
    .toLowerCase()
    .replace(/\s+/g, "")
    .split("");

  var counts = {};
  chars.forEach((char) => {
    if (char in counts) {
      counts[char] += 1;
    }
    else {
      counts[char] = 1;
    }
  });

  return counts;
}

// Function to handle input change
function handleChange(event) {
  // grab the value of the input field
  const value = d3.event.target.value;
  console.log(value);
  document.getElementById("output").innerHTML = "You searched for <code>&lt;" + value+ "&gt;</code>";
  }
text.on("change", handleChange);


var globalVariable={
    searchword: value
 };




//   // clear the existing output
//   output.html("");
//   document.getElementById("output").innerHTML = "You searched for" + value;

//   var frequencyCounts = counter(value);
//   Object.entries(frequencyCounts).forEach(([key, value]) => {
//     var li = output.append("li").text(`${key}: ${value}`);
//   });


// text.on("change", handleChange);


// node.addEventListener("keyup", function(event) {
//     if (event.key === "Enter") {
//         var x = document.getElementById("inputbutton");
//     y = x.elements["inputbutton"].value;
//     document.getElementById("searched").innerHTML = "You searched for" + y;
//     console.log(x);
//     console.log(y)
//     }
// });
// function input() {
//     var x, y;
//     var x = document.getElementById("inputbutton");
//     y = x.elements["placeholder"].value;
//     document.getElementById("searched").innerHTML = "You searched for" + y;
//     console.log(x);
//     console.log(y)
// };