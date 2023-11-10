function projectCard(title, difficulty, href, imgSrc) {
    return `
        <div class="card grid-item ${difficulty}" style="width: 20em; margin: 0 1em 1em 0;">
            <a href="${href}"><img src="${imgSrc}" class="card-img-top" alt="${title}"></a>
            <h5 class="card-body">${title}
                <cc-badge-${difficulty}/>
            </h5>
        </div>
    `;
}

customElements.define(
    'cc-project-card',
    class extends HTMLElement {
        static observedAttributes = ['title', 'difficulty', 'path', 'href', 'img-src'];

        attributeChangedCallback(name, oldValue, newValue) {
            if (oldValue === newValue) return;
            this[name] = newValue;
            if (name === 'path') {
                this.href = `${this.path}/index.html`;
                this['img-src'] = `${this.path}/screenshot.png`;
            }
            if (this.title && this.difficulty && this.href && this['img-src'])
                this.innerHTML = projectCard(this.title, this.difficulty, this.href, this['img-src']);
        }
    });

customElements.define(
    'cc-project-filters',
    class extends HTMLElement {
        connectedCallback() {
            this.innerHTML = `
                <style>
                    .btn-check#btnradio2:checked+.btn-outline-dark {
                        background-color: #198754;
                        color: #ffffff;
                    }
                    
                    .btn-check#btnradio3:checked+.btn-outline-dark {
                        background-color: #ffc107;
                        color: #000000;
                    }
                    
                    .btn-check#btnradio4:checked+.btn-outline-dark {
                        background-color: #dc3545;
                        color: #ffffff;
                    }
                </style>
                <div class="filters" style="margin-bottom: 1em;">
                    <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
                        <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" data-filter="*" checked>
                        <label class="btn btn-outline-dark" for="btnradio1">All</label>

                        <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off" data-filter=".easy">
                        <label class="btn btn-outline-dark" for="btnradio2">Easy</label>

                        <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off" data-filter=".medium">
                        <label class="btn btn-outline-dark" for="btnradio3">Medium</label>

                        <input type="radio" class="btn-check" name="btnradio" id="btnradio4" autocomplete="off" data-filter=".hard">
                        <label class="btn btn-outline-dark" for="btnradio4">Hard</label>
                    </div>
                </div>
            `;
        }
    });

window.addEventListener('load', function() {
    // Initialise Isotope
    let grid = $('.grid').isotope({
        // options
        itemSelector: '.grid-item',
        layoutMode: 'masonry',
    });

    // Layout Isotope after each image loads
    grid.imagesLoaded().progress(function() {
        grid.isotope('layout');
    });

    let buttonGroup = $('.filters');
    buttonGroup.on('click', 'input', function(event) {
        let button = $(event.currentTarget);
        let filterValue = button.attr('data-filter');
        grid.isotope({
            filter: filterValue
        });
    });
});
