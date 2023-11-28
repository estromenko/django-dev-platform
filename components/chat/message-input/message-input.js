(function() {
    htmx.onLoad(function(content) {
        const messageInput = content.querySelector("#message-input");

        messageInput.addEventListener("keydown", function(event) {
            if (event.code === "Enter" && !event.shiftKey) {
                event.preventDefault();
                htmx.trigger("#message-input-form", "submit");
            }
        });
    });
})();
