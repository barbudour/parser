# CardHelper - класс
Хэлперы и константы для взаимодействия с карточками и их типами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardHelper
VB __Копировать
     Public NotInheritable Class CardHelper
C++ __Копировать
     public ref class CardHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardHelper
##  __Свойства
[DefaultDateTime](P_Tessa_Cards_CardHelper_DefaultDateTime.htm)|  Дата и
время, устанавливаемые по умолчанию в пакете карточки. Значение представлено в
формате UTC. Гарантируется, что время в UTC равно 00:00:00. Значение
отличается от [MinDateTime](P_Tessa_Cards_CardHelper_MinDateTime.htm) для
безопасного перевода между часовыми поясами, когда в структуре
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
устанавливается только время.  
---|---  
[DefaultLocalDateTime](P_Tessa_Cards_CardHelper_DefaultLocalDateTime.htm)|
Дата, соответствующая дате
[DefaultDateTime](P_Tessa_Cards_CardHelper_DefaultDateTime.htm), и время
00:00:00. Значение представление в локальном часовом поясе.  
[MaxDateTime](P_Tessa_Cards_CardHelper_MaxDateTime.htm)|  Максимальные дата и
время, допустимые в пакете карточки. Значение представлено в формате UTC.
Гарантируется, что время в UTC равно 00:00:00.  
[MaxDateTimeOffset](P_Tessa_Cards_CardHelper_MaxDateTimeOffset.htm)|
Максимальные дата и время со смещением, допустимые в пакете карточки.  
[MinDateTime](P_Tessa_Cards_CardHelper_MinDateTime.htm)|  Минимальные дата и
время, допустимые в пакете карточки. Значение представлено в формате UTC.
Гарантируется, что время в UTC равно 00:00:00.  
[MinDateTimeOffset](P_Tessa_Cards_CardHelper_MinDateTimeOffset.htm)|
Минимальные дата и время со смещением, допустимые в пакете карточки.  
## __Методы
[Compress](M_Tessa_Cards_CardHelper_Compress.htm)|  Выполняет упаковку пакета
карточки. Заданный декоратор становится непригоден к использованию.  
---|---  
[CompressFileVersions](M_Tessa_Cards_CardHelper_CompressFileVersions.htm)|
Выполняет упаковку запроса на получение информации по версиям файла. Заданный
декоратор становится непригоден к использованию.  
[CopyFilesAsync](M_Tessa_Cards_CardHelper_CopyFilesAsync.htm)|
Создаёт копии файлов карточки sourceCard в карточке targetCard. При этом не
выполняется расширений, но учитываются все те же особенности, что и при
создании карточек по шаблону. Подписи файла по умолчанию не переносятся, если
не указан параметр copySignatures.
Фактическая копия файла с контентом будет создана после сохранения карточки
targetCard. Метод может вызываться как на сервере, так и на клиенте (причём
сервер не будет вызван).
Метод возвращает результат копирования, который не равен null и содержит
ошибки, если копирование не было выполнено.
Т.к. в карточке targetCard могут быть добавлены файлы, то карточку
рекомендуется сохранять посредством
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm), чтобы содержимое
файлов было корректно скопировано.
При сохранении посредством
[ICardRepository](T_Tessa_Cards_ICardRepository.htm) файлы будут добавлены без
содержимого.  
[CreateDefaultFileType](M_Tessa_Cards_CardHelper_CreateDefaultFileType.htm)|
Создаёт тип карточки [CardType](T_Tessa_Cards_CardType.htm), описывающий
стандартный тип файла [FileTypeID](F_Tessa_Cards_CardHelper_FileTypeID.htm).
Рекомендуется использовать только в целях предпросмотра карточек.  
[CreateDeletedAfterBeginTransactionAsync](M_Tessa_Cards_CardHelper_CreateDeletedAfterBeginTransactionAsync.htm)|
Метод, создающий карточку в корзине. Обычно вызывается в
[AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm)
до того, как карточка будет удалена, но уже внутри транзакции. Вызывается как
в платформенной расширении на удаление в корзину, также может быть вызван для
удаления в корзину виртуальных карточек. Возвращает признак того, что
удалённая карточка была создана.  
[CreateDeletedAfterRequestAsync](M_Tessa_Cards_CardHelper_CreateDeletedAfterRequestAsync.htm)|
Метод, выполняемый после создания карточки в корзине
[CreateDeletedAfterBeginTransactionAsync(ICardDeleteExtensionContext,
ICardContentStrategy, ICardStoreStrategy, ICardRepository, ICardRepository,
ICardRepository, ICardRepository,
CancellationToken)](M_Tessa_Cards_CardHelper_CreateDeletedAfterBeginTransactionAsync.htm)
снаружи транзакции. Обычно вызывается в
[AfterBeginTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterBeginTransaction.htm),
после того, как карточка будет удалена, но уже внутри транзакции. Вызывается
как в платформенной расширении на удаление в корзину, также может быть вызван
для удаления в корзину виртуальных карточек.  
[CreateFromExportedCardAsync](M_Tessa_Cards_CardHelper_CreateFromExportedCardAsync.htm)|
Создаёт карточку по экспортированной карточке и информации из карточки-
источника, из которой выполнялся экспорт и которая используется для связи с
файлами.  
[CreateFromTemplateAsync](M_Tessa_Cards_CardHelper_CreateFromTemplateAsync.htm)|
Создаёт карточку по шаблону и возвращает её.  
[CreateSectionRows](M_Tessa_Cards_CardHelper_CreateSectionRows.htm)|  Создаёт
объект, содержащий коллекцию пустых строк коллекционных и древовидных секций,
упорядоченных по имени секции.  
[Decompress(Dictionary<String,
Object>)](M_Tessa_Cards_CardHelper_Decompress.htm)|  Выполняет распаковку
пакета карточки.  
[Decompress(IStorageObjectProvider)](M_Tessa_Cards_CardHelper_Decompress_1.htm)|
Выполняет распаковку пакета карточки.  
[DecompressFileVersions(Dictionary<String,
Object>)](M_Tessa_Cards_CardHelper_DecompressFileVersions.htm)|  Выполняет
распаковку запроса на получение информации по версиям файла.  
[DecompressFileVersions(IStorageObjectProvider)](M_Tessa_Cards_CardHelper_DecompressFileVersions_1.htm)|
Выполняет распаковку запроса на получение информации по версиям файла.  
[DeserializeJsonFieldsInSectionsAndFilesAsync](M_Tessa_Cards_CardHelper_DeserializeJsonFieldsInSectionsAndFilesAsync.htm)|  
[DeserializeJsonFieldsInSectionsAsync](M_Tessa_Cards_CardHelper_DeserializeJsonFieldsInSectionsAsync.htm)|  
[ExecuteTypeExtensionsAsync](M_Tessa_Cards_CardHelper_ExecuteTypeExtensionsAsync.htm)|
Выполняет расширения на типы карточек для заданного типа расширений type.  
[GetBlockClass](M_Tessa_Cards_CardHelper_GetBlockClass.htm)|  Возвращает имя
класса блока, используемое в типах карточек.  
[GetCardFileNameWithoutExtension](M_Tessa_Cards_CardHelper_GetCardFileNameWithoutExtension.htm)|
Возвращает корректное имя файла карточки без расширения по дайджесту карточки.
Может использоваться для определения имени файла для экспортируемой карточки.  
[GetCardFileTypes](M_Tessa_Cards_CardHelper_GetCardFileTypes.htm)|  Получение
набора типов файлов [IFileType](T_Tessa_Files_IFileType.htm) по типам карточек
[CardType](T_Tessa_Cards_CardType.htm), полученным из метаданных.  
[GetDisplayText](M_Tessa_Cards_CardHelper_GetDisplayText.htm)|  Возвращает
текст для отображения, в котором был заменён перевод строки.  
[GetFileCardTypesAsync](M_Tessa_Cards_CardHelper_GetFileCardTypesAsync.htm)|
Получение типов файлов, доступных из API карточек.  
[GetFormClass](M_Tessa_Cards_CardHelper_GetFormClass.htm)|  Возвращает имя
класса формы, используемое в типах карточек.  
[GetLink](M_Tessa_Cards_CardHelper_GetLink.htm)|  Возвращает ссылку на
открытие карточки в клиентском приложении с опциональным открытием файла в
карточке.  
[GetSubContentDirectoryProvider](M_Tessa_Cards_CardHelper_GetSubContentDirectoryProvider.htm)|
Получает провайдер поддиректории для карточки на основании провайдера для
файла самой карточки.  
[GetTaskState](M_Tessa_Cards_CardHelper_GetTaskState.htm)|  Возвращает строку
с кратким описанием по состоянию задания по его параметрам.  
[GetTaskStateDate](M_Tessa_Cards_CardHelper_GetTaskStateDate.htm)|  Возвращает
дату, актуальную для состояния задания. Состояние можно получить вызовом
метода [GetTaskState(String, String,
Nullable<Guid>)](M_Tessa_Cards_CardHelper_GetTaskState.htm).  
[GetWebFileLink](M_Tessa_Cards_CardHelper_GetWebFileLink.htm)|  
[GetWebLink](M_Tessa_Cards_CardHelper_GetWebLink.htm)|  Возвращает ссылку на
открытие карточки в web-клиенте или null, если ссылка webAddress является
равна null после нормализации.  
[GrantAllPermissions](M_Tessa_Cards_CardHelper_GrantAllPermissions.htm)|
Выдаёт все возможные разрешения для заданной карточки и её вложенных карточек.  
[HasFilesContentsToSave](M_Tessa_Cards_CardHelper_HasFilesContentsToSave.htm)|
Возвращает признак того, что в заданной карточке присутствует хотя бы один
файл, который был добавлен или содержимое которого было изменено.  
[IsSystemKey](M_Tessa_Cards_CardHelper_IsSystemKey.htm)|  Определяет, является
ли заданный ключ хранилища IDictionary<string, object> системным ключом.  
[IsUserKey](M_Tessa_Cards_CardHelper_IsUserKey.htm)|  Определяет, является ли
заданный ключ хранилища IDictionary<string, object> пользовательским ключом.  
[LimitDisplayValue](M_Tessa_Cards_CardHelper_LimitDisplayValue.htm)|
Ограничивает длину имени карточки для отображения пользователю или в ссылке на
карточку.  
[MergeSection](M_Tessa_Cards_CardHelper_MergeSection.htm)|  
[ParseMergeOptionsAsync](M_Tessa_Cards_CardHelper_ParseMergeOptionsAsync.htm)|
Загружает опции слияния из файла.  
[ProhibitAllPermissions](M_Tessa_Cards_CardHelper_ProhibitAllPermissions.htm)|
Явно запрещает все возможные разрешения для заданной карточки и её вложенных
карточек.  
[SetAllCardPermissions](M_Tessa_Cards_CardHelper_SetAllCardPermissions.htm)|
Устанавливает указанные разрешения для карточки, её файлов и заданий.  
[StoreAsync(CardStoreRequest, IFileContainer, ICardRepository,
ICardStreamServerRepository,
CancellationToken)](M_Tessa_Cards_CardHelper_StoreAsync_1.htm)|  Выполняет
сохранение карточки на сервере с возможным наличием файлов. Не выполняет
проверку на наличие изменений в контенте файлов методом
[EnsureAllContentModifiedAsync(IEnumerable<IFile>,
CancellationToken)](M_Tessa_Files_FileExtensions_EnsureAllContentModifiedAsync.htm).
Метод для внутреннего использования, рекомендуется использовать объект
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm) для сохранения карточки
с файлами, обратитесь к руководству разработчика за примерами.  
[StoreAsync(CardStoreRequest, IFileContainer, ICardRepository,
ICardStreamClientRepository, Func<Double, CancellationToken, ValueTask>,
Int32, CancellationToken)](M_Tessa_Cards_CardHelper_StoreAsync.htm)|
Выполняет асинхронное сохранение карточки на клиенте с возможным наличием
файлов. Не выполняет проверку на наличие изменений в контенте файлов. Метод
для внутреннего использования, рекомендуется использовать объект
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm) для сохранения карточки
с файлами, обратитесь к руководству разработчика за примерами.  
[TemplateFileIsMatchForSource(CardFile,
Guid)](M_Tessa_Cards_CardHelper_TemplateFileIsMatchForSource.htm)|  Возвращает
признак того, что заданный файл, расположенный в шаблоне, соответствует файлу
в карточке с заданным идентификатором. Идентификатор версии не проверяется.  
[TemplateFileIsMatchForSource(CardFile, Guid,
Guid)](M_Tessa_Cards_CardHelper_TemplateFileIsMatchForSource_1.htm)|
Возвращает признак того, что заданный файл, расположенный в шаблоне,
соответствует файлу в карточке с заданным идентификатором и идентификатором
версии.  
[TryGetCsvEncodingAsync](M_Tessa_Cards_CardHelper_TryGetCsvEncodingAsync.htm)|
Возвращает кодировку для формирования файлов csv  
[TryGetCsvSeparatorAsync](M_Tessa_Cards_CardHelper_TryGetCsvSeparatorAsync.htm)|
Возвращает разделитель для формирования файлов csv. В случае если символ не
задан или при конвертации символа произошла ошибка возвращает ';' в качестве
разделителя по умолчанию  
[TryGetLinkAsync](M_Tessa_Cards_CardHelper_TryGetLinkAsync.htm)|  Возвращает
ссылку на открытие карточки в desktop- или в web-клиенте в соответствии с
объектом сессии.  
[TryGetWebAddressAsync](M_Tessa_Cards_CardHelper_TryGetWebAddressAsync.htm)|
Возвращает базовый адрес веб-клиента или null, если адрес не удалось получить.  
[TryParseCardFileFormatFromExtension](M_Tessa_Cards_CardHelper_TryParseCardFileFormatFromExtension.htm)|
Определяет формат файла по расширению. Возвращает null, если определить формат
не удалось.  
[TryParseLink](M_Tessa_Cards_CardHelper_TryParseLink.htm)|  Выполняет попытку
прочитать параметры, полученные для открытия карточки по ссылке.  
## __Поля
[AccountUserSettingsTypeID](F_Tessa_Cards_CardHelper_AccountUserSettingsTypeID.htm)|
Card type identifier for "AccountUserSettings":
{48332157-4F6A-4CB1-ACE6-4B811C0E5364}.  
---|---  
[AccountUserSettingsTypeName](F_Tessa_Cards_CardHelper_AccountUserSettingsTypeName.htm)|
Card type name for "AccountUserSettings".  
[ActionHistoryRecordTypeID](F_Tessa_Cards_CardHelper_ActionHistoryRecordTypeID.htm)|
Card type identifier for "ActionHistoryRecord":
{ABC13918-AA63-45CA-A3F4-D1FD5673C248}.  
[ActionHistoryRecordTypeName](F_Tessa_Cards_CardHelper_ActionHistoryRecordTypeName.htm)|
Card type name for "ActionHistoryRecord".  
[AdSyncFlagKey](F_Tessa_Cards_CardHelper_AdSyncFlagKey.htm)|  Ключ, по
которому в [!:CardStoreRequest.Info] устанавливается признак того, что
карточка относится к синхронизации с AD / LDAP.  
[AdSyncForceCardRepoKey](F_Tessa_Cards_CardHelper_AdSyncForceCardRepoKey.htm)|
Ключ, по которому в [!:Card.Info] устанавливается признак того, что карточка
должна сохраняться через [CardRepository](T_Tessa_Cards_CardRepository.htm).  
[AdSyncTypeCaption](F_Tessa_Cards_CardHelper_AdSyncTypeCaption.htm)|
Отображаемое имя типа карточки для настроек синхронизации с Active Directory.  
[AdSyncTypeID](F_Tessa_Cards_CardHelper_AdSyncTypeID.htm)|  Идентификатор типа
карточки для настроек синхронизации с Active Directory.  
[AdSyncTypeName](F_Tessa_Cards_CardHelper_AdSyncTypeName.htm)|  Имя типа
карточки для настроек синхронизации с Active Directory.  
[AllowAllCardPermissionFlags](F_Tessa_Cards_CardHelper_AllowAllCardPermissionFlags.htm)|
Все разрешения, доступные для карточки.  
[AllowAllFilePermissionFlags](F_Tessa_Cards_CardHelper_AllowAllFilePermissionFlags.htm)|
Все разрешения, доступные для файла.  
[ApplicationAliasMaxLength](F_Tessa_Cards_CardHelper_ApplicationAliasMaxLength.htm)|
Максимальная длина алиаса приложения.  
[ApplicationTypeCaption](F_Tessa_Cards_CardHelper_ApplicationTypeCaption.htm)|
Отображаемое имя типа карточки для приложения.  
[ApplicationTypeID](F_Tessa_Cards_CardHelper_ApplicationTypeID.htm)|
Идентификатор типа карточки для приложения.  
[ApplicationTypeName](F_Tessa_Cards_CardHelper_ApplicationTypeName.htm)|  Имя
типа карточки для приложения.  
[AttachedCardKey](F_Tessa_Cards_CardHelper_AttachedCardKey.htm)|  Ключ, по
которому в [!:CardGetRequest.Info] кладется storage карточки.  
[BusinessProcessTemplateTypeID](F_Tessa_Cards_CardHelper_BusinessProcessTemplateTypeID.htm)|
Card type identifier for "BusinessProcessTemplate":
{D05799BD-35B6-43B4-97DD-B6D0E683EFF2}.  
[BusinessProcessTemplateTypeName](F_Tessa_Cards_CardHelper_BusinessProcessTemplateTypeName.htm)|
Card type name for "BusinessProcessTemplate".  
[CalendarTypeCaption](F_Tessa_Cards_CardHelper_CalendarTypeCaption.htm)|
Отображаемое имя типа карточки для настроек бизнес-календаря.  
[CalendarTypeID](F_Tessa_Cards_CardHelper_CalendarTypeID.htm)|  Идентификатор
типа карточки для настроек бизнес-календаря.  
[CalendarTypeName](F_Tessa_Cards_CardHelper_CalendarTypeName.htm)|  Имя типа
карточки для настроек бизнес-календаря.  
[CardDigestMaxLength](F_Tessa_Cards_CardHelper_CardDigestMaxLength.htm)|
Максимальная длина Digest для записи в историю действий с карточкой.  
[CardTypeCaptionMaxLength](F_Tessa_Cards_CardHelper_CardTypeCaptionMaxLength.htm)|
Максимальная длина строки с отображаемым в пользовательском интерфейсе именем
типа карточки.  
[CardTypeGroupMaxLength](F_Tessa_Cards_CardHelper_CardTypeGroupMaxLength.htm)|
Максимальная длина строки с отображаемым в пользовательском интерфейсе именем
группы для типа карточки.  
[CardTypeNameMaxLength](F_Tessa_Cards_CardHelper_CardTypeNameMaxLength.htm)|
Максимальная длина строки с именем типа карточки.  
[CardUserNameMaxLength](F_Tessa_Cards_CardHelper_CardUserNameMaxLength.htm)|
Максимальная длина строки с именем пользователя, создавшего или изменившего
карточку.  
[CardWasCopiedFromIDKey](F_Tessa_Cards_CardHelper_CardWasCopiedFromIDKey.htm)|
Ключ со значением [Guid](https://learn.microsoft.com/dotnet/api/system.guid) в
хеш-таблице Info в карточке [Card](T_Tessa_Cards_Card.htm), которая была
создана в результате копирования другой карточки с заданным идентификатором.
Ключ требуется для сохранения в историю действий и для работы расширений, но
он не используется в платформенных расширениях.  
[CardWasCreatedFromTemplateIDKey](F_Tessa_Cards_CardHelper_CardWasCreatedFromTemplateIDKey.htm)|
Ключ со значением [Guid](https://learn.microsoft.com/dotnet/api/system.guid) в
хеш-таблице Info в карточке [Card](T_Tessa_Cards_Card.htm), которая была
создана в результате копирования другой карточки с заданным идентификатором.
Ключ требуется для сохранения в историю действий и для работы расширений, но
он не используется в платформенных расширениях.  
[CompletionOptionCaptionMaxLength](F_Tessa_Cards_CardHelper_CompletionOptionCaptionMaxLength.htm)|
Максимальная длина строки с отображаемым в пользовательском интерфейсе именем
варианта завершения.  
[CompletionOptionTypeCaption](F_Tessa_Cards_CardHelper_CompletionOptionTypeCaption.htm)|
Отображаемое имя типа виртуальной карточки варианта завершения.  
[CompletionOptionTypeID](F_Tessa_Cards_CardHelper_CompletionOptionTypeID.htm)|
Идентификатор типа виртуальной карточки варианта завершения:
{F6B95639-234E-4800-A2F1-3CB20E0BCDA4}.  
[CompletionOptionTypeName](F_Tessa_Cards_CardHelper_CompletionOptionTypeName.htm)|
Имя типа виртуальной карточки варианта завершения "CompletionOption".  
[ConditionTypeTypeID](F_Tessa_Cards_CardHelper_ConditionTypeTypeID.htm)|  Card
type identifier for "ConditionType": {CA37649D-9585-4C83-8EF4-FDF91C4C42EE}.  
[ConditionTypeTypeName](F_Tessa_Cards_CardHelper_ConditionTypeTypeName.htm)|
Card type name for "ConditionType".  
[CopyingCardKey](F_Tessa_Cards_CardHelper_CopyingCardKey.htm)|  Ключ в хеш-
таблице Info в запросе на экспорт карточки
[CardGetRequest](T_Tessa_Cards_CardGetRequest.htm) или на создание по шаблону
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm). Содержит признак того, что
выполняется копирование карточки, а не обычный экспорт или создание по
шаблону. Для созданной карточки признак устанавливается в Card.Info, где его
можно увидеть в истории действий.  
[DefaultIDKey](F_Tessa_Cards_CardHelper_DefaultIDKey.htm)|  Ключ
идентификатора карточки по умолчанию.  
[DefaultMergeOptionsFileName](F_Tessa_Cards_CardHelper_DefaultMergeOptionsFileName.htm)|
Имя файла с опциями слияния по умолчанию, который располагается в подпапке с
именем файла импортируемой карточки.  
[DefaultRowIDKey](F_Tessa_Cards_CardHelper_DefaultRowIDKey.htm)|  Ключ
идентификатора строки по умолчанию.  
[DeletedCardIDKey](F_Tessa_Cards_CardHelper_DeletedCardIDKey.htm)|
Идентификатор удалённой карточки, которая создаётся при удалении карточки с
возможностью восстановления.  
[DeletedTypeCaption](F_Tessa_Cards_CardHelper_DeletedTypeCaption.htm)|
Отображаемое имя типа карточки для удалённой карточки.  
[DeletedTypeID](F_Tessa_Cards_CardHelper_DeletedTypeID.htm)|  Идентификатор
типа карточки для удалённой карточки.  
[DeletedTypeName](F_Tessa_Cards_CardHelper_DeletedTypeName.htm)|  Имя типа
карточки для удалённой карточки.  
[DialogFileFlagKey](F_Tessa_Cards_CardHelper_DialogFileFlagKey.htm)|  Ключ, по
которому в [!:CardFile.Info] устанавливается признак того, что карточка
относится к вложенно сохраняемой карточке диалога.  
[DisplayValueMaxLength](F_Tessa_Cards_CardHelper_DisplayValueMaxLength.htm)|
Максимальная длина имени карточки для отображения пользователю или в ссылке на
карточку.  
[DocLoadCaption](F_Tessa_Cards_CardHelper_DocLoadCaption.htm)|  Отображаемое
имя типа карточки для настроек модуля Потокового ввода документов.  
[DocLoadFlagKey](F_Tessa_Cards_CardHelper_DocLoadFlagKey.htm)|  Ключ, по
которому в [!:CardFile.Info] устанавливается признак того, что карточка
относится к модулю потокового сканирования.  
[DocLoadTypeID](F_Tessa_Cards_CardHelper_DocLoadTypeID.htm)|  Идентификатор
типа карточки для настроек модуля Потокового ввода документов.  
[DocLoadTypeName](F_Tessa_Cards_CardHelper_DocLoadTypeName.htm)|  Имя типа
карточки для настроек модуля Потокового ввода документов.  
[ErrorTypeID](F_Tessa_Cards_CardHelper_ErrorTypeID.htm)|  Card type identifier
for "Error": {FA81208D-2D83-4CB6-A83D-CBA7E3F483A7}.  
[ErrorTypeName](F_Tessa_Cards_CardHelper_ErrorTypeName.htm)|  Card type name
for "Error".  
[FileCategoryCaption](F_Tessa_Cards_CardHelper_FileCategoryCaption.htm)|
Отображаемое имя типа карточки для категории файла.  
[FileCategoryCaptionMaxLength](F_Tessa_Cards_CardHelper_FileCategoryCaptionMaxLength.htm)|
Максимальная длина строки с отображаемым именем категории файла.  
[FileCategoryID](F_Tessa_Cards_CardHelper_FileCategoryID.htm)|  Идентификатор
типа карточки для категории файла.  
[FileCategoryName](F_Tessa_Cards_CardHelper_FileCategoryName.htm)|  Имя типа
карточки для категории файла.  
[FileConverterCacheTypeCaption](F_Tessa_Cards_CardHelper_FileConverterCacheTypeCaption.htm)|
Отображаемое имя типа карточки для кэша конвертации файлов.  
[FileConverterCacheTypeID](F_Tessa_Cards_CardHelper_FileConverterCacheTypeID.htm)|
Идентификатор типа карточки для кэша конвертации файлов.  
[FileConverterCacheTypeName](F_Tessa_Cards_CardHelper_FileConverterCacheTypeName.htm)|
Имя типа карточки для кэша конвертации файлов.  
[FileNameMaxLength](F_Tessa_Cards_CardHelper_FileNameMaxLength.htm)|
Максимальная длина строки с именем файла.  
[FileSatelliteTypeID](F_Tessa_Cards_CardHelper_FileSatelliteTypeID.htm)|  Card
type identifier for "FileSatellite": {580CD334-6630-420E-ACD8-9524BE99E43E}.  
[FileSatelliteTypeName](F_Tessa_Cards_CardHelper_FileSatelliteTypeName.htm)|
Card type name for "FileSatellite".  
[FileTemplateTypeCaption](F_Tessa_Cards_CardHelper_FileTemplateTypeCaption.htm)|
Отображаемое имя типа карточки для шаблона файла.  
[FileTemplateTypeID](F_Tessa_Cards_CardHelper_FileTemplateTypeID.htm)|
Идентификатор типа карточки для шаблона файла.  
[FileTemplateTypeName](F_Tessa_Cards_CardHelper_FileTemplateTypeName.htm)|
Имя типа карточки для шаблона файла.  
[FileTypeCaption](F_Tessa_Cards_CardHelper_FileTypeCaption.htm)|  Отображаемое
имя типа карточки для стандартного файла, не имеющего дополнительных секций.  
[FileTypeID](F_Tessa_Cards_CardHelper_FileTypeID.htm)|  Идентификатор типа
карточки для стандартного файла, не имеющего дополнительных секций.  
[FileTypeName](F_Tessa_Cards_CardHelper_FileTypeName.htm)|  Имя типа карточки
для стандартного файла, не имеющего дополнительных секций.  
[FileVersionTagsMaxLength](F_Tessa_Cards_CardHelper_FileVersionTagsMaxLength.htm)|
Максимальная длина строки со списком тегов для версии файла.  
[FmUserSettingsTypeID](F_Tessa_Cards_CardHelper_FmUserSettingsTypeID.htm)|
Card type identifier for "FmUserSetttings":
{E337B575-FA44-4842-9E78-0222F0819529}.  
[FmUserSettingsTypeName](F_Tessa_Cards_CardHelper_FmUserSettingsTypeName.htm)|
Card type name for "FmUserSetttings".  
[FunctionRoleTypeCaption](F_Tessa_Cards_CardHelper_FunctionRoleTypeCaption.htm)|
Отображаемое имя типа виртуальной карточки функциональной роли.  
[FunctionRoleTypeID](F_Tessa_Cards_CardHelper_FunctionRoleTypeID.htm)|
Идентификатор типа виртуальной карточки функциональной роли:
{A830094D-6E03-4242-9C17-0D0A8F2FCB33}.  
[FunctionRoleTypeName](F_Tessa_Cards_CardHelper_FunctionRoleTypeName.htm)|
Имя типа виртуальной карточки функциональной роли "FunctionRole".  
[GeneralUserSettingsTypeID](F_Tessa_Cards_CardHelper_GeneralUserSettingsTypeID.htm)|
Card type identifier for "GeneralUserSettings":
{39DCE9D4-F429-4552-A268-5A9BF9C1BA53}.  
[GeneralUserSettingsTypeName](F_Tessa_Cards_CardHelper_GeneralUserSettingsTypeName.htm)|
Card type name for "GeneralUserSettings".  
[LicenseTypeCaption](F_Tessa_Cards_CardHelper_LicenseTypeCaption.htm)|
Отображаемое имя типа карточки для настроек лицензии.  
[LicenseTypeID](F_Tessa_Cards_CardHelper_LicenseTypeID.htm)|  Идентификатор
типа карточки для настроек лицензии.  
[LicenseTypeName](F_Tessa_Cards_CardHelper_LicenseTypeName.htm)|  Имя типа
карточки для настроек лицензии.  
[MainCardIDKey](F_Tessa_Cards_CardHelper_MainCardIDKey.htm)|  Ключ, по
которому в [!:CardNewRequest.Info] устанавливается идентификатор основной
карточки. Наличие такого идентификатора свидетельствует о том, что создаваемую
карточку следует интерпретировать как сателлит. Также используется при
сохранении карточки диалога для передачи идентификатора основной карточки.  
[NewCardBilletKey](F_Tessa_Cards_CardHelper_NewCardBilletKey.htm)|  Ключ, по
которому располагается заготовка карточки, обрабатываемая
[MergeWithBilletCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_MergeWithBilletCardNewExtension.htm).  
[NewCardBilletSignatureKey](F_Tessa_Cards_CardHelper_NewCardBilletSignatureKey.htm)|
Ключ, по которому располагается подпись заготовки карточки, обрабатываемая
[MergeWithBilletCardNewExtension](T_Tessa_Extensions_Platform_Server_Cards_MergeWithBilletCardNewExtension.htm).  
[NotificationSubscriptionsTypeID](F_Tessa_Cards_CardHelper_NotificationSubscriptionsTypeID.htm)|
Card type identifier for "NotificationSubscriptions":
{4D92F912-2907-4E3C-BCE5-7767A0F98BF8}.  
[NotificationSubscriptionsTypeName](F_Tessa_Cards_CardHelper_NotificationSubscriptionsTypeName.htm)|
Card type name for "NotificationSubscriptions".  
[NotificationTypeID](F_Tessa_Cards_CardHelper_NotificationTypeID.htm)|  Card
type identifier for "Notification": {D3087E3C-A2DA-4CC7-A92D-D5CF17E48D3F}.  
[NotificationTypeName](F_Tessa_Cards_CardHelper_NotificationTypeName.htm)|
Card type name for "Notification".  
[NotificationTypeTypeID](F_Tessa_Cards_CardHelper_NotificationTypeTypeID.htm)|
Card type identifier for "NotificationType":
{813234A7-3B29-4845-BE9D-B5BECE5F7C1C}.  
[NotificationTypeTypeName](F_Tessa_Cards_CardHelper_NotificationTypeTypeName.htm)|
Card type name for "NotificationType".  
[NotificationUserSettingsTypeID](F_Tessa_Cards_CardHelper_NotificationUserSettingsTypeID.htm)|
Card type identifier for "NotificationUserSettings":
{193C278D-7178-4EE3-A73B-438357D69D2A}.  
[NotificationUserSettingsTypeName](F_Tessa_Cards_CardHelper_NotificationUserSettingsTypeName.htm)|
Card type name for "NotificationUserSettings".  
[OpenCardLinkAction](F_Tessa_Cards_CardHelper_OpenCardLinkAction.htm)|
Название действия на открытие карточки по ссылке.  
[OperationTypeCaption](F_Tessa_Cards_CardHelper_OperationTypeCaption.htm)|
Отображаемое имя типа виртуальной карточки операции.  
[OperationTypeID](F_Tessa_Cards_CardHelper_OperationTypeID.htm)|
Идентификатор типа виртуальной карточки операции:
{F2517B14-035B-4451-B4A1-605BF7A764A4}.  
[OperationTypeName](F_Tessa_Cards_CardHelper_OperationTypeName.htm)|  Имя типа
виртуальной карточки операции "Operation".  
[PersonalizationUserSettingsTypeID](F_Tessa_Cards_CardHelper_PersonalizationUserSettingsTypeID.htm)|
Card type identifier for "PersonalizationUserSettings":
{3BD67BFF-6990-4026-AA7F-B789BA8A8744}.  
[PersonalizationUserSettingsTypeName](F_Tessa_Cards_CardHelper_PersonalizationUserSettingsTypeName.htm)|
Card type name for "PersonalizationUserSettings".  
[PlaceholderCurrentCardIDInfo](F_Tessa_Cards_CardHelper_PlaceholderCurrentCardIDInfo.htm)|
Имя объекта в Info, содержащего ID оригинальной карточки при генерации
шаблона.  
[PlaceholderExportInfo](F_Tessa_Cards_CardHelper_PlaceholderExportInfo.htm)|
Имя объекта в Info, содержащего сериализованный объект с произвольной
пользовательской информацией для замены плейсхолдеров.  
[PlaceholderUserInfoKey](F_Tessa_Cards_CardHelper_PlaceholderUserInfoKey.htm)|
Имя объекта в Info, содержащего сериализованный объект с произвольной
пользовательской информацией для замены плейсхолдеров.  
[PlaceholderViewContextKey](F_Tessa_Cards_CardHelper_PlaceholderViewContextKey.htm)|
Имя объекта в Info, содержащего сериализованный объект с информацией по
текущему представлению
[IViewPlaceholderContext](T_Tessa_Platform_Placeholders_IViewPlaceholderContext.htm).  
[PlainJsonSuffix](F_Tessa_Cards_CardHelper_PlainJsonSuffix.htm)|  
[PostponeCommentMaxLength](F_Tessa_Cards_CardHelper_PostponeCommentMaxLength.htm)|
Максимальная длина поля с комментарием по откладыванию задания.  
[ProhibitAllCardPermissionFlags](F_Tessa_Cards_CardHelper_ProhibitAllCardPermissionFlags.htm)|
Запрет всех разрешений, доступных для карточки.  
[ProhibitAllFilePermissionFlags](F_Tessa_Cards_CardHelper_ProhibitAllFilePermissionFlags.htm)|
Запрет всех разрешений, доступных для файла.  
[ReplacePlaceholdersVersionRowID](F_Tessa_Cards_CardHelper_ReplacePlaceholdersVersionRowID.htm)|
Идентификатор версии файла, для которой идет обработка замены плейсхолдеров
для файлового шаблона.  
[SequenceTypeCaption](F_Tessa_Cards_CardHelper_SequenceTypeCaption.htm)|
Отображаемое имя типа карточки для карточки последовательности.  
[SequenceTypeID](F_Tessa_Cards_CardHelper_SequenceTypeID.htm)|  Идентификатор
типа карточки для карточки последовательности.  
[SequenceTypeName](F_Tessa_Cards_CardHelper_SequenceTypeName.htm)|  Имя типа
карточки для карточки последовательности.  
[ServerInstanceTypeCaption](F_Tessa_Cards_CardHelper_ServerInstanceTypeCaption.htm)|
Отображаемое имя типа карточки для настроек сервера.  
[ServerInstanceTypeID](F_Tessa_Cards_CardHelper_ServerInstanceTypeID.htm)|
Идентификатор типа карточки для настроек сервера.  
[ServerInstanceTypeName](F_Tessa_Cards_CardHelper_ServerInstanceTypeName.htm)|
Имя типа карточки для настроек сервера.  
[ShowDialogTypeID](F_Tessa_Cards_CardHelper_ShowDialogTypeID.htm)|  Task type
identifier for "ShowDialog": {706E6173-F55D-4FE8-9CBE-AAEB2964BA80}.  
[ShowDialogTypeName](F_Tessa_Cards_CardHelper_ShowDialogTypeName.htm)|  Task
type name for "ShowDialog".  
[SignatureSettingsTypeCaption](F_Tessa_Cards_CardHelper_SignatureSettingsTypeCaption.htm)|
Отображаемое имя типа карточки для настроек цифровой подписи.  
[SignatureSettingsTypeID](F_Tessa_Cards_CardHelper_SignatureSettingsTypeID.htm)|
Идентификатор типа карточки для настроек цифровой подписи.  
[SignatureSettingsTypeName](F_Tessa_Cards_CardHelper_SignatureSettingsTypeName.htm)|
Имя типа карточки для настроек цифровой подписи.  
[SpecialFieldSuffixStart](F_Tessa_Cards_CardHelper_SpecialFieldSuffixStart.htm)|  
[SystemKeyPrefix](F_Tessa_Cards_CardHelper_SystemKeyPrefix.htm)|  Префикс
системных свойств, располагающихся в произвольном месте в хранилище объекта
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm). Такие
свойства не должны как-либо учитываться или изменяться пользовательским кодом.  
[SystemRestoreKey](F_Tessa_Cards_CardHelper_SystemRestoreKey.htm)|  Ключ для
логического значения с признаком необходимости восстановления карточки,
которое записывается в [Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm)
запроса на удаление удалённой карточки. Ключ является системным и его не
следует использовать для других целей.  
[TaskHistoryGroupCaptionMaxLength](F_Tessa_Cards_CardHelper_TaskHistoryGroupCaptionMaxLength.htm)|
Максимальная длина строки с именем группы истории заданий.  
[TaskHistoryKindCaptionMaxLength](F_Tessa_Cards_CardHelper_TaskHistoryKindCaptionMaxLength.htm)|
Максимальная длина строки с видом задания, к которому относится запись в
истории заданий.  
[TaskHistoryProcessKindMaxLength](F_Tessa_Cards_CardHelper_TaskHistoryProcessKindMaxLength.htm)|
Максимальная длина строки с типом бизнес-процесса, к которому относится запись
в истории заданий.  
[TaskHistoryProcessNameMaxLength](F_Tessa_Cards_CardHelper_TaskHistoryProcessNameMaxLength.htm)|
Максимальная длина строки с именем бизнес-процесса, к которому относится
запись в истории заданий.  
[TaskKindCaptionKey](F_Tessa_Cards_CardHelper_TaskKindCaptionKey.htm)|  Ключ,
по которому в [!:CardTask.Info] помещается информация об названии вида
задания.  
[TaskKindIDKey](F_Tessa_Cards_CardHelper_TaskKindIDKey.htm)|  Ключ, по
которому в [!:CardTask.Info] помещается информация об идентификаторе вида
задания.  
[TemplateFileTypeCaption](F_Tessa_Cards_CardHelper_TemplateFileTypeCaption.htm)|
Отображаемое имя типа карточки для файла шаблона.  
[TemplateFileTypeID](F_Tessa_Cards_CardHelper_TemplateFileTypeID.htm)|
Идентификатор типа карточки для файла шаблона.  
[TemplateFileTypeName](F_Tessa_Cards_CardHelper_TemplateFileTypeName.htm)|
Имя типа карточки для файла шаблона.  
[TemplateSourceCardIDKey](F_Tessa_Cards_CardHelper_TemplateSourceCardIDKey.htm)|
Ключ в хеш-таблице Info в запросе на создание карточки по шаблону
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm), который содержит
идентификатор карточки, по которой создаётся новая карточка. Это может быть
как идентификатор карточки шаблона, если карточка создаётся по шаблону, так и
идентификатор копируемой карточки, если выполняется копирование карточки
(через плитку "Копировать"). Если карточка копируется, то в Info будет признак
[CopyingCardKey](F_Tessa_Cards_CardHelper_CopyingCardKey.htm). Также ключ
может отсутствовать в Info, например, если карточка создаётся по шаблону из
экспортированной в файл карточки.  
[TemplateSourceCardTypeIDKey](F_Tessa_Cards_CardHelper_TemplateSourceCardTypeIDKey.htm)|
Ключ в хеш-таблице Info в запросе на создание карточки по шаблону
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm), который содержит
идентификатор типа карточки, по которой создаётся новая карточка. Это может
быть как идентификатор типа шаблона
[TemplateTypeID](F_Tessa_Cards_CardHelper_TemplateTypeID.htm), если карточка
создаётся по шаблону, так и идентификатор типа копируемой карточки, если
выполняется копирование карточки (через плитку "Копировать"). Если карточка
копируется, то в Info будет признак
[CopyingCardKey](F_Tessa_Cards_CardHelper_CopyingCardKey.htm). Также ключ
может отсутствовать в Info, например, если карточка создаётся по шаблону из
экспортированной в файл карточки.  
[TemplateTypeCaption](F_Tessa_Cards_CardHelper_TemplateTypeCaption.htm)|
Отображаемое имя типа карточки шаблона.  
[TemplateTypeID](F_Tessa_Cards_CardHelper_TemplateTypeID.htm)|  Идентификатор
типа карточки шаблона.  
[TemplateTypeName](F_Tessa_Cards_CardHelper_TemplateTypeName.htm)|  Имя типа
карточки шаблона.  
[TileUserSettingsTypeID](F_Tessa_Cards_CardHelper_TileUserSettingsTypeID.htm)|
Card type identifier for "TileUserSettings":
{D3E5A259-E7E6-49F2-A7DD-1FC7B051781B}.  
[TileUserSettingsTypeName](F_Tessa_Cards_CardHelper_TileUserSettingsTypeName.htm)|
Card type name for "TileUserSettings".  
[TimeZonesTypeID](F_Tessa_Cards_CardHelper_TimeZonesTypeID.htm)|
Идентификатор типа карточки для справочника временных зон:
{CC60E8C6-AF29-4AD5-A55D-3E6EE985CEB2}.  
[TimeZonesTypeName](F_Tessa_Cards_CardHelper_TimeZonesTypeName.htm)|  Имя типа
карточки для справочника временных зон.  
[TopicDescriptionMaxLength](F_Tessa_Cards_CardHelper_TopicDescriptionMaxLength.htm)|
Максимальная длина описания обсуждения.  
[TopicMessageMaxLength](F_Tessa_Cards_CardHelper_TopicMessageMaxLength.htm)|
Максимальная длина сообщений в обсуждених.  
[TopicTitleMaxLength](F_Tessa_Cards_CardHelper_TopicTitleMaxLength.htm)|
Максимальная длина заголовка обсуждения.  
[UnavailableTypesKey](F_Tessa_Cards_CardHelper_UnavailableTypesKey.htm)|  Ключ
со списком типов карточек, недоступных пользователю для создания.  
[UserKeyPrefix](F_Tessa_Cards_CardHelper_UserKeyPrefix.htm)|  Префикс
пользовательских свойств, располагающихся в произвольном месте в хранилище
объекта [CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm).  
[UserSettingsOnlyKey](F_Tessa_Cards_CardHelper_UserSettingsOnlyKey.htm)|
Ключ, по которому в [!:CardGetRequest.Info] и [!:CardStoreRequest.Info]
устанавливается признак того, что запрос на получение или сохранение карточки
сотрудника выполняется в рамках изменения настроек пользователя.  
[UserSettingsSystemTypeTypeID](F_Tessa_Cards_CardHelper_UserSettingsSystemTypeTypeID.htm)|
Card type identifier for "UserSettingsSystemType":
{7E6A9F59-0889-4B4D-8989-9F0C70C39F90}.  
[UserSettingsSystemTypeTypeName](F_Tessa_Cards_CardHelper_UserSettingsSystemTypeTypeName.htm)|
Card type name for "UserSettingsSystemType".  
[ViewTypeCaption](F_Tessa_Cards_CardHelper_ViewTypeCaption.htm)|  Отображаемое
имя типа карточки для представления.  
[ViewTypeID](F_Tessa_Cards_CardHelper_ViewTypeID.htm)|  Card type identifier
for "View": {635BBE7B-9C2E-4FDE-87C2-9DEEFAAD7981}.  
[ViewTypeName](F_Tessa_Cards_CardHelper_ViewTypeName.htm)|  Card type name for
"View".  
[WebApplicationTypeCaption](F_Tessa_Cards_CardHelper_WebApplicationTypeCaption.htm)|
Отображаемое имя типа карточки для приложения Web.  
[WebApplicationTypeID](F_Tessa_Cards_CardHelper_WebApplicationTypeID.htm)|
Идентификатор типа карточки для приложения Web.  
[WebApplicationTypeName](F_Tessa_Cards_CardHelper_WebApplicationTypeName.htm)|
Имя типа карточки для приложения Web.  
[WebClientUserSettingsTypeID](F_Tessa_Cards_CardHelper_WebClientUserSettingsTypeID.htm)|
Card type identifier for "WebClientUserSettings": {7104AC73-BF0A-4DBA-
BE9E-21F7148C8C82}.  
[WebClientUserSettingsTypeName](F_Tessa_Cards_CardHelper_WebClientUserSettingsTypeName.htm)|
Card type name for "WebClientUserSettings".  
[WorkplaceTypeCaption](F_Tessa_Cards_CardHelper_WorkplaceTypeCaption.htm)|
Отображаемое имя типа карточки для рабочего места.  
[WorkplaceTypeID](F_Tessa_Cards_CardHelper_WorkplaceTypeID.htm)|  Card type
identifier for "Workplace": {12FD0E19-D751-4D8E-959D-78C9763BBB38}.  
[WorkplaceTypeName](F_Tessa_Cards_CardHelper_WorkplaceTypeName.htm)|  Card
type name for "Workplace".  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
