import getBrowserLocale from '@/util/i18n/get-browser-locale';
import { supportedLocalesInclude } from '@/util/i18n/supported-locales';
import { createI18n } from 'vue-i18n';

function getStartingLocale() {
  const browserLocale = getBrowserLocale({ countryCodeOnly: true });
  if (supportedLocalesInclude(browserLocale)) {
    return browserLocale;
  } else {
    return process.env.VUE_APP_I18N_LOCALE || 'ru';
  }
}

function loadLocaleMessages() {
  const locales = require.context(
    '../locales',
    true,
    /[A-Za-z0-9-_,\s]+\.json$/i
  );
  const messages: any = {};
  locales.keys().forEach((key: any) => {
    const matched = key.match(/([A-Za-z0-9-_]+)\./i);
    if (matched && matched.length > 1) {
      const locale = matched[1];
      messages[locale] = locales(key);
    }
  });
  return messages;
}
const messeges = {
  message: 'Привет, i18n!',
  buttons: {
    create: 'Создать',
    logOut: 'Выйти',
    toMainPage: 'На главную',
    connect: 'Присоединиться',
    techSupport: 'Техническая поддержка',
  },
  organization: {
    organization: 'Организация',
    prefix: 'Префикс',
    subdomain: 'Поддомен',
    name: 'Имя',
  },
  room: {
    createNewRoom: 'Создать комнату',
    moneyPerMonth: 'Деньги за месяц',
    numberOfTurns: 'Количество месяцев',
    month: 'Месяц',
    periodIs: 'период составляет',
    numberOfMonths: 'месяца',
    monthNumber: {
      '1': 'ПЕРВЫЙ месяц периода',
      '2': 'ВТОРОЙ месяц периода',
      '3': 'ТРЕТИЙ месяц периода',
      '4': 'ЧЕТВЕРТЫЙ месяц периода',
      '5': 'ПЯТЫЙ месяц периода',
      '6': 'Шестой месяц периода',
      '7': 'Седьмой месяц периода',
      '8': 'Восьмой месяц периода',
      '9': 'Девятый месяц периода',
      '10': 'Десятый месяц периода',
    },
    of: 'из',
    ofMonths: 'Месяцев',
    waitingForRound: 'Ожидание начала раунда',
    roundEnded: 'Конец раунда',
    roomsList: 'Список комнат',
    room: 'Комната',
    scores: 'Всего очков: ',
    goToRoom: 'Перейти в комнату',
    round: 'Раунд',
    player: {
      playersList: 'Игроки',
      player: 'Игрок',
      roomOwner: 'Владелец комнаты',
      effectsList: 'Изменения',
      chat: 'Чат',
      you: 'Вы',
      application: 'Кол-во',
    },
    gameBoard: {
      gameBoard: 'Игровая доска',
      channelsTitle: 'Каналы',
      trafficTitle: 'Трафик',
      total: 'Итого',
      stageConversion: 'Конверсия этапа',
    },
    mechanics: 'Механика',
    card: {
      moneyLeft: 'Оставшийся бюджет',
      waitingForOthers: 'Ожидание других игроков...',
      cardsList: 'Список карточек',
      chooseCard: 'Выбрать',
      selectedCard: 'Выбранная карточка',
      deselectCard: 'Отменить выбор',
      send: 'Завершить ход',
      notEnoughMoney: 'Недостаточно денег!',
    },
    waitingHeader: 'Ожидаем подключения игроков...',
    waitingTextForOwner:
      'Когда все приглашённые игроки зайдут в комнату, вы можете начать игру',
    startRoundButton: 'Начать раунд',
    roundFinishedHeader: 'Раунд {round} завершён',
    reStartRoundButton: 'Начать новый раунд {nextRound}',
    navigation: {
      players: 'Участники',
      effects: 'Эффекты',
      chat: 'Чат',
      cards: 'Карточки',
    },
    flow: 'Игровая механика',
    connectRoom: 'Присоединиться к комнате',
    roomCode: 'Номер комнаты',
    result: 'Результат',
    startMonth: 'Начальный месяц',
    step: 'Ход',
    passStep: 'Пропуск хода',
    firstPlace: 'I место',
    secondPlace: 'II место',
    thirdPlace: 'III место',
    yourResult: 'Ваш результат',
    notPrizePlace: 'Не призовое место',
    place: 'Место',
  },
  headers: {
    main: 'Главная',
    newOrganization: 'Создать новую организацию',
    organizationList: 'Ваши организации',
    newOrganizationBtn: 'Создать новую организацию',
  },
  version: 'Версия',
  auth: {
    authHeader: 'Авторизация',
    enterButton: 'Войти',
    emailLabel: 'Электронная почта',
    passwordLabel: 'Пароль',
    passwordRepeatLabel: 'Повторите пароль',
    setPasswordHeader: 'Введите новый пароль',
    signUpText: 'Ещё нет учётной записи?',
    signUpButton: 'Зарегистрироваться',
    signUpHeader: 'Зарегистрироваться',
    enterText: 'Уже есть учётная запись?',
    resetPasswrodHeader: 'Введите вашу почту',
    wrongCredentialsText: 'Неправильные почта или пароль',
    resetPasswordButton: 'Забыли пароль?',
    resetPasswordSendButton: 'Восстановить пароль',
    setNewPasswordSendButton: 'Подтвердить новый пароль',
    firstNameLabel: 'Имя',
    lastNameLabel: 'Фамилия',
    signUpSuccessText:
      'На вашу почту было отправлено письмо с подтверждением регистрации.',
    signUpSuccessHeader: 'Вы успешно зарегистрированы!',
    signUpConfirmText: 'Войдите в учётную запись, чтобы начать играть.',
    signUpConfirmHeader: 'Ваш аккаунт был активирован!',
    signUpConfirmErrorHeader: 'Что-то пошло не так!',
  },
  textInput: {
    requiredError: 'Обязательное поле!',
  },
  profile: {
    title: 'Профиль',
    email: 'Почта',
    firstName: 'Имя',
    lastName: 'Фамилия',
    edit: 'Редактировать профиль',
    editHeader: 'Редактирование профиля',
    save: 'Сохранить изменения',
    discard: 'Отменить',
  },
};

export default createI18n({
  locale: 'en',
  // TODO: from env.
  fallbackLocale:  'en',
  messeges,
});
