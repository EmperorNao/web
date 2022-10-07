<template>
  <div>
  <div class="review">
    {{text}}
  </div>
  </div>
</template>

<script>

export default {
  name: 'Review',
  components: {},
  props: ['text'],
}

</script>

<style>

  .review {
    border: solid #fff0d9 1px;
    background-color: #fffbf4;
    border-radius: 6px;
    padding: 20px;
    font-size: 18px;
  }

</style>