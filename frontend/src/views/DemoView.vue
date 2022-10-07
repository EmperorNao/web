<template>

  <div class="demo">
    <div class="title">Суммаризация текста</div>
    <div class="description">Суммаризация — автоматическое создание краткого содержания, например заголовка, резюме, аннотации, на основе исходного текста.</div>
    <div class="demo-texts">
      <textarea class="demo-input" placeholder="Введите исходный текст"></textarea>
      <textarea class="demo-input" readonly=""></textarea>
    </div>
    <div class="button-container">
      <button type="button demo-button" class="btn btn-lg btn-outline-dark">Попробовать</button>
    </div>
  </div>

</template>

<script>
export default {
  name: "DemoView"
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