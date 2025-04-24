// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
  // Add copy buttons to code blocks that don't already have them
  document.querySelectorAll('pre code').forEach(function(codeBlock) {
    const pre = codeBlock.parentNode;
    if (!pre.querySelector('.md-clipboard')) {
      const button = document.createElement('button');
      button.className = 'md-clipboard';
      button.title = 'Copy to clipboard';
      button.setAttribute('aria-label', 'Copy to clipboard');
      
      button.addEventListener('click', function() {
        navigator.clipboard.writeText(codeBlock.textContent).then(function() {
          button.setAttribute('data-copied', 'true');
          setTimeout(function() {
            button.removeAttribute('data-copied');
          }, 1000);
        });
      });
      
      pre.appendChild(button);
    }
  });

  // Handle tabs if using custom tab implementation
  document.querySelectorAll('.tabbed-set').forEach(function(tabSet) {
    const tabs = tabSet.querySelectorAll('.tabbed-set > input');
    tabs.forEach(function(tab) {
      tab.addEventListener('change', function() {
        if (tab.checked) {
          // Store the selected tab index in local storage
          localStorage.setItem(
            'tabbed-set-' + Array.from(tabs).indexOf(tab),
            tab.id
          );
        }
      });
      
      // Restore tab state from local storage
      const stored = localStorage.getItem(
        'tabbed-set-' + Array.from(tabs).indexOf(tab)
      );
      if (stored && document.getElementById(stored)) {
        document.getElementById(stored).checked = true;
      }
    });
  });
}); 