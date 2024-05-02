// document.addEventListener('DOMContentLoaded', function() {
//     const submitButton = document.getElementById('submitPost');
//     submitButton.addEventListener('click', submitPost);
// });

// function submitPost() {
//     const postContent = document.getElementById('postContent').value;
//     if (postContent.trim() === '') {
//         alert('Please enter a post!');
//         return;
//     }

//     // Create a new post element
//     const postElement = document.createElement('div');
//     postElement.classList.add('post');
//     postElement.innerHTML = `
//         <img src="../static/images/ice_cream_profile_pic.jpg" class="profile-picture">

//         <div class="speech-bubble">
//             <p>${postContent}</p>
//         </div>
//     `;

//     // Add the post to the posts container
//     const postsContainer = document.getElementById('posts');
//     postsContainer.appendChild(postElement);

//     // Clear the post input field
//     document.getElementById('postContent').value = '';
// }



// Function to render posts
function renderPosts(posts) {
    const postsContainer = document.getElementById('posts');
    postsContainer.innerHTML = ''; // Clear previous posts

    posts.forEach(post => {
        const postElement = document.createElement('div');
        postElement.classList.add('post');

        // Display profile picture
        const profilePicture = document.createElement('img');
        profilePicture.classList.add('profile-picture');
        profilePicture.src = "../static/images/ice_cream_profile_pic.jpg"; // Path to profile picture
        document.getElementById('posts').appendChild(profilePicture);

        // Post content container
        const postContentContainer = document.createElement('div');
        postContentContainer.classList.add('post-content');

        // Display post content
        const contentElement = document.createElement('p');
        contentElement.textContent = post.content;
        postElement.appendChild(contentElement);

        // Display recipe name
        const recipeNameElement = document.createElement('p');
        const selectedRecipe = document.getElementById('recipeSelect').value;
        recipeNameElement.textContent = "Recipe Name: " + selectedRecipe;
        postElement.appendChild(recipeNameElement);

        // Display recipe rating
        const ratingElement = document.createElement('p');
        ratingElement.textContent = "Recipe Rating: " + post.rating;
        postElement.appendChild(ratingElement);
        postsContainer.appendChild(postElement);
    });
}

// Function to reset input boxes
function resetInputBoxes() {
    document.getElementById('postContent').value = ''; // Clear textarea
    document.getElementById('recipeSelect').selectedIndex = 0; // Reset select to first option
    document.getElementById('recipeRating').value = ''; // Clear input for rating
}

// Function to handle post submission
function handlePostSubmission() {
    const postContent = document.getElementById('postContent').value;
    const recipeName = document.getElementById('recipeSelect').value;
    const recipeRating = document.getElementById('recipeRating').value;

    // Check if post content, recipe name, and recipe rating are not empty
    if (postContent.trim() !== '' && recipeName.trim() !== '' && recipeRating.trim() !== '') {
        // Create post object
        const post = {
            content: postContent,
            recipeName: recipeName,
            rating: recipeRating
        };

        // Code to send post data to SQL goes here

        // After successful submission, render the updated posts
        // add code to do that here
        
        renderPosts([post]);

        // Reset input boxes for new post
        resetInputBoxes();
    } else {
        alert('Please enter post content, select a recipe name, and enter a recipe rating.');
    }
}

// Add event listener to submit button
document.getElementById('submitPost').addEventListener('click', handlePostSubmission);