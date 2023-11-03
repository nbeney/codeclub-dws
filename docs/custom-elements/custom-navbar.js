function navbar(active, level) {
    let activeHome = (active === 'home') ? 'active' : '';
    let activeGuizero = (active === 'guizero') ? 'active' : '';
    let activePygameZero = (active === 'pygame-zero') ? 'active' : '';
    let activeAdventurelib = (active === 'adventurelib') ? 'active' : '';

    let pathPrefix = (level === '0') ? './' : '../'.repeat(level);

    return `
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="${pathPrefix}index.html">Code Club</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link ${activeHome}" href="${pathPrefix}index.html">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activeGuizero}" href="${pathPrefix}guizero-based/index.html">Guizero</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activePygameZero}" href="${pathPrefix}pygame-zero-based/index.html">Pygame Zero</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link ${activeAdventurelib}" href="${pathPrefix}adventurelib-based/index.html">Adventurelib</a>
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
                this.innerHTML = navbar(this.active, this.level);
            }
        });
}

defineNavbarElement('cc-navbar');