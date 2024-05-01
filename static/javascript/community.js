document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.getElementById('submitPost');
    submitButton.addEventListener('click', submitPost);
});

function submitPost() {
    const postContent = document.getElementById('postContent').value;
    if (postContent.trim() === '') {
        alert('Please enter a post!');
        return;
    }

    // Create a new post element
    const postElement = document.createElement('div');
    postElement.classList.add('post');
    postElement.innerHTML = `
        <img src="../static/images/ice_cream_profile_pic.jpg" class="profile-picture">

        <div class="speech-bubble">
            <p>${postContent}</p>
        </div>
    `;

    // Add the post to the posts container
    const postsContainer = document.getElementById('posts');
    postsContainer.appendChild(postElement);

    // Clear the post input field
    document.getElementById('postContent').value = '';
}

