// Sidebar toggle for mobile
function toggleSidebar() {
  const sidebar = document.querySelector('.sidebar');
  sidebar.classList.toggle('open');
}

// Close sidebar when clicking outside on mobile
document.addEventListener('click', function(e) {
  const sidebar = document.querySelector('.sidebar');
  const toggle = document.querySelector('.sidebar-toggle');
  if (!sidebar || !toggle) return;
  
  if (sidebar.classList.contains('open') &&
      !sidebar.contains(e.target) &&
      !toggle.contains(e.target)) {
    sidebar.classList.remove('open');
  }
});

// Highlight current chapter in sidebar
document.addEventListener('DOMContentLoaded', function() {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll('.nav-chapter');
  links.forEach(link => {
    if (currentPath.endsWith(link.getAttribute('href'))) {
      link.classList.add('active');
    }
  });
});
