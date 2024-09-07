document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/user-profiles')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('user-profiles');
            data.forEach(profile => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${profile.id}</td>
                    <td>${profile.messages}</td>
                    <td>${profile.keywords.join(', ')}</td>
                    <td>${profile.status}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching user profiles:', error));
});
