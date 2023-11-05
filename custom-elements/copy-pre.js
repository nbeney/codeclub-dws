document.addEventListener('DOMContentLoaded', function() {
    addStyle();

    const preElements = document.querySelectorAll('.copy-pre');
    for (const preElement of preElements) {
        const copyIcon = document.createElement('i');
        copyIcon.className = 'bi bi-clipboard copy-icon';
        preElement.appendChild(copyIcon);

        copyIcon.addEventListener('click', function() {
            const content = preElement.innerText;
            navigator.clipboard.writeText(content)
                .then(() => {
                    console.log('Copied to clipboard: ' + content);
                    flashIcon(copyIcon, 'bi-clipboard', 'bi-check-lg');
                })
                .catch(err => {
                    console.error('Unable to copy to clipboard', err);
                    flashIcon(copyIcon, 'bi-clipboard', 'bi-exclamation-lg');
                });
        });
    }
});

function flashIcon(iconElement, oldName, newName) {
    iconElement.classList.replace(oldName, newName);
    setTimeout(() => {
        iconElement.classList.replace(newName, oldName);
    }, 500);
}

function addStyle() {
    const cssRules = `
  @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css");

  .copy-pre {
    position: relative;
  }

  .copy-icon {
    position: absolute;
    top: 0;
    right: 0;
    margin: 5px 5px 0 0;
  }

  .copy-icon:hover {
    background: #dddddd;
  }
`;

    // Create a style element and set its content to the CSS rules
    const styleElement = document.createElement('style');
    styleElement.type = 'text/css';

    if (styleElement.styleSheet) {
        // For IE
        styleElement.styleSheet.cssText = cssRules;
    } else {
        // For other browsers
        styleElement.appendChild(document.createTextNode(cssRules));
    }

    // Append the style element to the document's head
    document.head.appendChild(styleElement);
}
