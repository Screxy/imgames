import { defineStore } from 'pinia';
import { ref } from 'vue';

function getSubdomain(url: any) {
  url = url.replace('https://www.', '');
  url = url.replace('http://www.', '');
  url = url.replace('https://', '');
  url = url.replace('http://', '');
  var temp = url.split('/');
  if (temp.length > 0) {
    var temp2 = temp[0].split('.');
    if (temp2.length > 1) {
      if (
        temp2.length > 2 ||
        temp2[1].includes(process.env.VUE_APP_MAIN_DOMAIN)
      ) {
        return temp2[0];
      }
    }
  }
  return '';
}
export const useStore = defineStore('store', () => {
  const userId = ref(false);
  const isAuthenticated = ref(false);
  const isAdmin = ref(false);
  const isStaff = ref(false);
  const isLoading = ref(false);
  const gotVerifiedAuth = ref(false);
  const subdomain = getSubdomain(window.location.host);
  // const packageVersion = process.env.PACKAGE_VERSION || '0';
  const packageVersion = '0';
  const chosenCards = Array<any> as any;
  const messages = Array<any> as any;
  const userName = '';
  return {
    userId,
    isAuthenticated,
    isAdmin,
    isStaff,
    isLoading,
    gotVerifiedAuth,
    subdomain,
    packageVersion,
    chosenCards,
    messages,
    userName,
  };
});
