<template>
  <div>
    <TextInput
      :placeholder="$t('room.moneyPerMonth')"
      :disabled="formLoading"
      :type="'number'"
      :predefined="defaultRoomSettings.moneyPerMonthDefault"
      @input="newRoom != undefined ? (newRoom.moneyPerMonth = $event) : ''"
    ></TextInput>
    <TextInput
      :placeholder="$t('room.numberOfTurns')"
      :disabled="formLoading"
      :predefined="defaultRoomSettings.numberOfTurnsDefault"
      :type="'number'"
      @input="
        defaultRoomSettings != undefined ? (newRoom.numberOfTurns = $event) : ''
      "
    ></TextInput>
    <DropdownSelector
      :options="[
        { value: 'Test', label: 'Test' },
        { value: 'Test2', label: 'Test2' },
      ]"
      :predefined="'Test'"
    ></DropdownSelector>
    <SubmitButton :disabled="formLoading" @click="createNewRoom">
      {{ $t('buttons.create') }}
    </SubmitButton>
  </div>
</template>

<script>
import TextInput from '@/components/ui/TextInput.vue';
import SubmitButton from '@/components/ui/SubmitButton.vue';
import defaultRoomSettings from '@/graphql/queries/rooms/defaultRoomSettings.gql';
import createRoom from '@/graphql/mutations/rooms/createRoom.gql';
import roomsInOrganization from '@/graphql/queries/rooms/roomsInOrganization.gql';
import { ROOMS_ROOT_PATH } from '@/pathVariables';
import DropdownSelector from '@/components/ui/DropdownSelector.vue';

export default {
  name: 'CreateRoomForm',
  components: {
    TextInput,
    SubmitButton,
    DropdownSelector,
  },
  apollo: {
    defaultRoomSettings: {
      query: defaultRoomSettings,
      variables() {
        return {
          // TODO: add subdomain variables
          subdomain: this.subdomain,
        };
      },
      update: function (data) {
        let settings = data.defaultRoomSettings;
        return settings;
      },
    },
  },
  data() {
    return {
      formLoading: false,
      newRoom: {
        moneyPerMonth: '',
        numberOfTurns: '',
      },
      defaultRoomSettings: {},
    };
  },
  computed: {
    subdomain() {
      return this.$store.state.subdomain;
    },
  },
  methods: {
    createNewRoom() {
      this.newRoom.subdomain = this.subdomain;
      this.$apollo
        .mutate({
          mutation: createRoom,
          variables: this.newRoom,
          update: (store, { data: { createRoom } }) => {
            const data = store.readQuery({
              query: roomsInOrganization,
              variables: { subdomain: this.subdomain },
            });

            let roomsInOrganizationCopy = data.roomsInOrganization.slice();

            roomsInOrganizationCopy.push(createRoom.room);

            store.writeQuery({
              query: roomsInOrganization,
              variables: { subdomain: this.subdomain },
              data: { roomsInOrganization: roomsInOrganizationCopy },
            });
          },
        })
        .then((data) => {
          this.$router.push(
            ROOMS_ROOT_PATH + '/' + data.data.createRoom.room.code.toUpperCase()
          );
        })
        .catch();
    },
  },
};
</script>

<style lang="scss" scoped></style>
