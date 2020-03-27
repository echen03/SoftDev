var pic = document.getElementById("vimage");


var c = document.createElementNS("http://www.w3.org/2000/svg", "rect");
c.setAttribute( "x", 0 );
c.setAttribute( "y", 0 );
c.setAttribute( "width", 500 );
c.setAttribute( "height", 500 );
c.setAttribute( "fill", "white" );

pic.appendChild(c);
