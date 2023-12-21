# CardComponentHelper - методы
##  __Методы
[CheckCardTypeAsync](M_Tessa_Cards_ComponentModel_CardComponentHelper_CheckCardTypeAsync.htm)|
Метод выполняет проверку предполагаемого типа карточки с актуальным, если
информация по предполагаемому типу была указана. В случае несовпадения в
результат валидации validationResult будет записано сообщение об ошибке, а
метод вернёт false.  
---|---  
[CleanCardAsync](M_Tessa_Cards_ComponentModel_CardComponentHelper_CleanCardAsync.htm)|
Очищает место, отведённое для контента файлов, принадлежащих карточке.  
[CleanFilesAsync](M_Tessa_Cards_ComponentModel_CardComponentHelper_CleanFilesAsync.htm)|
Очищает место, отведённое для контента файла. Метод вызывается перед удалением
файла.  
[CreateResponse](M_Tessa_Cards_ComponentModel_CardComponentHelper_CreateResponse.htm)|
Возвращает ответ на универсальный запрос к сервису карточек по заданному
запросу.  
[DeleteContentsAsync](M_Tessa_Cards_ComponentModel_CardComponentHelper_DeleteContentsAsync.htm)|
Удаляет контенты версий файлов, определяемые заданным списком контекстов.  
[ExtendRequestAsync<TRequest, TResponse, TContext,
TExtension>](M_Tessa_Cards_ComponentModel_CardComponentHelper_ExtendRequestAsync__4.htm)|
Дополняет запрос к API карточек цепочками расширений.  
[FixAfterExport(Card)](M_Tessa_Cards_ComponentModel_CardComponentHelper_FixAfterExport.htm)|
Исправляет структуру карточки после экспорта для того, чтобы её можно было
использовать для импорта или для создания по шаблону. Метод устанавливает
версию карточку, равную 0, а также исправляет файлы и задания (при этом не
изменяются секции).  
[FixAfterExport(CardFile)](M_Tessa_Cards_ComponentModel_CardComponentHelper_FixAfterExport_1.htm)|
Исправляет структуру файла после экспорта для того, чтобы её можно было
использовать для импорта или для создания по шаблону.  
[FixAfterExport(CardTask)](M_Tessa_Cards_ComponentModel_CardComponentHelper_FixAfterExport_2.htm)|
Исправляет структуру задания после экспорта для того, чтобы её можно было
использовать для импорта.  
[GetContentContextsAsync](M_Tessa_Cards_ComponentModel_CardComponentHelper_GetContentContextsAsync.htm)|
Возвращает список контекстов, описывающий все версии для заданного списка
файлов.  
[GetInvalidInstanceTypeResponse<TResponse>](M_Tessa_Cards_ComponentModel_CardComponentHelper_GetInvalidInstanceTypeResponse__1.htm)|
Возвращает запрос с сообщением об ошибке валидации, обозначающей
несоответствие типа экземпляра для заданного типа карточки cardType и
ожидаемого типа экземпляра expectedInstanceType.  
[GetStoreMode](M_Tessa_Cards_ComponentModel_CardComponentHelper_GetStoreMode.htm)|
Возвращает способ сохранения карточки по её версии.  
[IsAllowedPhysicalColumn](M_Tessa_Cards_ComponentModel_CardComponentHelper_IsAllowedPhysicalColumn.htm)|
Возвращает признак того, что колонка с заданным именем columnName присутствует
в указанном списке columns и является физической колонкой.  
[IsTemporaryTaskRole](M_Tessa_Cards_ComponentModel_CardComponentHelper_IsTemporaryTaskRole.htm)|
Возвращает признак того, что роль с заданным идентификатором типа является или
заменена на временную роль задания и должна быть удалена после завершения
задания.  
[TryGetCardTypeAsync(Guid, ICardMetadata,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardComponentHelper_TryGetCardTypeAsync.htm)|
Возвращает тип карточки по заданному идентификатору, или null, если тип
карточки не найден.  
[TryGetCardTypeAsync(Nullable<Guid>, String, ICardMetadata,
CancellationToken)](M_Tessa_Cards_ComponentModel_CardComponentHelper_TryGetCardTypeAsync_1.htm)|
Возвращает тип карточки по заданному идентификатору или имени, или null, если
идентификатор и имя равны null или тип карточки не найден по заданным
идентификатору или имени.  
[TryGetUserInfo](M_Tessa_Cards_ComponentModel_CardComponentHelper_TryGetUserInfo.htm)|
Возвращает информацию о пользователе по объекту сессии или false, если
информацию невозможно получить.  
## __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
