function showIframe(id) {

    const options = [
        {
            "id": "rsoto",
            "btn": "showIframeRsoto",
            "iframe": "iframe_rsoto",
        },
        {
            "id": "induserve",
            "btn": "showIframeInduserve",
            "iframe": "iframe_induserve",
        }
    ];

    function search(id, options){

        for (let i=0; i < options.length; i++) {
            if (options[i].btn === id) {               
                return options[i];
            }
        }
    }

    function change_style(selection, options){
        for (let i=0; i < options.length; i++) {

            let iframe = document.getElementById(options[i].iframe);           
            let btn = document.getElementById(options[i].btn);

            if (options[i] === selection) {    

                if (iframe.style.display === "none"){
                    iframe.style.display = "inline";
                    btn.innerHTML = "Ocultar";
                }
                else if(iframe.style.display === "inline"){
                    iframe.style.display = "none";
                    btn.innerHTML = "Mostrar";
                }
            }
            else {
                btn.innerHTML = "Mostrar";
                iframe.style.display = "none";
            }
        }
    }

    // start

    let selection = search(id, options);
    change_style(selection, options);

    let iframe = document.getElementById(selection.iframe);
    iframe.scrollIntoView();

    // end
    
}