(function() {
    const chatClass = "chat-sidebar__chat";
    const selectedChatClass = "chat-sidebar__chat-selected";

    const chats = document.querySelectorAll("." + chatClass);
    chats.forEach(function(chat) {
        chat.addEventListener("click", function() {
            const selectedChat = document.querySelector("." + selectedChatClass);
            selectedChat?.classList.remove(selectedChatClass);
            chat.classList.add(selectedChatClass);
        });
    });
})();
