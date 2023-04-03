let postToDelete;

function saveDelete(post){
    postToDelete = post;
}

function getDelete(redirectURL){
    window.location.replace(`${redirectURL}/${postToDelete}` );
} 
