customElements.define('cc-toc', class extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        const toc = document.createElement('ul');
        toc.className = 'toc';
        const headings = document.querySelectorAll('h2[id]');
        for (const heading of headings) {
            const li = document.createElement('li');
            li.className = 'toc-entry';
            const a = document.createElement('a');
            a.href = `#${heading.id}`;
            a.textContent = heading.textContent;
            li.appendChild(a);
            toc.appendChild(li);
        }
        this.insertBefore(toc, this.firstChild);
    }
});
