function defineBadgeElement(name, text, bg) {
    customElements.define(
        name,
        class extends HTMLElement {
            connectedCallback() {
                this.innerHTML = `<span class="badge ${bg}">${text}</span>`;
            }
        });
}

defineBadgeElement('badge-easy', 'Easy', 'bg-success');
defineBadgeElement('badge-medium', 'Medium', 'bg-warning');
defineBadgeElement('badge-hard', 'Hard', 'bg-danger');
