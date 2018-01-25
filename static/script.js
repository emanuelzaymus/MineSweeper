$(document).ready(function () {

    var $container = $("#main-container");
    var gameArray = [];

    $(document).ready(loadNewGame());

    function loadNewGame(){
        $.ajax({
            type: 'GET',
            url: '/newGameData',
            success: createGameGrid,
            error: function() {
                alert('error loading data');
            }
        });
    }

    function createGameGrid(data)  {
        gameArray = data.data;
        $container.css("grid-template-columns", "repeat(" + data.columns + ", auto)");

        for (let i = 0; i < gameArray.length; i++) {
            for (let j = 0; j < gameArray[i].length; j++) {
                $container.append(' <img id="'+i+'x'+j+'" src="/static/minesweeper_img/unclicked.png" alt="field" class="unclicked" width="40" height="40"> ');
            }
        }
        $container.css('visibility','visible');
    }

    function updateGameGrid() {
        for (let i = 0; i < gameArray.length; i++) {
            for (let j = 0; j < gameArray[i].length; j++) {
                if (gameArray[i][j].clickable) {
                    var $field = $container.find("#"+i+"x"+j);
                    $field.attr('src', ('/static/minesweeper_img/' + gameArray[i][j].type +'.png'));
                    $field.removeClass("unclicked");
                }
            }
        }
    }

    $("#new-game-button").on("click", function() {
        $container.css('visibility','hidden');
        $container.html("");
        gameArray = [];
        loadNewGame();
    });

    $('#main-container').on("click", '.unclicked', function() {
        var str = $(this).attr('id');
        var y, x = str.split('x');
        console.log(y + " - " + x + " was clicked");

        postData = {
            "x": parseInt(y),
            "y": parseInt(x),
            "data": gameArray
        }

        $.ajax({
            type: 'POST',
            url: '/postMoveData',
            contentType: 'application/json',
            data: JSON.stringify(postData),
            success: function(data) {
                console.log(data);
                gameArray = data.data;
                updateGameGrid();
            },
            error: function() {
                alert('error sending data');
            }
        });
    });


});