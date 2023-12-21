# CardRequestExtensions - класс
Расширения для запросов и ответов на запросы к сервису карточек, контекста
расширений карточек, а также для дополнительных настроек UI в пакете карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardRequestExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class CardRequestExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class CardRequestExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type CardRequestExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardRequestExtensions
##  __Методы
[AddCardIDToLoadSignatures](M_Tessa_Cards_CardRequestExtensions_AddCardIDToLoadSignatures.htm)|
Добавляет идентификатор карточки в список идентификаторов, для которых будут
загружены подписи для файлов, помимо текущей загруженной карточки. Используйте
для виртуальных файлов, относящихся к другим карточкам, которые добавлены в
загруженную карточку. Подписи загружаются в CardGetExtension.AfterRequest на
этапе ExtensionStage.Platform, поэтому список идентификаторов должен быть
установлен раньше. Возвращает признак того, что идентификатор был добавлен,
т.к. отсутствовал в списке.  
---|---  
[AddInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_AddInvalidateCompletedCacheNames.htm)|
Добавляет имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null и пустой список идентичны. Пустой список означает, что сброс
кэшей не выполняется.  
[ClearCardIDListToLoadSignatures](M_Tessa_Cards_CardRequestExtensions_ClearCardIDListToLoadSignatures.htm)|
Очищает список идентификаторов карточек, для которых будут загружены подписи
для файлов. Возвращает признак того, что список присутствовал перед вызовом
метода.  
[ClearInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_ClearInvalidateCompletedCacheNames.htm)|
Очищает имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).  
[ClearOriginalVersion](M_Tessa_Cards_CardRequestExtensions_ClearOriginalVersion.htm)|
Удаляет информацию об оригинальной версии карточки.  
[EnsureDecompressed](M_Tessa_Cards_CardRequestExtensions_EnsureDecompressed.htm)|
Гарантирует, что ответ на запрос по получению карточки не содержит сжатую
карточку. Если карточка сжата, то метод производит её декомпрессию.  
[GetAdditionalFiles](M_Tessa_Cards_CardRequestExtensions_GetAdditionalFiles.htm)|
Возвращает список дополнительных файлов [CardFile](T_Tessa_Cards_CardFile.htm)
в ответе на запрос на экспорт карточки. Если объект не существовал, то он
будет добавлен.  
[GetADFSAuthenticationResponse](M_Tessa_Cards_CardRequestExtensions_GetADFSAuthenticationResponse.htm)|
Возвращает сериализованную в XML информацию в виде строки, которая получена
при автоматическом создании сотрудника средствами ADFS, или null, если не
выполняется автоматическое создание сотрудника.  
[GetCard](M_Tessa_Cards_CardRequestExtensions_GetCard.htm)|  Возвращает
карточку, используемую в универсальном запросе к API карточек.  
[GetDigestCard](M_Tessa_Cards_CardRequestExtensions_GetDigestCard.htm)|
Возвращает карточку, используемую для получения Digest в расширениях.  
[GetFile](M_Tessa_Cards_CardRequestExtensions_GetFile.htm)|  Возвращает файл,
используемый в универсальном запросе к API карточек.  
[GetFileMapping](M_Tessa_Cards_CardRequestExtensions_GetFileMapping.htm)|
Возвращает список объектов с маппингом для контента файлов
[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm) в ответе на
запрос на экспорт карточки. Если объект не существовал, то он будет добавлен.  
[GetForbidStoringHistory(CardDeleteRequest)](M_Tessa_Cards_CardRequestExtensions_GetForbidStoringHistory.htm)|
Возвращает запрет на сохранение данных об удаляемой карточке в историю
действий с карточкой.  
[GetForbidStoringHistory(CardGetFileContentRequest)](M_Tessa_Cards_CardRequestExtensions_GetForbidStoringHistory_1.htm)|
Возвращает запрет на сохранение данных о загружаемом файле карточки в историю
действий с карточкой.  
[GetForbidStoringHistory(CardGetRequest)](M_Tessa_Cards_CardRequestExtensions_GetForbidStoringHistory_2.htm)|
Возвращает запрет на сохранение данных о загружаемой карточке в историю
действий с карточкой.  
[GetForbidStoringHistory(CardGetResponse)](M_Tessa_Cards_CardRequestExtensions_GetForbidStoringHistory_3.htm)|
Возвращает запрет на сохранение данных о загруженной карточке в историю
действий с карточкой.  
[GetForbidStoringHistory(CardStoreRequest)](M_Tessa_Cards_CardRequestExtensions_GetForbidStoringHistory_4.htm)|
Возвращает запрет на сохранение данных о сохраняемой карточке в историю
действий с карточкой.  
[GetIgnoreExternalSourceContent](M_Tessa_Cards_CardRequestExtensions_GetIgnoreExternalSourceContent.htm)|
Возвращает признак того, что при сохранении карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение. Если признак не был установлен, то возвращается false.  
[GetIgnorePermissionsWarning](M_Tessa_Cards_CardRequestExtensions_GetIgnorePermissionsWarning.htm)|
Возвращает признак того, что при сохранении карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение. Если признак не был установлен, то возвращается false.  
[GetIgnoreTaskAccessCheckList](M_Tessa_Cards_CardRequestExtensions_GetIgnoreTaskAccessCheckList.htm)|
Возвращает массив, содержащий список идентификаторов заданий, для которых не
выполняется проверка на права. Массив всегда не равен null.  
[GetInstanceIDList](M_Tessa_Cards_CardRequestExtensions_GetInstanceIDList.htm)|
Получает список идентификаторов карточек с указанием типа экземпляра таких
карточек. Если список не был установлен, то возвращается пустой список, не
равный null.  
[GetKeepTaskDialog(CardResponseBase)](M_Tessa_Cards_CardRequestExtensions_GetKeepTaskDialog_1.htm)|
Возвращает значение показывающее требуется ли оставить открытым окно диалога
или нет.  
[GetKeepTaskDialog(Dictionary<String,
Object>)](M_Tessa_Cards_CardRequestExtensions_GetKeepTaskDialog.htm)|
Возвращает значение показывающее требуется ли оставить открытым окно диалога
или нет.  
[GetNoLockingMainCard(CardRequestBase)](M_Tessa_Cards_CardRequestExtensions_GetNoLockingMainCard.htm)|
Возвращает признак того, что не следует выполнять блокировку основной карточки
при создании или изменении сателлита.  
[GetNoLockingMainCard(CardStoreRequest)](M_Tessa_Cards_CardRequestExtensions_GetNoLockingMainCard_1.htm)|
Возвращает признак того, что не следует выполнять блокировку основной карточки
при создании или изменении сателлита.  
[GetRestoreMode](M_Tessa_Cards_CardRequestExtensions_GetRestoreMode.htm)|
Возвращает признак того, что при удалении удалённой карточки одновременно
выполняется восстановление карточки, которая была удалена.  
[GetTypeIDList(CardResponse)](M_Tessa_Cards_CardRequestExtensions_GetTypeIDList.htm)|
Возвращает список идентификаторов типов карточек в виде массива. Размер
массива определяется по количеству элементов в запросе. Массив не равен null.
Элементы возвращаемого массива равны null, если для идентификатора карточки,
переданного в запросе на соответствующей позиции, не найден идентификатор.  
[GetTypeIDList(CardResponse,
Int32)](M_Tessa_Cards_CardRequestExtensions_GetTypeIDList_1.htm)|  Возвращает
список идентификаторов типов карточек в виде массива заданного размера.
Элементы возвращаемого массива равны null, если для идентификатора карточки,
переданного в запросе на соответствующей позиции, не найден идентификатор.  
[GetVisibleTiles](M_Tessa_Cards_CardRequestExtensions_GetVisibleTiles.htm)|
Возвращает массив, содержащий список всех видимых плиток. Массив всегда не
равен null. Данные видимости обычно устанавливаются при создании или загрузке
карточки, в т.ч. на сервере.  
[GetWithoutBackupOnly](M_Tessa_Cards_CardRequestExtensions_GetWithoutBackupOnly.htm)|
Возвращает признак того, что пользователем запрошено принудительное удаление
карточки без возможности восстановления. Если признак не был установлен, то
возвращается false.  
[HasTypeIDList](M_Tessa_Cards_CardRequestExtensions_HasTypeIDList.htm)|
Возвращает признак того, что список идентификаторов типов карточек был
установлен в ответе на запрос к сервису карточек
[CardResponse](T_Tessa_Cards_CardResponse.htm).  
[IgnoreTaskAccessCheck](M_Tessa_Cards_CardRequestExtensions_IgnoreTaskAccessCheck.htm)|
Возвращает признак того, что для задания с указанным идентификатором не
выполняется проверка прав.  
[InvalidateCacheAsync](M_Tessa_Cards_CardRequestExtensions_InvalidateCacheAsync.htm)|
Выполняет запрос по сбросу кэшей на сервере. Может быть вызван с сервера или
клиента для сессии пользователя с правами администратора. Если в качестве
списка имён cacheNames указывается null, то выполняется сброс всех кэшей; если
указан пустой массив, то сброс не будет выполнен, однако, запрос будет запущен
(т.е. расширения могут определить список кэшей для сброса сами). Возвращает
результат выполнения операции, который не равен null.  
[IsADFSAuthenticationResponseExists](M_Tessa_Cards_CardRequestExtensions_IsADFSAuthenticationResponseExists.htm)|
Возвращает признак того, что в заданном запросе автоматически создаётся
сотрудник при входе в ADFS, т.е. при успешной авторизации по ADFS для
сотрудника, отсутствующего в Tessa, создаётся и заполняется карточка.  
[IsInvalidatingAllCaches](M_Tessa_Cards_CardRequestExtensions_IsInvalidatingAllCaches.htm)|
Возвращает признак того, что запрошен сброс всех кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).  
[IsPartiallyLoaded](M_Tessa_Cards_CardRequestExtensions_IsPartiallyLoaded.htm)|
Возвращает признак того, что карточка может быть загружена частично (например,
без расширений), поэтому не все её поля могут быть корректно заполнены.
Актуально, например, для карточки, загруженной в контексте для действий с
номерами.  
[RemoveInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_RemoveInvalidateCompletedCacheNames.htm)|
Удаляет имена фактически сброшенных кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null и пустой список идентичны. Пустой список означает, что сброс
кэшей не выполняется.  
[ResetAllTaskAccessCheckIgnores](M_Tessa_Cards_CardRequestExtensions_ResetAllTaskAccessCheckIgnores.htm)|
Удаляет всю информацию по заданиям, для которых не выполняется проверка прав.
Возвращает признак того, что информация присутствовала перед удалением.  
[ResetAllTilesVisibility](M_Tessa_Cards_CardRequestExtensions_ResetAllTilesVisibility.htm)|
Удаляет всю информацию по видимости плиток. Плитки, которые используют
информацию по видимости, будут считать себя скрытыми. Возвращает признак того,
что информация присутствовала перед удалением.  
[ResetRequestToCache](M_Tessa_Cards_CardRequestExtensions_ResetRequestToCache.htm)|
Сбрасывает признак того, что запрос на получение карточки должен обращаться к
кэшу. После выполнения метода запрос будет выполняться стандартным образом,
т.е. в обход кэша. Значение актуально для карточек-синглтонов.  
[SetActionHistoryRowID](M_Tessa_Cards_CardRequestExtensions_SetActionHistoryRowID.htm)|
Устанавливает идентификатор записи в историю действий, которая была записана в
процессе обработки запроса, или null, если требуется удалить предыдущий
идентификатор.  
[SetAdditionalFiles](M_Tessa_Cards_CardRequestExtensions_SetAdditionalFiles.htm)|
Устанавливает список дополнительных файлов
[CardFile](T_Tessa_Cards_CardFile.htm) в ответе на запрос на экспорт карточки.  
[SetAddToRolesIDList](M_Tessa_Cards_CardRequestExtensions_SetAddToRolesIDList.htm)|
Устанавливает список идентификаторов ролей, в которые должен быть добавлен
создаваемый сотрудник в запросе на создание (первое сохранение) карточки
сотрудника [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). Если при
включении сотрудника в одну из ролей возникнет ошибка, то она будет добавлена
как предупреждение, и включение в другие роли, а также сохранение завершатся
успешно.  
[SetADFSAuthenticationResponse](M_Tessa_Cards_CardRequestExtensions_SetADFSAuthenticationResponse.htm)|
Устанавливает сериализованную в XML информацию в виде строки, которая получена
при автоматическом создании сотрудника средствами ADFS, или null, если
информацию требуется удалить.  
[SetBackground](M_Tessa_Cards_CardRequestExtensions_SetBackground.htm)|
Устанавливает цвет фона для задания.  
[SetCard](M_Tessa_Cards_CardRequestExtensions_SetCard.htm)|  Устанавливает
карточку для использования в универсальном запросе к API карточек.  
[SetCardToDelete](M_Tessa_Cards_CardRequestExtensions_SetCardToDelete.htm)|
Устанавливает карточку, для которой выполняется удаление с восстановлением,
окончательное удаление или восстановление, или null, если установленную
карточку требуется удалить.  
[SetContextData](M_Tessa_Cards_CardRequestExtensions_SetContextData.htm)|
Устанавливает данные в контексте цепочки расширений для заданного объекта-
отправителя sender. Данные существует в пределах цепочки расширений.  
[SetConverterFormat(CardGetFileContentRequest,
FileConverterFormat)](M_Tessa_Cards_CardRequestExtensions_SetConverterFormat_1.htm)|
Устанавливает, что загружаемое содержимое должно быть сконвертировано в
указанный формат.  
[SetConverterFormat(IDictionary<String, Object>,
FileConverterFormat)](M_Tessa_Cards_CardRequestExtensions_SetConverterFormat.htm)|
Устанавливает, что загружаемое содержимое должно быть сконвертировано в
указанный формат.  
[SetDigest(CardInfoStorageObject,
String)](M_Tessa_Cards_CardRequestExtensions_SetDigest_1.htm)|  Устанавливает
Digest для сохранения в историю действий с карточкой.  
[SetDigest(Dictionary<String, Object>,
String)](M_Tessa_Cards_CardRequestExtensions_SetDigest.htm)|  Устанавливает
Digest для сохранения в историю действий с карточкой.  
[SetDigestCard](M_Tessa_Cards_CardRequestExtensions_SetDigestCard.htm)|
Устанавливает карточку, используемую для получения Digest в расширениях.  
[SetDigestEventName(CardRequest,
String)](M_Tessa_Cards_CardRequestExtensions_SetDigestEventName_1.htm)|
Устанавливает имя события по расчёту Digest для сохранения в историю действий
с карточкой.  
[SetDigestEventName(Dictionary<String, Object>,
String)](M_Tessa_Cards_CardRequestExtensions_SetDigestEventName.htm)|
Устанавливает имя события по расчёту Digest для сохранения в историю действий
с карточкой.  
[SetDisableExpandJsonFlag](M_Tessa_Cards_CardRequestExtensions_SetDisableExpandJsonFlag.htm)|
Устанавливает флаг, указывающий на то, что при экспорте карточки не нужно
разворачивать JSON-поля карточки из строки в Dictionary<string, object>.  
[SetDisallowCaching](M_Tessa_Cards_CardRequestExtensions_SetDisallowCaching.htm)|
Устанавливает признак того, что не следует выполнять кэширование результата.  
[SetFile](M_Tessa_Cards_CardRequestExtensions_SetFile.htm)|  Устанавливает
файл для использования в универсальном запросе к API карточек.  
[SetFileMapping](M_Tessa_Cards_CardRequestExtensions_SetFileMapping.htm)|
Устанавливает список объектов с маппингом для контента файлов
[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm) в ответе на
запрос на экспорт карточки.  
[SetFileSource](M_Tessa_Cards_CardRequestExtensions_SetFileSource.htm)|
Устанавливает местоположение контента файла.  
[SetForbidFileStoreChanging](M_Tessa_Cards_CardRequestExtensions_SetForbidFileStoreChanging.htm)|
Устанавливает признак того, что для файлов сохраняемой карточки запрещено
изменять местоположение контента при сохранении.  
[SetForbidStoringHistory(CardDeleteRequest,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetForbidStoringHistory.htm)|
Устанавливает запрет на сохранение данных об удаляемой карточке в историю
действий с карточкой. Вызов метода в клиентских расширениях запрещён, это
приведёт к ошибке
[RequestFromClientCheckFailed](F_Tessa_Cards_CardValidationKeys_RequestFromClientCheckFailed.htm).  
[SetForbidStoringHistory(CardGetFileContentRequest,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetForbidStoringHistory_1.htm)|
Устанавливает запрет на сохранение данных о загружаемом файле карточки в
историю действий с карточкой. Вызов метода в клиентских расширениях запрещён,
это приведёт к ошибке
[RequestFromClientCheckFailed](F_Tessa_Cards_CardValidationKeys_RequestFromClientCheckFailed.htm).  
[SetForbidStoringHistory(CardGetRequest,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetForbidStoringHistory_2.htm)|
Устанавливает запрет на сохранение данных о загружаемой карточке в историю
действий с карточкой. Вызов метода в клиентских расширениях запрещён, это
приведёт к ошибке
[RequestFromClientCheckFailed](F_Tessa_Cards_CardValidationKeys_RequestFromClientCheckFailed.htm).  
[SetForbidStoringHistory(CardGetResponse,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetForbidStoringHistory_3.htm)|
Устанавливает запрет на сохранение данных о загруженной карточке в историю
действий с карточкой.  
[SetForbidStoringHistory(CardStoreRequest,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetForbidStoringHistory_4.htm)|
Устанавливает запрет на сохранение данных о сохраняемой карточке в историю
действий с карточкой. Вызов метода в клиентских расширениях запрещён, это
приведёт к ошибке
[RequestFromClientCheckFailed](F_Tessa_Cards_CardValidationKeys_RequestFromClientCheckFailed.htm).  
[SetForceTaskPanel](M_Tessa_Cards_CardRequestExtensions_SetForceTaskPanel.htm)|  
[SetIgnoreExternalSourceContent](M_Tessa_Cards_CardRequestExtensions_SetIgnoreExternalSourceContent.htm)|
Устанавливает признак того, что при обработке файла системой не следует
учитывать свойство [ExternalSource](P_Tessa_Cards_CardFile_ExternalSource.htm)
как необходимость копировать контент файла. Например, при создании шаблона
контент копируется средствами расширения и не должен копироваться системой.  
[SetIgnorePermissionsWarning](M_Tessa_Cards_CardRequestExtensions_SetIgnorePermissionsWarning.htm)|
Устанавливает признак того, что при обработке карточки могут быть не указаны
токены безопасности, поэтому не следует показывать соответствующее
предупреждение.  
[SetImportVersion](M_Tessa_Cards_CardRequestExtensions_SetImportVersion.htm)|
Устанавливает оригинальную версию импортируемой карточки, которую требуется
восстановить.  
[SetInstanceIDList](M_Tessa_Cards_CardRequestExtensions_SetInstanceIDList.htm)|
Устанавливает список идентификаторов карточек с указанием типа экземпляра
таких карточек в запросе к сервису карточек
[CardRequest](T_Tessa_Cards_CardRequest.htm).  
[SetInvalidateCacheNames(CardRequest,
IEnumerable<String>)](M_Tessa_Cards_CardRequestExtensions_SetInvalidateCacheNames.htm)|
Устанавливает имена сбрасываемых кэшей в запросе
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null определяет, что выполняется сброс всех кэшей. Пустой список
означает, что сброс кэшей не выполняется.  
[SetInvalidateCacheNames(ICardRequestExtensionContext,
IEnumerable<String>)](M_Tessa_Cards_CardRequestExtensions_SetInvalidateCacheNames_1.htm)|
Устанавливает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Значение null определяет, что выполняется сброс всех кэшей. Пустой список
означает, что сброс кэшей не выполняется.  
[SetKeepTaskDialog(CardResponseBase,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetKeepTaskDialog_1.htm)|
Устанавливает в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) объекта
[CardResponseBase](T_Tessa_Cards_CardResponseBase.htm) флаг показывающий
требуется ли оставить открытым окно диалога или нет.  
[SetKeepTaskDialog(IDictionary<String, Object>,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetKeepTaskDialog.htm)|
Устанавливает в указанный словарь флаг показывающий требуется ли оставить
открытым окно диалога или нет.  
[SetLoadData](M_Tessa_Cards_CardRequestExtensions_SetLoadData.htm)|
Устанавливает признак того, что следует выполнить загрузку бинарных данных.  
[SetNoLockingMainCard(CardRequestBase,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetNoLockingMainCard.htm)|
Устанавливает признак того, что не следует выполнять блокировку основной
карточки при создании или изменении сателлита.  
[SetNoLockingMainCard(CardStoreRequest,
Boolean)](M_Tessa_Cards_CardRequestExtensions_SetNoLockingMainCard_1.htm)|
Устанавливает признак того, что не следует выполнять блокировку основной
карточки при создании или изменении сателлита.  
[SetOriginalVersion](M_Tessa_Cards_CardRequestExtensions_SetOriginalVersion.htm)|
Устанавливает оригинальную версию карточки, которая была очищена при экспорте.  
[SetPartiallyLoaded](M_Tessa_Cards_CardRequestExtensions_SetPartiallyLoaded.htm)|
Устанавливает признак того, что карточка может быть загружена частично
(например, без расширений), поэтому не все её поля могут быть корректно
заполнены. Актуально, например, для карточки, загруженной в контексте для
действий с номерами.  
[SetPluginType](M_Tessa_Cards_CardRequestExtensions_SetPluginType.htm)|
Устанавливает тип плагина при выполнении запроса к карточке из плагина
Chronos. Стандартные типы перечислены в
[CardPluginTypes](T_Tessa_Cards_CardPluginTypes.htm).  
[SetRepairSectionsFlag](M_Tessa_Cards_CardRequestExtensions_SetRepairSectionsFlag.htm)|
Устанавливает флаг, который указывает на то, что нужно починить (добавить)
строковые секции карточки в случае, если они отсутствуют в БД.  
[SetRequestToCache](M_Tessa_Cards_CardRequestExtensions_SetRequestToCache.htm)|
Устанавливает признак того, что запрос на получение карточки должен обращаться
к кэшу. Значение актуально для карточек-синглтонов.  
[SetRestoreMode](M_Tessa_Cards_CardRequestExtensions_SetRestoreMode.htm)|
Устанавливает признак того, что при удалении удалённой карточки одновременно
выполняется восстановление карточки, которая была удалена.  
[SetRows](M_Tessa_Cards_CardRequestExtensions_SetRows.htm)|  Устанавливает
строки коллекционной или древовидной секции в ответе на универсальный запрос к
карточке.  
[SetSectionRows](M_Tessa_Cards_CardRequestExtensions_SetSectionRows.htm)|
Устанавливает пустые строки коллекционных и древовидных секций в ответе на
универсальный запрос к карточке.  
[SetStorageFilePaths](M_Tessa_Cards_CardRequestExtensions_SetStorageFilePaths.htm)|
Устанавливает пути и имена файлов которые должны быть записаны в отдельные
файлы, относительно структуры карточки  
[SetSuggestedFileName](M_Tessa_Cards_CardRequestExtensions_SetSuggestedFileName.htm)|
Устанавливает предпочитаемое имя файла, которое используется для загрузки
предпросмотра или создания файла по шаблону.  
[SetTaskAccessCheckIsIgnored](M_Tessa_Cards_CardRequestExtensions_SetTaskAccessCheckIsIgnored.htm)|
Устанавливает признак того, что для задания с указанным идентификатором не
выполняется проверка прав.  
[SetTemplateCard(CardNewRequest,
Card)](M_Tessa_Cards_CardRequestExtensions_SetTemplateCard_1.htm)|
Устанавливает карточку шаблона в запросе на создание структуры карточки.  
[SetTemplateCard(CardRequest,
Card)](M_Tessa_Cards_CardRequestExtensions_SetTemplateCard_2.htm)|
Устанавливает карточку шаблона в универсальном запросе к карточке.  
[SetTemplateCard(CardResponse,
Card)](M_Tessa_Cards_CardRequestExtensions_SetTemplateCard_3.htm)|
Устанавливает карточку шаблона в ответе на универсальный запрос к карточке.  
[SetTemplateCard(Dictionary<String, Object>,
Card)](M_Tessa_Cards_CardRequestExtensions_SetTemplateCard.htm)|
Устанавливает карточку шаблона в запросе на создание структуры карточки.  
[SetTemplateCardID(CardNewRequest,
Nullable<Guid>)](M_Tessa_Cards_CardRequestExtensions_SetTemplateCardID_1.htm)|
Устанавливает идентификатор карточки шаблона, по которому требуется создать
карточку. При этом в запросе должен быть установлен идентификатор типа
карточки [CardTypeID](P_Tessa_Cards_CardNewRequest_CardTypeID.htm), равный
типу карточки шаблона
[TemplateTypeID](F_Tessa_Cards_CardHelper_TemplateTypeID.htm).  
[SetTemplateCardID(Dictionary<String, Object>,
Nullable<Guid>)](M_Tessa_Cards_CardRequestExtensions_SetTemplateCardID.htm)|
Устанавливает идентификатор карточки шаблона, по которому требуется создать
карточку. При этом в запросе должен быть установлен идентификатор типа
карточки [CardTypeID](P_Tessa_Cards_CardNewRequest_CardTypeID.htm), равный
типу карточки шаблона
[TemplateTypeID](F_Tessa_Cards_CardHelper_TemplateTypeID.htm).  
[SetTemplateCreatedFromCard](M_Tessa_Cards_CardRequestExtensions_SetTemplateCreatedFromCard.htm)|
Устанавливает признак того, что карточка шаблона создаётся из другой карточки,
а не в результате создания по шаблону из экспортированной карточки шаблона.  
[SetTemplateWasRepaired](M_Tessa_Cards_CardRequestExtensions_SetTemplateWasRepaired.htm)|
Устанавливает признак того, что карточка шаблона была исправлена после
изменения схемы данных.  
[SetTileIsVisible](M_Tessa_Cards_CardRequestExtensions_SetTileIsVisible.htm)|
Устанавливает признак того, должна ли плитка быть видимой. Рекомендуется
вызывать метод при создании или загрузке карточки, в т.ч. на сервере.  
[SetTitle](M_Tessa_Cards_CardRequestExtensions_SetTitle.htm)|  Устанавливает
заголовок задания, который выводится вместо типа задания.  
[SetTypedRequest<TRequest>](M_Tessa_Cards_CardRequestExtensions_SetTypedRequest__1.htm)|
Устанавливает строготипизированный запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm).  
[SetTypedResponse<TResponse>](M_Tessa_Cards_CardRequestExtensions_SetTypedResponse__1.htm)|
Устанавливает строготипизированный ответ на запрос для универсальных
расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm).  
[SetTypeIDList](M_Tessa_Cards_CardRequestExtensions_SetTypeIDList.htm)|
Устанавливает список идентификаторов типов карточек в ответе на запрос к
сервису карточек [CardResponse](T_Tessa_Cards_CardResponse.htm).  
[SetWarningIfEntryNotFoundFlag](M_Tessa_Cards_CardRequestExtensions_SetWarningIfEntryNotFoundFlag.htm)|
Устанавливает флаг, указывающий на то, что в случае отсутствия строковой
секции в БД, будет сгенерировано предупреждение, а не ошибка.  
[SetWipeDeletedFlag](M_Tessa_Cards_CardRequestExtensions_SetWipeDeletedFlag.htm)|
Устанавливает флаг, который указывает на то, что нужно очищать удаленные в
корзину карточки, если они будут мешать импорту.  
[SetWithoutBackupOnly](M_Tessa_Cards_CardRequestExtensions_SetWithoutBackupOnly.htm)|
Устанавливает признак того, что пользователем запрошено принудительное
удаление карточки без возможности восстановления.  
[ShouldExpandJson](M_Tessa_Cards_CardRequestExtensions_ShouldExpandJson.htm)|
Возвращает признак того, что нужно разворачивать JSON-поля карточки из строки
в Dictionary<string, object>.  
[ShouldInvalidateCache](M_Tessa_Cards_CardRequestExtensions_ShouldInvalidateCache.htm)|
Проверяет необходимость сброса кэша в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm).
Возвращает true, если был запрошен сброс указанного кэша или всех кэшей.  
[TileIsVisible](M_Tessa_Cards_CardRequestExtensions_TileIsVisible.htm)|
Возвращает признак того, что плитка с заданным именем должна быть видимой.
Данные видимости обычно устанавливаются при создании или загрузке карточки, в
т.ч. на сервере.  
[TryGetActionHistoryRowID](M_Tessa_Cards_CardRequestExtensions_TryGetActionHistoryRowID.htm)|
Возвращает идентификатор записи в историю действий, которая была записана в
процессе обработки запроса, или null, если записи в истории действий не было
сделано.  
[TryGetAdditionalFiles](M_Tessa_Cards_CardRequestExtensions_TryGetAdditionalFiles.htm)|
Возвращает список дополнительных файлов [CardFile](T_Tessa_Cards_CardFile.htm)
в ответе на запрос на экспорт карточки, или null, если строки не были заданы.  
[TryGetAddToRolesIDList](M_Tessa_Cards_CardRequestExtensions_TryGetAddToRolesIDList.htm)|
Получает список идентификаторов ролей, в которые должен быть добавлен
создаваемый сотрудник, или null, аналогичный пустому списку.  
[TryGetBackground](M_Tessa_Cards_CardRequestExtensions_TryGetBackground.htm)|
Возвращает цвет фона для задания или null, если цвет фона не установлен.  
[TryGetCardIDListToLoadSignatures](M_Tessa_Cards_CardRequestExtensions_TryGetCardIDListToLoadSignatures.htm)|
Возвращает список идентификаторов карточек, для которых будут загружены
подписи для файлов, помимо текущей загруженной карточки, или null, если список
не был создан или был очищен.  
[TryGetCardToDelete](M_Tessa_Cards_CardRequestExtensions_TryGetCardToDelete.htm)|
Возвращает карточку, для которой выполняется удаление с восстановлением,
окончательное удаление или восстановление, или null, если карточка неизвестна.
Рекомендуется использовать метод в цепочке расширений на удаление карточки,
для которой выполняется удаление с восстановлением, или на удаление карточки
Deleted, причём значение заполнено начиная с
[AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm)
этапа [AfterPlatform](T_Tessa_Extensions_ExtensionStage.htm)  
[TryGetContextData<T>](M_Tessa_Cards_CardRequestExtensions_TryGetContextData__1.htm)|
Возвращает данные, записанные методом [SetContextData(ICardExtensionContext,
Object, Object)](M_Tessa_Cards_CardRequestExtensions_SetContextData.htm) в
контекст цепочки расширений для заданного объекта-отправителя sender. Данные
существует в пределах цепочки расширений. Возвращает null, если данные не
найдены или были установлены как null.  
[TryGetConverterFormat(CardGetFileContentRequest)](M_Tessa_Cards_CardRequestExtensions_TryGetConverterFormat_1.htm)|
Возвращает формат, в который должно быть сконвертировано содержимое, или null,
если конвертация не требуется.  
[TryGetConverterFormat(IDictionary<String,
Object>)](M_Tessa_Cards_CardRequestExtensions_TryGetConverterFormat.htm)|
Возвращает формат, в который должно быть сконвертировано содержимое, или null,
если конвертация не требуется.  
[TryGetDigest](M_Tessa_Cards_CardRequestExtensions_TryGetDigest.htm)|
Возвращает Digest для сохранения в историю действий с карточкой или null, если
Digest не был установлен.  
[TryGetDigestEventName](M_Tessa_Cards_CardRequestExtensions_TryGetDigestEventName.htm)|
Возвращает имя события по расчёту Digest для сохранения в историю действий с
карточкой или null, если имя события не было установлено. Имена стандартных
событий указаны в константах
[CardDigestEventNames](T_Tessa_Cards_CardDigestEventNames.htm).  
[TryGetDisableExpandJsonFlag](M_Tessa_Cards_CardRequestExtensions_TryGetDisableExpandJsonFlag.htm)|
Возвращает флаг, указывающий на то, что при экспорте карточки не нужно
разворачивать JSON-поля карточки из строки в Dictionary<string, object>.  
[TryGetDisallowCaching](M_Tessa_Cards_CardRequestExtensions_TryGetDisallowCaching.htm)|
Возвращает признак того, что не следует выполнять кэширование результата.  
[TryGetFileMapping](M_Tessa_Cards_CardRequestExtensions_TryGetFileMapping.htm)|
Возвращает список объектов с маппингом для контента файлов
[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm) в ответе на
запрос на экспорт карточки, или null, если строки не были заданы.  
[TryGetFileSource](M_Tessa_Cards_CardRequestExtensions_TryGetFileSource.htm)|
Возвращает местоположение контента файла или null, если местоположение не было
установлено.  
[TryGetForbidFileStoreChanging](M_Tessa_Cards_CardRequestExtensions_TryGetForbidFileStoreChanging.htm)|
Возвращает признак того, что для файлов сохраняемой карточки запрещено
изменять местоположение контента при сохранении.  
[TryGetImportVersion](M_Tessa_Cards_CardRequestExtensions_TryGetImportVersion.htm)|
Возвращает оригинальную версию импортируемой карточки, которую требуется
восстановить.  
[TryGetInvalidateCacheNames(CardRequest)](M_Tessa_Cards_CardRequestExtensions_TryGetInvalidateCacheNames.htm)|
Возвращает имена сбрасываемых кэшей в запросе
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.  
[TryGetInvalidateCacheNames(ICardRequestExtensionContext)](M_Tessa_Cards_CardRequestExtensions_TryGetInvalidateCacheNames_1.htm)|
Возвращает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.  
[TryGetInvalidateCompletedCacheNames](M_Tessa_Cards_CardRequestExtensions_TryGetInvalidateCompletedCacheNames.htm)|
Возвращает имена сбрасываемых кэшей в контексте запроса
[InvalidateCache](F_Tessa_Cards_CardRequestTypes_InvalidateCache.htm) или
null, если имена не заданы, в этом случае инвалидация выполняется для всех
кэшей.  
[TryGetLoadData](M_Tessa_Cards_CardRequestExtensions_TryGetLoadData.htm)|
Возвращает признак того, что следует выполнить загрузку бинарных данных.  
[TryGetOriginalVersion](M_Tessa_Cards_CardRequestExtensions_TryGetOriginalVersion.htm)|
Возвращает оригинальную версию карточки, которая была очищена при экспорте.  
[TryGetPluginType](M_Tessa_Cards_CardRequestExtensions_TryGetPluginType.htm)|
Возвращает тип плагина, установленный при выполнении запроса к карточке из
плагина Chronos, или null, если запрос выполнен не из плагина или из
неизвестного плагина.  
[TryGetRepairSectionsFlag](M_Tessa_Cards_CardRequestExtensions_TryGetRepairSectionsFlag.htm)|
Возвращает флаг, который указывает на то, что нужно починить (добавить)
строковые секции карточки в случае, если они отсутствуют в БД.  
[TryGetRequestToCache](M_Tessa_Cards_CardRequestExtensions_TryGetRequestToCache.htm)|
Возвращает признак того, что запрос на получение карточки должен обращаться к
кэшу. Значение актуально для карточек-синглтонов.  
[TryGetRows](M_Tessa_Cards_CardRequestExtensions_TryGetRows.htm)|  Возвращает
строки коллекционной или древовидной секции, заданные в ответе на
универсальный запрос к карточке, или null, если строки не были заданы.  
[TryGetSectionRows](M_Tessa_Cards_CardRequestExtensions_TryGetSectionRows.htm)|
Возвращает пустые строки коллекционных и древовидных секций, заданные в ответе
на универсальный запрос к карточке, или null, если строки не были заданы.  
[TryGetStorageFilePaths](M_Tessa_Cards_CardRequestExtensions_TryGetStorageFilePaths.htm)|
Возвращает объекты с информацией о пути и имени файлов, которые должны быть
записаны в отдельные файлы, относительно структуры карточки  
[TryGetSuggestedFileName](M_Tessa_Cards_CardRequestExtensions_TryGetSuggestedFileName.htm)|
Возвращает предпочитаемое имя файла, которое используется для загрузки
предпросмотра или создания файла по шаблону, или null, если используется уже
известное имя файла (то, которое задано в шаблоне).  
[TryGetTemplateCard(CardNewRequest)](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateCard.htm)|
Возвращает карточку шаблона, заданную в запросе на создание структуры
карточки, или null, если карточка шаблона не была задана.  
[TryGetTemplateCard(CardRequest)](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateCard_1.htm)|
Возвращает карточку шаблона, заданную в универсальном запросе к карточке, или
null, если карточка шаблона не была задана.  
[TryGetTemplateCard(CardResponse)](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateCard_2.htm)|
Возвращает карточку шаблона, заданную ответ на универсальный запрос к
карточке, или null, если карточка шаблона не была задана.  
[TryGetTemplateCardID](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateCardID.htm)|
Возвращает идентификатор карточки шаблона, по которой требуется создать
карточку, или null, если идентификатор не был задан.  
[TryGetTemplateCreatedFromCard](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateCreatedFromCard.htm)|
Возвращает признак того, что карточка шаблона создаётся из другой карточки, а
не в результате создания по шаблону из экспортированной карточки шаблона.  
[TryGetTemplateWasRepaired](M_Tessa_Cards_CardRequestExtensions_TryGetTemplateWasRepaired.htm)|
Возвращает признак того, что структура карточки шаблона была исправлена после
изменения схемы данных.  
[TryGetTitle](M_Tessa_Cards_CardRequestExtensions_TryGetTitle.htm)|
Возвращает заголовок задания, который выводится вместо типа задания, или null,
если заголовок не задан и выводится тип задания.  
[TryGetTypedRequestAsync<TRequest>](M_Tessa_Cards_CardRequestExtensions_TryGetTypedRequestAsync__1.htm)|
Возвращает строготипизированный запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой запрос не задан.  
[TryGetTypedRequestStorage](M_Tessa_Cards_CardRequestExtensions_TryGetTypedRequestStorage.htm)|
Возвращает хранилище для строготипизированного запроса для универсальных
расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой запрос не задан.  
[TryGetTypedResponseAsync<TResponse>](M_Tessa_Cards_CardRequestExtensions_TryGetTypedResponseAsync__1.htm)|
Возвращает строготипизированный ответ на запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой ответ на запрос не задан.  
[TryGetTypedResponseStorage](M_Tessa_Cards_CardRequestExtensions_TryGetTypedResponseStorage.htm)|
Возвращает хранилище для строготипизированного ответа на запрос для
универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm),
или null, если такой запрос не задан.  
[TryGetWarningIfEntryNotFoundFlag](M_Tessa_Cards_CardRequestExtensions_TryGetWarningIfEntryNotFoundFlag.htm)|
Возвращает флаг, указывающий на то, что в случае отсутствия строковой секции в
БД, будет сгенерировано предупреждение, а не ошибка.  
[TryGetWipeDeletedFlag](M_Tessa_Cards_CardRequestExtensions_TryGetWipeDeletedFlag.htm)|
Возвращает флаг, который указывает на то, что нужно очищать удаленные в
корзину карточки, если они будут мешать импорту.  
## __Поля
[ImportVersionKey](F_Tessa_Cards_CardRequestExtensions_ImportVersionKey.htm)|  
---|---  
[KeepTaskDialogKey](F_Tessa_Cards_CardRequestExtensions_KeepTaskDialogKey.htm)|  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
