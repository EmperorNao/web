<template>
  <div class="contact">
      <img class="contact-photo" :src="image">
      <div class="contact-info">
        <div class="contact-fullname">{{fullname}}</div>
        <div class="contact-post_age">{{post_age}}</div>
        <div class="contact-description">{{description}}</div>

        <div class="contact-links">
        <Link
                v-for="link in links"
                :image="link.image"
                :link="link.link"
        />
        </div>

      </div>
  </div>
</template>

<script>

import Link from "@/components/Contact/Link/Link";
export default {
  name: 'Service',
  components: {Link},
  props: ['image', 'fullname', 'post_age', 'description', 'links'],
}

</script>

<style>


  .contact {
    display: flex;
    align-items: start;
    border-radius: 30px;
    padding: 20px;
    margin: 40px;
    width: 90%;
  }


  .contact-photo {
    width: 350px;
    border-radius: 30px;
    alignment: left;
  }


  .contact-info {
    margin-left: 50px;
    display: flex;
    flex-direction: column;
    align-items: start;
  }


  .contact-info .contact-fullname {
    font-size: 22px;
  }


  .contact-info .contact-post_age {
    font-size: 17px;
  }


  .contact-info .contact-description {
    margin-top: 15px;
    font-size: 18px;
    line-height: 2;
  }


  .contact-links {
    margin-top: 15px;
    list-style: None;
  }


</style>