# CardSatelliteHelper - методы
##  __Методы
[AddSatelliteToList](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_AddSatelliteToList.htm)|
Добавляет карточку-сателлит в список карточек-сателлитов, который должен
содержаться в пакете основной карточки. Если список не был создан, то он
автоматически создаётся при первом вызове метода.  
---|---  
[ClearSatelliteList](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_ClearSatelliteList.htm)|
Очищает список карточек-сателлитов, если он существовал в пакете основной
карточки (но не удаляет пустой список из структуры).  
[CreateSatelliteInfo](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_CreateSatelliteInfo.htm)|
Создаёт объект
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm),
содержащий информацию по карточке-сателлиту для задания.  
[GenerateSatelliteID](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_GenerateSatelliteID.htm)|
Возвращает идентификатор сателлита, созданный на основе идентификатора типа
сателлита и идентификатора владельца сателлита (карточки или задания).  
[RemoveSatelliteFromList](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_RemoveSatelliteFromList.htm)|
Удаляет из списка карточек-сателлитов, если он существовал в пакете основной
карточки, сателлиты указанного типа. Удаляет пустой список из структуры.  
[SatelliteCardWasFound](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_SatelliteCardWasFound.htm)|
Возвращает признак того, что карточка-сателлит была установлена как
присутствующая в пакете основной карточки, т.е. не равная null.  
[SatelliteCardWasNotFound](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_SatelliteCardWasNotFound.htm)|
Возвращает признак того, что карточка-сателлит была установлена как
отсутствующая в пакете основной карточки.  
[SetSatellite](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_SetSatellite.htm)|
Сохраняет карточку-сателлит в пакете основной карточки.  
[SetSatellitesToDeleteIDList](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_SetSatellitesToDeleteIDList.htm)|
Устанавливает список идентификаторов для сателлитов, которые должны быть
удалены из указанного в satelliteKey списка сателлитов.  
[SetupUniversalSatellite](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_SetupUniversalSatellite.htm)|
Метод для установки параметров универсального сателлита в секцию сателлита.  
[TryGetMainCardIDAndTaskRowID](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetMainCardIDAndTaskRowID.htm)|  
[TryGetMainCardIDAndTaskRowIDAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetMainCardIDAndTaskRowIDAsync.htm)|
Возвращает идентификатор основной карточки и идентификатор задания по
идентификатору карточки-сателлита задания или null, если сателлит не найден.
Возвращает признак того, что карточка запрошенная информация найдена. Вторым
значением возвращает идентификатор основной карточки или Guid.Empty, если
карточка-сателлит не найдена. Третьим значением возвращает идентификатор
задания или Guid.Empty, если карточка-сателлит не найдена.  
[TryGetMainCardIDByTaskRowIDAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetMainCardIDByTaskRowIDAsync.htm)|
Возвращает идентификатор основной карточки по идентификатору задания или null,
если задание не найдено. Поиск выполняется среди активных заданий и среди
записей в истории заданий.  
[TryGetMainCardIDFromSatelliteIDAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetMainCardIDFromSatelliteIDAsync.htm)|
Возвращает идентификатор основной карточки по идентификатору карточки-
сателлита или null, если сателлит не найден.  
[TryGetSatelliteCard](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetSatelliteCard.htm)|
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит не была установлена или была
установлена как отсутствующая.  
[TryGetSatelliteCardList](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetSatelliteCardList.htm)|
Возвращает список карточек-сателлитов, который был установлен в пакете
основной карточки, или null, если карточки-сателлиты не установлены, т.е.
список пустой.  
[TryGetSatelliteIDAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetSatelliteIDAsync.htm)|
Возвращает идентификатор сателлита по идентификатору основной карточки или
null, если сателлит ещё не создан.  
[TryGetSatelliteIDListAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetSatelliteIDListAsync.htm)|
Возвращает список идентификаторов карточек-сателлитов для заданной основной
карточки или null, если список пустой.  
[TryGetSatelliteInfoListAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetSatelliteInfoListAsync.htm)|
Возвращает список объектов
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm),
содержащий информацию по карточкам-сателлитам задач для заданной основной
карточки, или null, если такие список пустой.  
[TryGetSatellitesToDeleteIDList](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetSatellitesToDeleteIDList.htm)|
Получает список идентификаторов для сателлитов из CardStoreRequest, которые
должны быть удалены из указанного в satelliteKey списка сателлитов  
[TryGetSingleSatelliteCardFromList](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetSingleSatelliteCardFromList.htm)|
Возвращает карточку-сателлит, которая была установлена в пакете основной
карточки, или null, если карточка-сателлит указанного типа не была найдена в
списке карточек сателлитов доступном по указанному ключу или список карточек
сателлитов не содержит значений.  
[TryGetTaskSatelliteIDAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetTaskSatelliteIDAsync.htm)|
Возвращает идентификатор карточки-сателлита для задания с заданным
идентификатором, или null, если для задания отсутствует сателлит.  
[TryGetUniversalSatelliteIDAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetUniversalSatelliteIDAsync.htm)|
Возвращает идентификатор сателлита по идентификатору основной карточки,
идентификатору задания и типу сателлита или null, если сателлит ещё не создан.  
[TryGetUniversalSatelliteInfoListAsync](M_Tessa_Cards_Extensions_Templates_CardSatelliteHelper_TryGetUniversalSatelliteInfoListAsync.htm)|
Возвращает список объектов
[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm),
содержащий информацию по карточкам-сателлитам задач для заданной основной
карточки, или null, если такие список пустой.  
## __См. также
#### Ссылки
[CardSatelliteHelper -
](T_Tessa_Cards_Extensions_Templates_CardSatelliteHelper.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
