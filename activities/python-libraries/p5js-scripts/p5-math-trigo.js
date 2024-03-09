let globalAngle = 0;

new p5(p => {
    let mx = 0;
    let my = 0;

    p.setup = function() {
        p.createCanvas(300, 300);
        mx = 300;
        my = 300;
    }

    function update() {
        if (p.mouseX >= 0 && p.mouseX < p.width && p.mouseY >= 0 && p.mouseY < p.height) {
            mx = p.mouseX;
            my = p.mouseY;
        }
    }

    p.mousePressed = function() {
        update();
    }

    p.mouseDragged = function() {
        update();
    }

    p.draw = function() {
        const dx = mx - p.width/2;
        const dy = my - p.height/2;
        const angle = Math.atan2(dy, dx);
        const radius = p.height/2.5;
        const diameter = 2 * radius;
        const x = Math.cos(angle);
        const y = Math.sin(angle);

        globalAngle = p.radians((p.degrees(angle) + 360) % 360);
        
        p.background(200);
        p.push();
        
        p.translate(p.width/2, p.height/2);
        
        // Draw the axis.
        p.line(-p.width/2, 0, p.width/2, 0);
        p.text("x", p.width/2-10, 10);
        p.text("-1", -radius-15, 10);
        p.text("+1", radius+1, 10);
        p.line(0, p.height/2, 0, -p.height/2);
        p.text("y", 10, p.height/2-10);
        p.text("-1", 10, -radius-10);
        p.text("+1", 10, radius+10);
        
        // Draw the circle.
        p.noFill();
        p.circle(0, 0, diameter);
        
        // Draw the radius and the angle.
        p.stroke("green");
        p.line(0, 0, x*radius, y*radius);
        p.arc(0, 0, radius/2, radius/2, 0, angle);
        p.textAlign(p.CENTER, p.BOTTOM);
        p.text("a", 1.2 * radius/4 * Math.cos(angle/2), 1.2 * radius/4 * Math.sin(angle/2));
        
        // Draw the cos.
        p.stroke("red");
        p.line(0, radius*y, radius*x, radius*y);
        p.textAlign(p.CENTER, p.CENTER);
        p.text("x", radius*x/2, radius*y-10);
        
        // Draw the sin.
        p.stroke("blue");
        p.line(radius*x, 0, radius*x, radius*y);
        p.textAlign(p.LEFT, p.CENTER);
        p.text("y", radius*x+10, radius*y/2);

        // Draw the legend.
        p.textAlign(p.LEFT, p.BOTTOM);
        p.stroke("green");
        let a = (p.degrees(angle) + 360) % 360;
        p.text(`a = ${a.toFixed(0)}`, -p.width/2+15, p.height/2-45);
        p.stroke("red");
        p.text(`x = cos(a) = ${x.toFixed(2)}`, -p.width/2+15, p.height/2-30);
        p.stroke("blue");
        p.text(`y = sin(a) = ${y.toFixed(2)}`, -p.width/2+15, p.height/2-15);

        p.pop();
    }
}, "p5-trigo")
