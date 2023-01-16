var logic = {
    "start" : null,
    "end" : null,
    "lastRefresh": null,
    "localGameStatus": null,
    "step": 0,
}

var connectionData = {
    "visible_board" : "http://127.0.0.1:8000/visible_board",
    "board" : "http://127.0.0.1:8000/board",
    "dig" : "http://127.0.0.1:8000/dig",
    "superdig" : "http://127.0.0.1:8000/superdig",
    "mark" : "http://127.0.0.1:8000/mark",
    "new_game" : "http://127.0.0.1:8000/newgame",
}

var renderMap = {
    "0" : {"symbol" : /*"0️⃣"*/" ", "class" : "cell-desert", "callFlag" : false},
    "1" : {"symbol" : /*"1️⃣"*/"1", "class" : "cell-pressed", "callFlag" : false},
    "2" : {"symbol" : /*"2️⃣"*/"2", "class" : "cell-pressed", "callFlag" : false},
    "3" : {"symbol" : /*"3️⃣"*/"3", "class" : "cell-pressed", "callFlag" : false},
    "4" : {"symbol" : /*"4️⃣"*/"4", "class" : "cell-pressed", "callFlag" : false},
    "5" : {"symbol" : /*"5️⃣"*/"5", "class" : "cell-pressed", "callFlag" : false},
    "6" : {"symbol" : /*"6️⃣"*/"6", "class" : "cell-pressed", "callFlag" : false},
    "7" : {"symbol" : /*"7️⃣"*/"7", "class" : "cell-pressed", "callFlag" : false},
    "8" : {"symbol" : /*"8️⃣"*/"8", "class" : "cell-pressed", "callFlag" : false},
    "E" : {"symbol" : /*"⬜"*/" ", "class" : "cell", "callFlag" : true},
    "B" : {"symbol" : "💣", "class" : "cell-pressed", "callFlag" : false},
    "Q" : {"symbol" : "❔", "class" : "cell", "callFlag" : true},
    "X" : {"symbol" : "❌", "class" : "cell", "callFlag" : false},
}


var renderCell = function(content, row, col){
    return "<div class='"+renderMap[content].class+"' id-row='"+row+"' id-col='"+col+"' >"+renderMap[content].symbol+"</div>";
    
}


var renderGame = function(obj){
    var rows = obj.board.length;
    var cols = obj.board[0].length;
    var gameStatus = obj.status;

    if(gameStatus == "playing"){
        if(logic.localGameStatus == null){
            logic.localGameStatus = "playing";
        }
        logic.start = obj.startTime;
        logic.lastRefresh = Math.round(Date.now()/1000);
    }

    if(gameStatus == "loser" || gameStatus == "winner"){
        logic.start = obj.startTime;
        logic.end = obj.endTime;
        logic.localGameStatus = obj.status;
    }


    var cells = obj.board.map(
        function(r,j){
            var row = r.map(
                function(c,i){
                    return renderCell(c,j,i);
                }
            ).join('');

            return '<div class="row">'+row+'</div>';
        }
    ).join('');


    document.getElementById("wrapper").innerHTML = "<div class='board'>"+cells+"</div>";

    var cells = document.getElementsByClassName("cell");
    for (const cell of cells) {
        cell.addEventListener("mousedown", function(e){
            // Only applied to class cell and not his childrens
            // if(e.target.className != 'cell')

            if(e.button == 0){
                // Left click (main click)
                var row = e.target.attributes["id-row"].value;
                var col = e.target.attributes["id-col"].value;
                digCell(row, col);
                console.log("Celda "+row+","+col+".");
            }

            if(e.button == 2){
                // Right click (menu click)
                var row = e.target.attributes["id-row"].value;
                var col = e.target.attributes["id-col"].value;
                markCell(row, col);
                console.log("Celda "+row+","+col+".");
            }
        });
    }

    var cellsPressed = document.getElementsByClassName("cell-pressed");
    for (const cell of cellsPressed) {
        cell.addEventListener("mousedown", function(e){
            // Only applied to class cell-pressed and not his childrens
            // if(e.target.className != 'cell')

            if(e.button == 1){
                // Middle click (wheel click)
                var row = e.target.attributes["id-row"].value;
                var col = e.target.attributes["id-col"].value;
                superDigCell(row, col);
                console.log("Celda "+row+","+col+".");
            }
        });
    }
};


var generateGame = function(){
    var initialBoard = null;

    fetch(connectionData.visible_board, {cache: "no-store"}).then(function (response) {
        // The API call was successful!
        return response.json();
    }).then(function (data) {
        // This is the JSON from our response
        renderGame(data);
    }).catch(function (err) {
        // There was an error
        console.warn('Something went wrong.', err);
    });
    
};


var digCell = function(row, col){
    fetch(connectionData.dig+'/'+row+'/'+col, 
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        cache: 'no-store',
        // body: JSON.stringify({ "id": 78912 })
    }).then(function(response){
        return response.json();
    }).then(function(data){
        var currentBoard = document.getElementsByClassName("board");
        currentBoard[0].remove();
        var ts = Date.now();
        renderGame(data);
    });

};


var superDigCell = function(row, col){
    fetch(connectionData.superdig+'/'+row+'/'+col, 
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        cache: 'no-store',
        // body: JSON.stringify({ "id": 78912 })
    }).then(function(response){
        return response.json();
    }).then(function(data){
        var currentBoard = document.getElementsByClassName("board");
        currentBoard[0].remove();
        var ts = Date.now();
        renderGame(data);
    });

};


var markCell = function(row, col){
    fetch(connectionData.mark+'/'+row+'/'+col,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        cache: 'no-store',
        // body: JSON.stringify({ "id": 78912 })
    }).then(function(response){
        return response.json();
    }).then(function(data){
        var currentBoard = document.getElementsByClassName("board");
        currentBoard[0].remove();
        var ts = Date.now();
        renderGame(data);
    });

};


var newGame = function(row, col){
    fetch(connectionData.new_game,
    {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        cache: 'no-store',
        // body: JSON.stringify({ "id": 78912 })
    }).then(function(response){
        return response.json();
    }).then(function(data){
        logic = {
            "start" : null,
            "end" : null,
            "lastRefresh": null,
            "localGameStatus": null,
            "step": 0,
        };
        var currentBoard = document.getElementsByClassName("board");
        currentBoard[0].remove();
        renderGame(data);
    });

};


var refreshTimer = function(){
    var calculatedTime = 0;
    if(logic.localGameStatus == "playing"){
        calculatedTime = Math.round(Date.now()/1000)-logic.start;
    }
    
    if(logic.localGameStatus == "loser" || logic.localGameStatus == "winner"){
        calculatedTime = logic.end-logic.start;
    }

    var timer = document.getElementsByClassName("timer");
    // timer[0].innerHTML = "<h2>"+(Math.random() + 1).toString(36).substring(4)+"</h2>";
    timer[0].innerHTML = "<h2>"+calculatedTime+"</h2>";

}


var worker = function(){
    logic.step += 1;
    logic.step = logic.step % 10

    refreshTimer();

}


window.oncontextmenu = function (){
    return false;     // cancel default menu
}


window.onload = function (){
    generateGame();
    setInterval(worker, 1000);
};