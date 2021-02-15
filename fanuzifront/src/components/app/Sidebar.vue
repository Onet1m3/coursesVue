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
            <Schools />
            <Courses />
            
        </ul>
    </div>
</template>

<script>
import M from 'materialize-css/dist/js/materialize.min'
import Schools from './sidebar/Schools'
import Courses from './sidebar/Courses'
export default {
  mounted () {
    M.Collapsible.init(this.$refs.collapsible, {})
  },
  components: {
      Schools, Courses
  }
}
</script>
