$(document).ready(function () {
    var $container = $('#main-container');
    var jsonData;
    var gameArray = [];

    $(document).ready(loadNewGame());

    function loadNewGame(){
        $.ajax({
            type: 'GET',
            url: '/newGameData',
            success: function(data) {
                storeData(data);
                createGameGrid();
            },
            error: function() {
                alert('error loading data');
            }
        });
    }

    function storeData(data) {
        console.log(data)
        jsonData = data;
        gameArray = data.data;
    }

    function showMassage(message) {
        if (message == 'won') {
            alert('Congratulations, You Won!');
        } else if (message == 'lost') {
            alert('You Lost... Try it one more time!');
        }
    }

    function createGameGrid() {
        $container.css('grid-template-columns', 'repeat(' + jsonData.columns + ', auto)');
        gameArray.forEach(function(row, i) {
            row.forEach(function(field, j) {
                $container.append('<img id="'+i+'x'+j+'" class="unclicked" src="/static/minesweeper_img/unclicked.png" alt="field" width="40" height="40">');
            });
        });
        $container.css('visibility','visible');
        $('#count-of-mines').text(jsonData.countOfMines);
    }

    function updateGameGrid() {
        for (var i = 0; i < jsonData.rows; i++) {
            for (var j = 0; j < jsonData.columns; j++) {
                if (!gameArray[i][j].clickable) {
                    var $field = $container.find('#'+i+'x'+j);
                    if ($field.hasClass('unclicked')) {
                        $field.attr('src', ('/static/minesweeper_img/' + gameArray[i][j].type +'.png'));
                        $field.removeClass('unclicked');
                    }
                }
            }
        }
        $('#count-of-mines').text(jsonData.countOfMines);
    }

    $('#new-game-button').on('click', function() {
        $container.css('visibility','hidden');
        $container.html('');
        loadNewGame();
    });

    $container.on('click', '.unclicked', function() {
        var str = $(this).attr('id');
        var clickedXY = str.split('x');
        if (gameArray[clickedXY[0]][clickedXY[1]].marked) {
            return;
        }
        console.log(clickedXY[0] + ' - ' + clickedXY[1] + ' was clicked');

        jsonData.clickedY = parseInt(clickedXY[0]);
        jsonData.clickedX = parseInt(clickedXY[1]);
        jsonData.data = gameArray;

        $.ajax({
            type: 'POST',
            url: '/postMoveData',
            contentType: 'application/json',
            data: JSON.stringify(jsonData),
            success: function(data) {
                storeData(data);
                updateGameGrid();
                showMassage(data.message);
            },
            error: function() {
                alert('error sending data');
            }
        });
    });

    $container.on('contextmenu','.unclicked', function(event) {
        event.preventDefault();
        var str = $(this).attr('id');
        var clickedXY = str.split('x');
        console.log(clickedXY[0] + ' - ' + clickedXY[1] + ' RIGHT CLICK');

        var field = gameArray[clickedXY[0]][clickedXY[1]];
        if (!field.marked) {
            $(this).attr('src', ('/static/minesweeper_img/flag.png'));
            jsonData.countOfMines--;
        } else {
            $(this).attr('src', ('/static/minesweeper_img/unclicked.png'));
            jsonData.countOfMines++;
        }
        field.marked = !field.marked;
        updateGameGrid();
    });


});