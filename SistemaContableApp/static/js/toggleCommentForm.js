document.addEventListener("DOMContentLoaded", function() {
    var comentarButtons = document.querySelectorAll(".comentar-btn");

    comentarButtons.forEach(function(button) {
        button.addEventListener("click", function(event) {
            var followingId = button.getAttribute("data-following-id");
            var fieldType = button.getAttribute("data-field-type");
            var commentModal = document.getElementById("commentModal_" + fieldType + "_" + followingId);
            commentModal.style.display = "block";
            event.stopPropagation();
        });
    });

    var closeButtons = document.querySelectorAll(".popup .close");
    closeButtons.forEach(function(closeBtn) {
        closeBtn.addEventListener("click", function() {
            var popup = closeBtn.closest(".popup");
            popup.style.display = "none";
        });
    });
});

function openCommentModal(followingId, fieldType) {
    var commentModal = document.getElementById("commentModal_" + fieldType + "_" + followingId);
    commentModal.style.display = "block";
}

function closeCommentModal(followingId, fieldType) {
    var commentModal = document.getElementById("commentModal_" + fieldType + "_" + followingId);
    commentModal.style.display = "none";
}
