<template>
  <div class="container">
    <TopBar></TopBar>
    <div class="main-grid">
      <div class="main-grid-column scrollable">
        <RoomList></RoomList>
      </div>
      <div>
        <CreateRoomView></CreateRoomView>
      </div>
      <div>
        <OrganizationList
          class="main-grid-column scrollable"
        ></OrganizationList>
      </div>
    </div>
  </div>
</template>

<script>
import { AUTH_PATH } from '@/pathVariables.js';

import OrganizationList from '@/components/organization/OrganizationList.vue';
import CreateRoomView from '@/components/room/CreateRoomView.vue';
import RoomList from '@/components/room/RoomsList.vue';
import TopBar from '@/components/ui/TopBar.vue';

export default {
  name: 'Main',
  components: {
    OrganizationList,
    CreateRoomView,
    RoomList,
    TopBar,
  },
  data() {
    return {
      authPath: AUTH_PATH,
    };
  },
};
</script>

<style lang="scss" scoped>
.main-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  column-gap: 1rem;
  height: calc(100vh - 48px);
  padding: 0 1rem;
  background: radial-gradient(
    52.5% 97.01% at 21.67% 20.17%,
    rgba(82, 110, 255, 0.25) 0%,
    rgba(249, 216, 167, 0.25) 89.06%
  );

  &-column {
    overflow-y: auto;
    overflow-x: hidden;
    height: calc(100vh - 48px);
  }
}
</style>
