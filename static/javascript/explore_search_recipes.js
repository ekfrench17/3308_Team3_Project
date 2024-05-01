text_box_added = false;
        function addTextBox(search_type, id) {
            if (!text_box_added && id !== "Surprise_Me"){
                var label = document.createElement("label");
                label.textContent = "Search by " + search_type + ":";

                var text_box = document.createElement("input");
                text_box.setAttribute("type", "text");

                var search_type_button = document.getElementById(id);

                var submit_search_button = document.createElement("button");

                submit_search_button.textContent = "Search";
                
                search_type_button.insertAdjacentElement('afterend', submit_search_button); 
                search_type_button.insertAdjacentElement('afterend', text_box);
                search_type_button.insertAdjacentElement('afterend', label); 
                
                text_box_added = true;

                document.body.addEventListener("click",function(event) {
                    if (event.target !== search_type_button && event.target !== text_box && event.target !== submit_search_button){
                        label.remove();
                        text_box.remove();
                        submit_search_button.remove();
                        text_box_added = false;
                    } else if (event.target === submit_search_button){
                        var search_box_value = text_box.value;
                        //console.log.out(search_box_value)
                        window.location.href="/search_results/"+ id + "/" + search_box_value;
                    }

                });
        }
    }
    function surprise_me(){
        window.location.href="/surprise_me"
        }