<template>
    <div>
        <ul class="collapsible collapsible-accordion" ref="collapsible">
            <li>
                <nav>
                    <div class="nav-wrapper">
                        <form>
                            <div class="input-field input-field-search">
                            <input id="search" type="search" required>
                            <label class="label-icon" for="search"><i class="material-icons">search</i></label>
                            <i class="material-icons">close</i>
                            </div>
                        </form>
                    </div>
                </nav>
            </li>
            <li class="bold"><a class="collapsible-header waves-effect waves-purple lighten-3" tabindex="0">Онлайн школы</a>
                <div class="collapsible-body">
                    <ul>
                        <li><a href="">Школа 2</a></li>
                        <li><a href="">Школа 3</a></li>
                        <li><a href="">Школа 4</a></li>
                    </ul>
                </div>
            </li>
            <li class="bold"><a class="collapsible-header waves-effect waves-purple lighten-3" tabindex="0">Курсы</a>
                <div class="collapsible-body">
                    <ul>
                        <li><a href="">Что-то</a></li>
                    </ul>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
import M from 'materialize-css/dist/js/materialize.min'
export default {
  mounted () {
    M.Collapsible.init(this.$refs.collapsible, {})
  }
}
</script>
