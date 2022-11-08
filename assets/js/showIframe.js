function showIframe(id) {
    let iframe;
    let btn;

    btn = document.getElementById(id);

    if( id == "showIframeRsoto" ){
        iframe = document.getElementById("iframe_rsoto");
    }

    else if( id == "showIframeInduserve" ){
        iframe = document.getElementById("iframe_induserve");
    }

    if (iframe.style.display === "none"){
        iframe.style.display = "inline";
        btn.innerHTML = "Ocultar";

    } else if(iframe.style.display === "inline"){
        iframe.style.display = "none";
        btn.innerHTML = "Mostrar";
    }
    
}