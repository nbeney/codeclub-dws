function defineBadgeElement(tag, text, bg) {
    customElements.define(
        tag,
        class extends HTMLElement {
            connectedCallback() {
                this.innerHTML = `<span class="badge ${bg}">${text}</span>`;
            }
        });
}

defineBadgeElement('badge-easy', 'Easy', 'bg-success');
defineBadgeElement('badge-medium', 'Medium', 'bg-warning');
defineBadgeElement('badge-hard', 'Hard', 'bg-danger');
