import pickle as pk
import random
# -*- coding: UTF-8 -*-

def load_file():

    data = pk.load(open('dat.bas', mode='rb'))
    return data


def save_file(data):
    pk.dump(data, open('dat.bas', mode='wb'))

def r():
    quot = ['"Когда-то у меня была работа, но теперь у меня появилось хобби: размозжевывать кабины охуевшим сукам"',
            '"Я бы вступил в полемику, но боюсь дискуссионный лимит моего ебальника исчерпан"',
            '«Почему Уилл Смит играет только чернокожих?? Он что, расист?!"',
            '«Котлеты с макарошками - в рот оно ебись, а с пюрешкой - вот что заебись»',
            '«Когда вы уже запомните: Кавказ - сила, а Чечня - круто! Сколько можно путать?!»',
            '«У тебя спина белая))))))))))»',
            '"Голосуй,не голосуй - все равно получишь хуй"',
            '"Если вас назвали Саша - хуй сосать работа ваша"',
            '"Нажал отписаться - ушел с мужчинами ебаца ихихих"',
            '"Бочку дерьма, ложка мёда портит"',
            '"На завтрак я сегодня хавал темную энергию, укутавшись в незримую материю вселенной,'
            ' и запивая молоком гравитационных волн, разлитых звездами, которых давно нет. Я перевариваю боль вселенной. '
            'Я здесь живу веками. Во тьме, построенной из сгустков атомов рожденных смертью света и сотканных в агонии'
            ' случайных встреч. А теперь я должен сидеть и смотреть на твое тупорылое ебало"',
            '«Хоть мы и не богаты,но живем как депутаты.»',
            'Действуй. Двигайся. Старайся. До толчка терпеть пытайся."',
            '"Тобi пiзда тiкай з села"',
            '"Месть - это блюдо, которое нужно подавать к пиву, а как раз за ним я и иду."',
            '"Карочи заходишь в вк с компа, пишешь другу "ты онлайн?", он пишет "да", а потом ты редактируешь своё сообщение на "ты пидар?" и получается, что он на этот вопрос ответил "да", и типа он признался что он пидар ахпахпахап аруууу"',
            '"Нет, ну кто такие танкисты? Да это пидорасы!"',
            '"ДА ЕСЛИ Я ПРИЕДУ Я БЛЯТЬ УГЛА ДАМ ПЕРЕД ТВОЕЙ ПРИОРОЙ У ТЕБЯ БЛЯТЬ КОЛЕСА ПООТПАДАЮТ ОТ ВИБРАЦИИ ЙОБАНА РОТ"',
            '«Тяжело в учении - легко в отчислении»',
            '«Жизнь прожить - не в поле наложить»',
            '"Вся жизнь - село, а ты в ней городской на каникулах"',
            '"JPG или зассал?"',
            '"Кто носит фирму адидас, тот круче путина в сто раз"',
            '"Люди не шекели - бывают и лишние"',
            '"я в детстве хотел гелик, теперь вырос и хочу велик"',
            '"бляя голоса вконтакте подорожали... как теперь в вормикс донатить"',
            '"Пойду на ночь яжки бахну. Яга яга ягуар- мой волшебный нектар!"',
            '"Я занимаюсь продажей гробов вида б/у"',
            '"Парикмахер дядя Толик, подстриги меня под нолик..."',
            '"Я бы хотел сказать слава КПСС, но ведь вся слава КПРФ"',
            '"Oh shit I\'m sorry"',
            '"блядь горшок умер"',
            '"Что такое божья сила? Божья масса умноженная на божье ускорение. Ну или производная божьего импульса по божьему времени,хуй его знает,в рот ебал я эту физику"',
            '"Предупреждаю - уебу! Предупреждаю - уебал! Предупреждаю - еще уебу!"',
            '"Дискриминант для пацанов, теорема Виета для петухов"',
            '"Слышь, ты меня на слышь-то не бери, слышь!"',
            '"Не наебешь - сквозь пространство-время не пройдешь"',
            '"Накатим пивка для научного рывка"',
            '"Я лягу—ты встанешь"',
            '"Пацаны,гуф умер"',
            '"Дед доест"',
            '"Спид как ветрянка. Лучше переболеть им в детстве"',
            '"Современные теории описывающие разные гендеры - полнейшая чушь. Есть только 2 гендера: боевой вертолет и сельский туалет"',
            '"Всё, вы меня заебали. Цитаток возможно не будет до 2018, так как я буду заниматься гангстерскими андэрграундами"',
            '"Маме я сказал, что уехал на Донбасс, а сам еду на трамвае в магазин гуччи в Санкт-Петербурге"',
            '"Как говорится: нормального человека Павлом не назовут"',
            '"АМАХАСЛ НИГА БИЧ ОХИМИРОН ПИДАРАС КИРПИЧ"',
            '"Школа фу,компьютер класс,кто согласен ставим класс"',
            '"Идет медведь по лесу, видит, машина горит. Сел в нее и сгорел."',
            '"Короче я рэпанулся, зовите меня пожилой гнойный кпрф"',
            '"У России два врага - логарифм и интеграл"',
            '"Хах мне похуй, честно, мне похуй, мне поебать на танки, мне похуй, все танкисты долбаебы"',
            '"Спиннеры крутятся - хромосомы мутятся"',
            '"мдаа,одмен опять говно постит"',
            '"У России два союзника: автоботы и люди Х"',
            '"Лучше быть царем на нарах,чем в агу сидеть на парах"',
            '"Яга - сила, спорт - могила"',
            '"Я че то не пойму. Почему на автарке паблика с моими цитатками какой-то негр?"',
            '"EBLANY, YA NE GOVORYU PO RUSSKI"',
            '"Уважение - это когда физрук здоровается с тобой за руку."',
            '"Хуево когда голову в капюшоне поворачиваешь,а капюшон не поворачивается"',
            '"Мужик не тот, кто баб ебал, а тот, кто в школьном туалете срал"',
            '"Аллах над нами,земля под нами,ножи в кармане, вперед азербайджане!"',
            '"Не люблю когда обещают и не выполняют, когда говорят,что любят,а потом кидают, когда срут и не смывают."',
            '"Совесть - это когда на пляже ищешь туалетную кабинку."',
            '"Настоящее искусство - это незаметно залепить жвачку под парту."',
            '"Если оденешь носок с большой дырой, то обязательно придется зайти к кому-нибудь в гости"',
            '"Зачем откладывать дела на завтра,если можно отложить их нахуй?"',
            '"Мне бы крышу повыше,ночи потише, насвая послаще и пиваса почаще"',
            '"Любая шаурмичная деградирует без конкуренции."',
            '"Бомжур,епта!"',
            '"Кто пиво пьет - сто лет живёт!"',
            '"Питер для понтов, Новоалтайск для пацанов!"',
            '"Ебать меня жмёт"',
            '"Однажды подписчик «Цитат Киану Ривза» назвал мой паблик дерьмом, я ударил его, потому что никто не смеет говорить гадости о моем паблике, затем я ударил себя, потому что никто не смеет бить моих подписчиков, затем он ударил меня, потому что никто не смеет бить Киану Ривза, после чего ударил сам себя, потому что никто не смеет меня бить, затем я ударил его, потому что никто не смеет бить моих подписчиков..."',
            '"Че-то анекдоты в "Телесемь" несмешные("',
            '"Автор предыдущего поста даун"',
            '"Бля,уже 49 подписчиков,не успел про 47 пошутить(((99((9(9("',
            '"Путин - краб"',
            '"Как отличить уберменша от простого быдла? Все уберменши планеты подписаны на мой паблик с цитатками"',
            '"Я завалю любую блядь, кто в падике решит поссать."',
            '"Так блэд"',
            '"1)хуле ты мне сделаеш\nВовторых пошел нахуй\nВтретьих 3)что ты мне сделаеш я в другом городе\nСоре за ма*т"',
            '"В рот я ебал этот ваш егэ,хуета какая-то, в однокласнеках лучше преколы"',
            '"Ты че охуел "Ворониных" дерьмом называть?"',
            '"Самый трудный период в моей жизни начался после того, как мне сказали поднять руки, а потом опустить ту, которой дрочу..."',
            '"Да вы доебали уже со своей зеленкой, я не Навальный!"',
            '"Слушай сюда, Виталий!"',
            '"Я хуй пойму, как мiвiну-то варить правильно?!"',
            '"Приготовить ракету ЗЕМЛЯ-ПИВО к запуску!"',
            '"ДУРОВ ВЕРНИ СТЕНУ!"',
            '"Нэвэльный прийде - порядок наведе"',
            '"Не бойся ложки, бойся вилки.Один удар - 4 дырки"',
            '"ВНИМАНИЕ АНЕКДОТ! У меня компьютер грязный. Я жму "мой компьютер" , а он не моется почему-то."',
            '"Ты че тупа деда оскорбляешь, я ветеринар донбасса ,дважды судим"',
            '"Фартук в масле оливье"',
            '"БЛЯДЬ НЭВЭЛЬНЫЙ"',
            '"Когда ты говоришь, что я левак, голос в моей душе ропщет:\nЯ настолько коммунист, что сделал твою мамку общей"',
            '"Уроки учат только лохи, а пацаны ебут ладохи!"',
            '"Бля, надо запомнить этот район, тут шавуха за 80!"',
            '"Есть тема одна. Ссышь на тарелку, ставишь в морозильник, ждешь, когда все превратится в твёрдый желтый блин, засовываешь соседу под дверь, а он потом охуевает, что у него дома нассано!"',
            '"Помогите, мне во снах приходят хохлы, каждую ночь, они кушают сало и ругают меня. Я говорю им, уходите хохлы, уходите! А они не уходят, что мне делать?"',
            '"Зачем жрать капусту, если есть картошка?"',
            '"НЕ ТУДА ВОЮЕШЬ, ЕБЛАН!"',
            '"Ебнй нсрл, кк ж я упрлся. Сттхм ты прнс?"',
            '"СУКА! МЕНЯ ЗАГРИФЕРИЛИ!!!!((((("',
            '"GOD LEFT ME UNFINISHED!"',
            '"Алё, здрасьте, у вас есть присыпочка белая для пиццы, которая патау-дцп-додик?"',
            '"ДОБРОГО РАНКУ, МОЯ УКРАЇНА! ДОБРОГО РАНКУ, ДЕРЖАВА МОЯ!"',
            '"Школу можно пропустить, а за качалку пизды получишь!"',
            '"Ты в пиве"',
            '"Жизнь без ягуара - как жизнь без кислорода, только без ягуара."',
            '"Мне наплевать, если я заболею - буду лечиться насваем неделю!"',
            '"Это цой-то пидарас и хуесос?!! Да тебе нормальные ребята за такие слова палкой бы переебали!!!!!!!"',
            '"Хуже раковой опухоли может быть только подписчик, желающий видеть регулярно обновляемый контент в паблике с цитатками"',
            '"БУРЖУЙ - ГОВНА ПОЖУЙ!"',
            '"Не страшно когда тебе не хватает на еду, страшно когда тебе не хватает на жижку для вейпа."',
            '"БЕНК БЕНК БЕНК! БАТЯ В ЗДАНИИ!"',
            '"Вы не поняли. Водка внутри, а снаружи бутылка."',
            '"Кек или не кек - вот в чем вопрос."',
            '"Слышь ты че, тварь, охуел деревню не уважать?!"',
            '"На пятки встал - уважение потерял"',
            '"Я слеп, но я вижу, что ты охуел.\nЯ глух, но я слышу, что ты охуел.\nЯ нем, но я говорю, что ты охуел."',
            '"Обама - чмо!"',
            '"Слышь, ты че говна поел?!"',
            '"ALLO YOBA ETO TY?"',
            '"Русский рэп - говнище ебаное"',
            '"Вы кто такие? Я вас не звал. Идите нахуй!"',
            '"чё надо, сука?"',
            '"Вот было бы круто, если б уроки шли по 15 минут!!!"',
            '"Да ты поторопись! У нас щас обед! Котлетки!"',
            '"Здравствуйте, у вас есть шаурма?"',
            '"4 это зека короче с это с омска сбежали сильно прям на судебном заседании как мы его всеми своими ребятами захват перехват сделали поломали сложили обратно всё"'
            ]
    random_phrases = ['Как вы относитесь к Биллу Гейтсу',
                      'Слава КПРФ',
                      'Ты в пиве'
                      'Слава Украiнi',
                      'Це ж москальска мова',
                      'УЙДИ ПАВУЧАРА',
                      'каво',
                      'шо',
                      'блэд нэвэльный',
                      'извенись',
                      'не слышу',
                      'Ну что,может по пивговну?',
                      'Не розумію, що ти балакаєш',
                      'Помогите, я из подъезда выйти не могу, там большая собака сидит',
                      'Навально',
                      'ОНОТОЛЕ ГАЛАКТИКЕ ОТАКУЭ ПЫЩЬ ПЫЩЬ ПОПЯЧСО ПОПЯЧСО',
                      'Казалосб бы причем здес укроина',
                      'Я ПАЖИЛОЙ РЕПЕР',
                      'Я пажилой путин фбк',
                      'извините я в метро пшшшшшшшш',
                      'ТЕБЯ БИКАНУТЬ?',
                      'ВОТ ТЕБЕ ЩАС КАЖЕТСЯ ЧТО Я НЕ МАШИНА НИХУЯ А БЫК ОБЫЧНЫЙ НО Я РЕАЛЬНО МАШИНА',
                      'Нi понiв',
                      'ore wa ochinchin ga daisuki nandayo',
                      'HAMBURGER PLISS',
                      'habe u sin an alien plis?',
                      'ey b0ss, i habe a cancer',
                      'тю те шо ебало разбить?']
    n = []
    phras = {'Слава Украине': ['Героям слава', 'Пошел нахуй какол', 'Я доложу президенту'],
             'тю те шо ебало разбить?': ['да иди нахуй'],
             'мне сейчас послышалось?': ['тю те шо ебало разбить?']}
    data = {'1': random_phrases, '2': phras, '3': quot}
    save_file(data)
    return data


data = load_file()

print("Це чат-бот, чтобы побалакать напишите ему.\n")
ai = ''
while 1>0:
    flag = 0
    data = load_file()
    man = input()
    if man == '000':
        save_file(data)
        exit(0)
    else:
        if ai in data['2'].keys() and ai != '':
            if man not in data['2'][ai] and man != '' and 'цитат' not in man:
                data['2'][ai].append(man)
        else:
            t = [man]
            data['2'][ai] = t
        if 'цитат' in man:
            ai = random.choice(data['3'])
            flag = 1
        elif man in data['2'].keys():
                ai = random.choice(data['2'][man])
        else:
            if man not in data['1']:
                data['1'].append(man)
            ai = random.choice(data['1'])
        save_file(data)
        print(ai)
        if flag == 1:
            ai = ''

        print(data['2'])