<template>

  <footer>
    <div class="container">
      <div>&copy; VFLab, 2022</div>
      <div>+7(000)000-00-00</div>
    </div>
  </footer>

</template>

<script>
export default {
  name: "Footer"
}
</script>

<style>


  footer {
    background-color: rgb(0, 0, 0);
    padding: 15px;
    color: #fff;
    height: 100px;
  }


  footer .container {
    height: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }


</style>