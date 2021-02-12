
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, {});
});

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
});

const btnSearch = document.getElementById('searchBtn');
const searchForm = document.getElementById('searchBox')

let displaySearch = false;

btnSearch.onclick = function(e){
    e.preventDefault ();
    
    if (displaySearch) {
        // searchForm.classList.add('hidden');
        // TweenMax.to(searchForm,1,{x:'2%',display:'none',width:'60%',height:'65vh',ease:Back.easeOut});
        TweenLite.to(searchForm, 0.01, {css:{scale:.05, opacity:0}, ease:Quad.easeOut}), 20,-20;
        setTimeout(() => searchForm.classList.add('hidden'), 1000);
        displaySearch = !displaySearch;
    }else {
        TweenLite.to(searchForm, 0.01, {css:{scale:1, opacity:1}, ease:Quad.easeInOut}), 20,-20;
        searchForm.classList.remove('hidden');
        displaySearch = !displaySearch;
    }
}