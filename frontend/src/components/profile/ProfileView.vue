<template>
    <div class='profile'>
        <h2 class='profile__title'>{{ $t('profile.title') }}</h2>
        <img
            class="profile__avatar"
            src="@/assets/no_avatar.svg"
            alt="Аватар"
        />
        <ul class='profile__fields'>
            <li v-for="field, key in profile" v-if="key != '__typename' && key != 'id' && key != 'isStaff' && key != 'isAdmin'">
                {{ $t("profile." + key) }}: {{ field }}
            </li>
        </ul>
        <SubmitButton
          class="profile__edit-btn"
          :type="'bg-outline'"
          @click="$router.push('/edit')"
          >{{ $t('profile.edit') }}</SubmitButton
        >
    </div>
</template>

<script>
import profile from "@/graphql/queries/profile.gql";
import SubmitButton from '@/components/ui/SubmitButton.vue';

export default {
    name: 'ProfileView',
    components: {
        SubmitButton,
    },
    data() {
        return {
        };
    },
    apollo: {
        profile: {
            query: profile,
        }
    }
};
</script>

<style lang='scss'>
.profile {
    position: relative;
    width: 100%;
    grid-column-start: 3;
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    row-gap: 0;
    justify-content: space-around;

    &__title {
        text-align: center;
        width: 100%;
    }

    &__avatar {
        width: 30%;
    }

    &__fields {
        font-size: 22px;    
        list-style-type: none;
        padding-left: 0;
        flex-grow: 2;
    }

    &__edit-btn {
        position: absolute;
        top: 10px;
        right: 10px;
    }
}

</style>