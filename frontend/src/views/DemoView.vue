<template>

  <section>
    <Demo
    />
  </section>

</template>

<script>

import Demo from "@/components/Demo/Demo";

export default {
  name: "DemoView",
  components: {Demo},
  // data () {
  //   return {
  //     original_text: "",
  //     summarized_text: "",
  //     onclick: this.methods.summarize
  //   }
  // }

}
</script>

<style>

  .demo {
    font-family: 'Ubuntu', sans-serif;
    color: black;
    border-radius: 30px;
  }


  .demo .title {
    font-size: 40px;
    text-align: center;
    margin: 20px 0px;
  }


  .demo .description {
    margin: 20px 20px;
    font-size: 25px;
  }


  .demo .demo-texts {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }


  .demo .demo-input {
    width: 50%;
    min-height: 200px;
    font-size: 25px;
    margin: 20px;
  }


  .demo .button-container {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
    padding-bottom: 20px;
  }

</style>