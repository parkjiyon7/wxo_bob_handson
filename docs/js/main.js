// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add active state to navigation links
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

window.addEventListener('scroll', () => {
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (pageYOffset >= sectionTop - 200) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Add animation on scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all cards
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card, .resource-card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
        observer.observe(card);
    });
});

// Function to add copy buttons to code blocks
function addCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(block => {
        const pre = block.parentElement;
        
        // Check if wrapper already exists
        if (pre.parentElement.classList.contains('code-block-wrapper')) {
            return;
        }
        
        // Create wrapper
        const wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';
        
        // Create button
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = '복사';
        button.addEventListener('click', () => {
            navigator.clipboard.writeText(block.textContent).then(() => {
                button.textContent = '복사됨!';
                setTimeout(() => {
                    button.textContent = '복사';
                }, 2000);
            });
        });
        
        // Wrap the pre element
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        wrapper.appendChild(button);
    });
}

// Copy code blocks to clipboard on page load
document.addEventListener('DOMContentLoaded', () => {
    addCopyButtons();
});

// Back to top button
const backToTopButton = document.createElement('button');
backToTopButton.innerHTML = '↑';
backToTopButton.className = 'back-to-top';
backToTopButton.style.display = 'none';
document.body.appendChild(backToTopButton);

window.addEventListener('scroll', () => {
    if (window.pageYOffset > 300) {
        backToTopButton.style.display = 'block';
    } else {
        backToTopButton.style.display = 'none';
    }
});

backToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Add styles for back to top button and active nav
const style = document.createElement('style');
style.textContent = `
    .back-to-top {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background-color: var(--primary-color);
        color: white;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        box-shadow: var(--shadow-lg);
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .back-to-top:hover {
        background-color: var(--primary-dark);
        transform: translateY(-5px);
    }
    
    .nav-link.active {
        background-color: var(--primary-color);
        color: white;
    }
`;
document.head.appendChild(style);

// Made with Bob

// Load Today's Info
document.addEventListener('DOMContentLoaded', () => {
    const todayInfoCard = document.getElementById('today-info-card');
    if (todayInfoCard) {
        fetch('Today_info.md')
            .then(response => {
                if (!response.ok) {
                    throw new Error('File not found');
                }
                return response.text();
            })
            .then(text => {
                // Use marked.js if available
                if (typeof marked !== 'undefined') {
                    todayInfoCard.innerHTML = marked.parse(text);
                } else {
                    // Fallback: display as plain text
                    todayInfoCard.innerHTML = '<pre>' + text + '</pre>';
                }
            })
            .catch(error => {
                console.log('Today info not found:', error);
                todayInfoCard.style.display = 'none';
            });
    }
});
