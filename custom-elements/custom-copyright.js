customElements.define('cc-copyright', class extends HTMLElement {
    connectedCallback() {
        const currentYear = new Date().getFullYear();
        this.innerHTML = `
            <footer>
                <div id="copyright">&copy; 2023-${currentYear} Nicolas Beney. All rights reserved.</div>
            </footer>
        `;
    }
});
