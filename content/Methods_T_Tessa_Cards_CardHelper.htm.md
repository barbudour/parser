# CardHelper - методы
##  __Методы
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
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
