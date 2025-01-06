document.getElementById('delete').addEventListener('click', () => {
    document.querySelector(".logout-modal-container").classList.remove('delete-hidden');
});

document.getElementById('cancel-delete').addEventListener('click', () => {
    document.querySelector(".logout-modal-container").classList.add('delete-hidden');
});