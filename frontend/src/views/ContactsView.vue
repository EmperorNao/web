<template>
  <section class="service-list contacts-list">
    <Contact
             v-for="review in reviews"
             :image="review.image"
             :fullname="review.fullname"
             :post_age="review.post_age"
             :description="review.description"
             :links="review.links"
    />
  </section>
</template>

<script>

import Contact from "@/components/Contact/Contact";

export default {
  name: 'ContactsView',
  components: {Contact},
  data () {
    return {
      reviews: [
        {
          image: require('@/assets/contacts/emperornao.jpg'),
          fullname: "Фахретдинов В.С",
          post_age: "Главный разработчик, 20 y.o",
          description: "Создатель лаборатории и по совместительству главный разработчик. Middle ML Software Engineer developer. 3 года опыта разработки: в прошлом аналитик данных в \"Белгородский информационный фонд\", на текущий момент разработчик машинного обучения в \"Яндекс\".",
          links: [
            {
              image: require('@/assets/icons/vk.svg'),
              link: "https://vk.com/emperornao"
            },
            {
              image: require('@/assets/icons/tg.png'),
              link: "https://t.me/emperornao"
            },
            {
              image: require('@/assets/icons/github.svg'),
              link: "https://github.com/EmperorNao"
            }
          ]
        },
        {
          image: require('@/assets/contacts/alex.jpg'),
          fullname: "Товстоганов А.К",
          post_age: "Бертухай младший, 21 y.o",
          description: "Вечный студент, младший разработчик.",
          links: [
            {
              image: require('@/assets/icons/vk.svg'),
              link: "https://vk.com/lexus_flexus"
            },
            {
              image: require('@/assets/icons/tg.png'),
              link: "https://t.me/lexusflexus"
            },
            {
              image: require('@/assets/icons/github.svg'),
              link: "https://github.com/Lexus1227"
            }
          ]
        }
      ]
    }

  }
}

</script>

<style>

  .contacts-list {
    margin-bottom: 20px;
  }

</style>