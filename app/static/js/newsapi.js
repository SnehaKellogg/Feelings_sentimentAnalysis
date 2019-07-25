
// For particular topic:

var searchinput = 'laser';
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
var date = yyyy + '-' + mm + '-' + dd; //2017-12-01
// const apikey = `b2ce97241188410e9ecc5d06f604130f`
var url = 'https://newsapi.org/v2/everything?' + // everything for all the news
    `q=${searchinput}&from=${date}&sortBy=popularity&apiKey=${apiKey}`;
   
console.log(url);
var req = new Request(url);

fetch(req).then(function (response) {
    return response.json();
})
    .then(function (newsJson) {
        console.log(newsJson['articles']);
        var newsarticles = newsJson['articles']
        console.log(newsarticles)
        var col = [];
        for (var i = 2; i < newsarticles.length -3; i++) {
            for (var key in newsarticles[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                    console.log(key);
                }
            }
        }
        var table = document.createElement("table");
        var tr = table.insertRow(-1);                   // TABLE ROW.

        for (var i = 2; i < col.length -3; i++) {
            var th = document.createElement("th");      // TABLE HEADER.
            th.innerHTML = col[i];
            tr.appendChild(th);
        }
        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (var i = 0; i < newsarticles.length; i++) {

            tr = table.insertRow(-1);

            for (var j = 2; j < col.length -3; j++) {
                var tabCell = tr.insertCell(-1);
                tabCell.innerHTML = newsarticles[i][col[j]];
            }
            
        }
        var divContainer = document.getElementById("news");
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
    });
    


// // Top and breaking news:
// var url = 'https://newsapi.org/v2/top-headlines?' +
// 'country=us&' +
// 'apiKey=b2ce97241188410e9ecc5d06f604130f';
// var req = new Request(url);
// fetch(req)
// .then(function(response) {
// console.log(response.json());
// })


// // From particular news Source:


// var url = 'https://newsapi.org/v2/top-headlines?' +
//           'sources=bbc-news&' +
//           'apiKey=b2ce97241188410e9ecc5d06f604130f';
// var req = new Request(url);
// fetch(req)
//     .then(function(response) {
//         console.log(response.json());
//     })


var tblrows = document.getElementsByTagName('tr');

for(i=0;i<tblrows.length;i++){
    if(i%2==0) tblrows[i].style.backgroundColor = '#6d7fcc'
}