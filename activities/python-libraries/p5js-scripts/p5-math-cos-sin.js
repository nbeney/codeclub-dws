new p5(p => {
    let x;
    let y;

    p.setup = function() {
        p.createCanvas(600, 300);
        mx = 100;
        my = 100;
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
        const freq = p.map(p.constrain(mx, 0, p.width), 0, p.width, 0.1, 10);  // frequency
        const amp = p.map(p.constrain(my, 0, p.height), 0, p.height, -p.height/3, p.height/3);  // amplitude
        
        p.background(200);
        p.text(`amp: ${amp.toFixed(1)}\nfreq: ${freq.toFixed(1)}`, 10, 10);

        p.text(p.degrees(globalAngle).toFixed(0), 10, 70);

        p.push();
        p.translate(0, p.height/2);
        
        // Draw the axis.
        p.line(0, 0, p.width, 0);
        p.text("x", p.width-10, 10);
        p.line(1, p.height/2, 1, -p.height/2);
        p.text("y", 10, p.height/2-10);
        
        // Draw the cos graph.
        p.stroke("red");
        let dx = 2;
        let px, py;
        for (let x = 0; x < p.width; x += dx) {
            let y = amp * Math.cos(p.radians(freq * x));
            if (px !== undefined) {
                p.line(px, py, x, y);
            }
            px = x;
            py = y;
        }
        
        // Draw the global angle.
        x = globalAngle;
        yCos = amp * Math.cos(freq * x);
        ySin = amp * Math.sin(freq * x);
        p.stroke("grey");
        p.line(p.degrees(x), -p.height/2, p.degrees(x), p.height/2);
        p.push();
        p.strokeWeight(5);
        p.stroke("red");
        p.point(p.degrees(x), yCos);
        p.stroke("blue");
        p.point(p.degrees(x), ySin);
        p.pop();
        
        // Draw the sin graph.
        p.stroke("blue");
        px = undefined;
        py = undefined;
        for (let x = 0; x < p.width; x += dx) {
            let y = amp * Math.sin(p.radians(freq * x));
            if (px !== undefined) {
                p.line(px, py, x, y);
            }
            px = x;
            py = y;
        }
        
        // Draw the legend.
        p.textAlign(p.CENTER, p.BOTTOM);
        p.stroke("red");
        p.text(`y = amp * cos(freq * x)`, p.width/2, p.height/2-30);
        p.stroke("blue");
        p.text(`y = amp * sin(freq * x)`, p.width/2, p.height/2-15);

        p.pop();
    }
}, "p5-cos-sin")
