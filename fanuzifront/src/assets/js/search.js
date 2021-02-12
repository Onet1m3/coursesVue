const btnSearch = document.getElementById('searchBtn')
const searchForm = document.getElementById('searchBox')

let displaySearch = false

btnSearch.onclick = function (e) {
  e.preventDefault()
  if (displaySearch) {
    setTimeout(() => searchForm.classList.add('hidden'), 1000)
    displaySearch = !displaySearch
  } else {
    searchForm.classList.remove('hidden')
    displaySearch = !displaySearch
  }
}
