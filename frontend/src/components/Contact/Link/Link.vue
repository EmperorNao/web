<template>
  <div class="contact-link">
    <img class="contact-link-image" :src="image">
    <a class="contact-link-link" :href="link">{{link}}</a>
  </div>
</template>

<script>


export default {
  name: 'Link',
  components: {},
  props: ['image', 'link'],
}
</script>

<style>

  .contact-link {
    margin-bottom: 8px;
  }


  .contact-link-image {
    width: 25px;
  }


  .contact-link-link {
    margin-left: 6px;
  }

</style>