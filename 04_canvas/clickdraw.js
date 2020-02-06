
// retrieve node in DOM via ID

var c = document.getElementById( "slate");

console.log( 'one');



// instantiate a CanvaRenderingContext2D object

var ctx = c.getContext( "2d");



// invoke interface methods

ctx.fillStyle = "#ff0000";

ctx.fillRect( 50, 50, 100, 200);



var clear = document.getElementById( 'clear');

var toggle = document.getElementById( 'toggle');

var mode = 'box';



clear.addEventListener( 'click', function( e){

    e.preventDefault()

});



toggle.addEventListener( 'click', function( e){

    if( mode == "box"){

	mode = "dot";

    }

    else{

	mode = "box";

    }

    toggle.innerHTML = mode;

});



c.addEventListener( 'click', function( e){

    var xcor = e.offsetX;

    var ycor = e.offsetY;

    if( mode=="box"){

	ctx.fillRect( xcor, ycor, 50, 50);

    }

    else{

	ctx.fillStyle="black";

	ctx.beginPath();

	ctx.ellipse( xcor, ycor, 5, 5, (Math.PI / 4), 0, (2 * Math.PI));

	ctx.stroke();

	ctx.fill();

    }

});
