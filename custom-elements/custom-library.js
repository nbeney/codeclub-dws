let libraryCounter = 0;

function libraryAccordionItem(name, description, content) {
    libraryCounter++;

    return `
        <div class="accordion-item">
            <h3 class="accordion-header" id="panelsStayOpen-heading${libraryCounter}">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapse${libraryCounter}" aria-expanded="false" aria-controls="panelsStayOpen-collapse${libraryCounter}">
                <strong class="text-primary">${name}</strong>&nbsp;- ${description}
            </button>
            </h3>
            <div id="panelsStayOpen-collapse${libraryCounter}" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-heading${libraryCounter}">
                <div class="accordion-body">
                    ${content}
                </div>
            </div>
        </div>
    `;
}

customElements.define(
    'cc-library',
    class extends HTMLElement {
        static observedAttributes = ['name', 'description'];

        attributeChangedCallback(name, oldValue, newValue) {
            if (oldValue === newValue) return;
            // Timeout required because innerHTML is not set yet.
            setTimeout(() => {
                this.content = this.content || this.innerHTML
                this[name] = newValue;
                if (this.name && this.description)
                    this.innerHTML = libraryAccordionItem(this.name, this.description, this.content);
            });
        }
    });