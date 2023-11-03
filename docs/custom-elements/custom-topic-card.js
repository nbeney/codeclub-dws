function topicCard(path, title, content) {
    return `
        <div class="card" style="display: inline-block; margin: 10px; width: 20rem;">
            <a href="${path}/index.html"><img src="${path}/logo.jpg" class="card-img-top" alt="..."></a>
            <div class="card-body">
                <h5 class="card-title">${title}</h5>
                <p class="card-text">${content}</p>
                <a href="${path}/index.html" class="btn btn-primary">Try it!</a>
            </div>
        </div>
    `;
}

customElements.define(
    'cc-topic-card',
    class extends HTMLElement {
        static observedAttributes = ['path', 'title'];

        attributeChangedCallback(name, oldValue, newValue) {
            if (oldValue === newValue) return;
            setTimeout(() => {
                this.content = this.content || this.innerHTML
                this[name] = newValue;
                if (this.path && this.title)
                    this.innerHTML = topicCard(this.path, this.title, this.content);
            });
        }
    });