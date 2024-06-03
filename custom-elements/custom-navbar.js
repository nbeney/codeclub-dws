function navbar(active, level, style) {
    let activeHome = (active === 'home') ? 'active' : '';
    let activeGuizero = (active === 'guizero') ? 'active' : '';
    let activePygameZero = (active === 'pygame-zero') ? 'active' : '';
    let activeAdventurelib = (active === 'adventurelib') ? 'active' : '';
    let activeP5 = (active === 'p5') ? 'active' : '';
    let activePythonLibraries = (active === 'python-libraries') ? 'active' : '';

    let origin = window.location.origin.replace(/\/$/, '');

    return `
        <nav class="navbar navbar-expand-lg ${style}">
            <div class="container-fluid">
                <a class="navbar-brand" href="${origin}/index.html">Code Club</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link ${activeHome}" href="${origin}/index.html">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activeGuizero}" href="${origin}/activities/guizero-based/index.html">Guizero</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activePygameZero}" href="${origin}/activities/pygame-zero-based/index.html">Pygame Zero</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activeAdventurelib}" href="${origin}/activities/adventurelib-based/index.html">Adventurelib</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activeP5}" href="${origin}/activities/p5-based/index.html">P5</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activePythonLibraries}" href="${origin}/activities/python-libraries/index.html">Python libraries</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    `;
}

function defineNavbarElement(tag, active) {
    customElements.define(
        tag,
        class extends HTMLElement {
            static observedAttributes = ['active', 'level'];

            attributeChangedCallback(name, oldValue, newValue) {
                this[name] = newValue;
                // this.innerHTML = navbar(this.active, this.level, 'navbar-dark bg-secondary');
                // this.innerHTML = navbar(this.active, this.level, 'navbar-dark bg-dark');
                this.innerHTML = navbar(this.active, this.level, 'navbar-dark bg-primary');
            }
        });
}

defineNavbarElement('cc-navbar');