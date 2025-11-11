document.querySelectorAll('a[aria-label^="Supprimer"]').forEach(btn => {
  btn.addEventListener('click', e => {
    if (!confirm('Voulez-vous vraiment supprimer cette tâche ?')) {
      e.preventDefault();
    }
  });
});
