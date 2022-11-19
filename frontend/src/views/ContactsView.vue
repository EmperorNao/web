<template>
  <section class="service-list contacts-list">
    <Contact
             v-for="contact in contacts"
             :image="contact.image"
             :fullname="contact.fullname"
             :post_age="contact.post_age"
             :description="contact.description"
             :links="contact.links"
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
      contacts: [
        // {
        //   image: require('@/assets/contacts/emperornao.jpg'),
        //   fullname: "Фахретдинов В.С",
        //   post_age: "Главный разработчик, 20 y.o",
        //   description: "Создатель лаборатории и по совместительству главный разработчик. Middle ML Software Engineer developer. 3 года опыта разработки: в прошлом аналитик данных в \"Белгородский информационный фонд\", на текущий момент разработчик машинного обучения в \"Яндекс\".",
        //   links: [
        //     {
        //       image: require('@/assets/icons/vk.svg'),
        //       link: "https://vk.com/emperornao"
        //     },
        //     {
        //       image: require('@/assets/icons/tg.png'),
        //       link: "https://t.me/emperornao"
        //     },
        //     {
        //       image: require('@/assets/icons/github.svg'),
        //       link: "https://github.com/EmperorNao"
        //     }
        //   ]
        // },
        // {
        //   image: require('@/assets/contacts/alex.jpg'),
        //   fullname: "Товстоганов А.К",
        //   post_age: "Бертухай младший, 21 y.o",
        //   description: "Вечный студент, младший разработчик.",
        //   links: [
        //     {
        //       image: require('@/assets/icons/vk.svg'),
        //       link: "https://vk.com/lexus_flexus"
        //     },
        //     {
        //       image: require('@/assets/icons/tg.png'),
        //       link: "https://t.me/lexusflexus"
        //     },
        //     {
        //       image: require('@/assets/icons/github.svg'),
        //       link: "https://github.com/Lexus1227"
        //     }
        //   ]
        // }
      ]
    }

  },

  created() {

    this.$http.get('api/contacts')
        .then((response) => this.contacts = response.data.items.map(el => {
              return {'image': this.$http.defaults.baseURL + el['image'],
                'description': el['description'],
                'fullname': el['fullname'],
                'post_age': el['post_age'],
                'links': el['links'].map(linkitem => {
                  return {
                    'image': this.$http.defaults.baseURL + linkitem['image'],
                    'link': linkitem['link']
                  }
                }),
              };
            }
        ))
  }

}





</script>

<style>

  .contacts-list {
    margin-bottom: 20px;
  }

</style>