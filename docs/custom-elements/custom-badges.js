function defineBadgeElement(tag, text, bg) {
    customElements.define(
        tag,
        class extends HTMLElement {
            connectedCallback() {
                this.innerHTML = `<span class="badge ${bg}">${text}</span>`;
            }
        });
}

defineBadgeElement('cc-badge-easy', 'Easy', 'bg-success');
defineBadgeElement('cc-badge-medium', 'Medium', 'bg-warning');
defineBadgeElement('cc-badge-hard', 'Hard', 'bg-danger');
