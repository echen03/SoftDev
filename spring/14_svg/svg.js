/*
Ethan Chen; Team Colors <br/>
SoftDev pd1 <br/>
K14 -- Ask Circles [Change || Die] While Moving<br/>
2020-04-01
 */

const svg = document.getElementById("vimage");
const clearButton = document.getElementById("clear");
const moveButton = document.getElementById("move");
const xtraButton = document.getElementById("xtra");
const radius = 20;
const [canvasWidth, canvasHeight] = [svg.clientWidth, svg.clientHeight];
let iterations = 0;
const circles = {};
let animationID;

svg.addEventListener('click', (e) => {
    createNewCircle(e.offsetX, e.offsetY);
});

const handleFirstClick = (e) => {
    // Only want action to be done on the HTMLElement we clicked on, so use currentTarget

    e.currentTarget.setAttribute("fill", "#00FFFF");
    e.currentTarget.addEventListener("click", handleSecondClick);

    // Stop from making more circles and clicking circle underneath
    e.stopPropagation();
};

const handleSecondClick = (e) => {
    // Only remove what the event listener is attached to
    svg.removeChild(e.currentTarget);

    // Make sure circle doesn't go out of bounds
    const [cx, cy] = [Math.random() * (canvasWidth - 2 * radius) + radius, Math.random() * (canvasWidth - 2 * radius) + radius];
    createNewCircle(cx, cy);

    // Stop from making more circles and clicking circle underneath
    e.stopPropagation();
};

const createNewCircle = (cx, cy) => {
    const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    circle.setAttribute("cx", String(cx));
    circle.setAttribute("cy", String(cy));
    circle.setAttribute("r", String(radius));
    circle.setAttribute("fill", "red");
    circle.setAttribute("stroke", "black");
    circle.addEventListener("click", handleFirstClick);
    svg.appendChild(circle);

    circle.setAttribute("id", iterations);
    circles[iterations] = [[cx, cy],[1, 1]];
    iterations++;
};

const move = () => {
    for (circle of svg.children){
        [pos, vel] = circles[circle.getAttribute("id")];
        pos[0] += vel[0];
        pos[1] += vel[1];
        circle.setAttribute("cx", String(pos[0]));
        circle.setAttribute("cy", String(pos[1]));
        if(pos[0] <= radius || pos[0] >= canvasWidth - radius){
            vel[0] *= -1;
        }
        if(pos[1] <= radius || pos[1] >= canvasHeight - radius){
            vel[1] *= -1;
        }
    }
    animationID = window.requestAnimationFrame(move);
};

moveButton.addEventListener("click", () => {
    if(animationID === undefined){
        animationID = window.requestAnimationFrame(move);
    }
});

xtraButton.addEventListener("click", () => {
    for (circle of svg.children){
        circle.setAttribute("fill",'#'+Math.floor(Math.random()*16777215).toString(16));
    }
});
