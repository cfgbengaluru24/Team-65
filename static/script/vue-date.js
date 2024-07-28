new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: () => ({
        date: document.querySelector('input[name="datetime"]').value,
        menu1: false,
    }),
    computed: {
        computedDateFormattedMomentjs() {
            return this.date ? moment(this.date).format('dddd, MMMM Do YYYY') : ''
        },
    },
})

