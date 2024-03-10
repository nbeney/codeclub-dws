{
    let sliderWidth;
    let labelWidth;

    new p5(p => {
        p.setup = function() {
            p.createCanvas(300, 188);

            let divContainer = p.createDiv();
            p.createSpan("Width: ").parent(divContainer);
            sliderWidth = p.createSlider(100, 400, 300, 10).parent(divContainer);
            p.createSpan("   ").parent(divContainer); // spacer
            labelWidth = p.createSpan("???").parent(divContainer);
        }

        p.draw = function() {
            const theWidth = sliderWidth.value();

            labelWidth.html(theWidth);
            p.resizeCanvas(theWidth, theWidth / 1.6);

            p.background("grey");
            p.noStroke();
            p.fill("red");
            p.rect(0, 0, p.width / 3, p.height);
            p.fill("white");
            p.rect(1 / 3 * p.width, 0, p.width / 3, p.height);
            p.fill("blue");
            p.rect(2 / 3 * p.width, 0, p.width / 3, p.height);
            // Frame
            p.noFill();
            p.stroke(0);
            p.rect(1, 1, p.width-1, p.height-1);
        }
    }, "p5-good-relative");

    new p5(p => {
        p.setup = function() {
            p.createCanvas(300, 188);
        }

        p.draw = function() {
            const theWidth = sliderWidth.value();

            p.resizeCanvas(theWidth, theWidth / 1.6);

            p.background("grey");
            p.noStroke();
            p.fill("red");
            p.rect(0, 0, 100, 188);
            p.fill("white");
            p.rect(100, 0, 100, 188);
            p.fill("blue");
            p.rect(200, 0, 100, 188);
            // Frame
            p.noFill();
            p.stroke(0);
            p.rect(1, 1, p.width-1, p.height-1);
        }
    }, "p5-bad-absolute");
}
