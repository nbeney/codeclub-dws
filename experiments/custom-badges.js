function defineBadgeElement(name, text, bg) {
    class BadgeElement extends HTMLElement {
        connectedCallback() {
            this.innerHTML = `<span class="badge ${bg}">${text}</span>`;
        }
    }

    customElements.define(name, BadgeElement);
}

defineBadgeElement('badge-easy', 'Easy', 'bg-success');
defineBadgeElement('badge-medium', 'Medium', 'bg-warning');
defineBadgeElement('badge-hard', 'Hard', 'bg-danger');
