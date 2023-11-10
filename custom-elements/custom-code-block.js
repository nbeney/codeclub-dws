const script = document.createElement('script');
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.2/highlight.min.js';
document.body.appendChild(script);

window.addEventListener('load', function() {
    const codeElements = document.querySelectorAll('pre > code');
    for (const codeElement of codeElements) {
        const iconElement = document.createElement('i');
        iconElement.className = 'bi bi-clipboard copy-icon';
        codeElement.appendChild(iconElement);

        codeElement.addEventListener('click', function() {
            const content = codeElement.innerText;
            navigator.clipboard.writeText(content)
                .then(() => {
                    console.log('Copied to clipboard: ' + content);
                })
                .catch(err => {
                    console.error('Unable to copy to clipboard', err);
                });
        });
    }
});

customElements.define(
    'cc-code-block',
    class extends HTMLElement {
        connectedCallback() {
            setTimeout(() => {
                this.innerHTML = `<pre><code class="language-python">${this.innerHTML.trim()}</code></pre>`;
            });
        }
    }
);

window.addEventListener('load', function() {
    hljs.highlightAll();
});