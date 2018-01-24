/* var number = 0;

$(document).ready(function () {
    console.log('heloo on ready');
    $.ajax({
        url: '/message',
        method: 'GET'
    }).done(function (data) {
        console.log(data);
        $('#message').text(data.text);
    }).fail(function (err) {
        console.error(err);
    });

    setInterval(increment, 1000);    

});
console.log('heloo');

function increment() {
    $.ajax({
        url: '/post',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            'number': number
        })
    }).done(function (data) {
        console.log(data);
        number = data.number;
        $('#message').text(number);
    }).fail(function (err) {
        console.error(err);
    });
} */

var $container = $("#main-container");
var gameArray = [];

$(document).ready(function(){
    console.log("v metode");
    $.ajax({
        type: 'GET',
        url: '/newGameData',
        success: createGameGrid
    });

});

function createGameGrid(data)  {
    console.log(data);
    gameArray = data.data;
    $container.css("grid-template-columns", "repeat(" + data.columnsCount + ", auto)");

    for (let i = 0; i < gameArray.length; i++) {
        for (let j = 0; j < gameArray[i].length; j++) {
            $container.append(' <img id="'+i+'x'+j+'" src="/static/minesweeper_img/unclicked.png" alt="unclicked" width="40" height="40"> ');
            console.log(gameArray[i][j].type);
        }
    }
}

function updateGameGrid() {
    for (let i = 0; i < gameArray.length; i++) {
        for (let j = 0; j < gameArray[i].length; j++) {
            if (!gameArray[i][j].clickable) {
                console.log("#"+i+"x"+j);
                $container.find("#"+i+"x"+j).attr('src', ('/static/minesweeper_img/' + gameArray[i][j].type +'.png'));
            }
        }
    }
}
