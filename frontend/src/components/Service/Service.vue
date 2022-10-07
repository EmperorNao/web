<template>
  <div>
  <div class="service">
    <div>
      <img :src="image">
    </div>
    <div class="service-title"><b>{{title}}</b></div>
    <div class="service-description">{{description}}</div>
  </div>
  </div>
</template>

<script>


export default {
  name: 'Service',
  components: {},
  props: ['image', 'title', 'description'],
}
</script>

<style>

.service {
  border-radius: 30px;
  border: 1px solid #ddd;
  padding: 15px;
}


.service .service-title {
  margin: 5px 0px;
  font-size: 24px;
}


.service .service-description {
  padding: 3px;
  font-size: 20px;
}


.service img {
  width: 100%;
  border-radius: 30px;
}

</style>