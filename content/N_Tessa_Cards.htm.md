# Tessa.Cards - пространство имён
API управления карточками и типами карточек.
##  __Классы
[Card](T_Tessa_Cards_Card.htm)|  Содержит информацию о карточке.  
---|---  
[CardAutocompleteInfo](T_Tessa_Cards_CardAutocompleteInfo.htm)|  Информация по
выбранной ссылке в элементах управления
[AutoCompleteEntry](F_Tessa_Cards_CardControlTypes_AutoCompleteEntry.htm) и
[AutoCompleteTable](F_Tessa_Cards_CardControlTypes_AutoCompleteTable.htm),
которые определяют информацию для расширений, предоставляемую для открытия
карточек, в т.ч. виртуальных.  
[CardBlockSettings](T_Tessa_Cards_CardBlockSettings.htm)|  Настройки блоков
карточки.  
[CardCachingPermissionResolver](T_Tessa_Cards_CardCachingPermissionResolver.htm)|
Осуществляет поиск и кэширование прав доступа для полей, строк, файлов и
карточки.  
[CardContentStoreCompletedEventArgs](T_Tessa_Cards_CardContentStoreCompletedEventArgs.htm)|
Аргументы события
[ContentStoreCompleted](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_ContentStoreCompleted.htm),
вызываемого при завершении сохранения содержимого файлов.  
[CardControlAdditionalInfoRegistry](T_Tessa_Cards_CardControlAdditionalInfoRegistry.htm)|  
[CardControlSettings](T_Tessa_Cards_CardControlSettings.htm)|  Настройки
элементов управления карточки.  
[CardControlSourceInfo](T_Tessa_Cards_CardControlSourceInfo.htm)|  Объект с
описанием источника данных контрола  
[CardControlType](T_Tessa_Cards_CardControlType.htm)|  Тип элемента
управления, используемый в объектах метаинформации по типу карточки
[CardType](T_Tessa_Cards_CardType.htm) для связи с пользовательским
интерфейсом редактирования карточки.  
[CardControlTypeRegistry](T_Tessa_Cards_CardControlTypeRegistry.htm)|  Реестр
типов элементов управления
[CardControlType](T_Tessa_Cards_CardControlType.htm). Класс является
синглтоном.  
[CardControlTypes](T_Tessa_Cards_CardControlTypes.htm)|  Типы элементов
управления [CardControlType](T_Tessa_Cards_CardControlType.htm).  
[CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)|  Запрос на удаление
карточки посредством сервиса карточек.  
[CardDeleteResponse](T_Tessa_Cards_CardDeleteResponse.htm)|  Ответ на запрос
на удаление карточки посредством сервиса карточек. Содержит объект,
осуществляющий валидацию результата удаления.  
[CardDigestEventNames](T_Tessa_Cards_CardDigestEventNames.htm)|  Стандартные
имена событий, которые инициируют расчёт Digest через запрос
cardRepository.GetDigest(...). Имя события позволяет в расширении на Digest
определить, откуда именно был запрошен Digest.  
[CardEntryData](T_Tessa_Cards_CardEntryData.htm)|  Объект, позволяющий
обратиться напрямую от строковой секции карточки к значению поля и
автоматически устанавливающий системную информацию об изменённых полях.  
[CardErrorDetailWriter](T_Tessa_Cards_CardErrorDetailWriter.htm)|  Объект,
выполняющий запись объекта с деталями по возникшей ошибке в карточку ошибки
[ErrorTypeID](F_Tessa_Cards_CardHelper_ErrorTypeID.htm).  
[CardExtendedRepairManager](T_Tessa_Cards_CardExtendedRepairManager.htm)|
Объект, управляющий исправлением структуры карточки с выполнением расширений.  
[CardExtensions](T_Tessa_Cards_CardExtensions.htm)|  Методы-расширения для
пространства имён Tessa.Cards.  
[CardExternalSourceLogic](T_Tessa_Cards_CardExternalSourceLogic.htm)|  
[CardFakeRepairManager](T_Tessa_Cards_CardFakeRepairManager.htm)|  Объект, не
выполняющий исправление структуры карточки, например, вследствие изменения её
типа карточки.  
[CardFakeTaskHistoryManager](T_Tessa_Cards_CardFakeTaskHistoryManager.htm)|
Объект, реализующий интерфейс
[ICardTaskHistoryManager](T_Tessa_Cards_ICardTaskHistoryManager.htm), но не
выполняющий действий. Все методы класса возвращают null. Объект доступен на
сервере.  
[CardFieldChangedEventArgs](T_Tessa_Cards_CardFieldChangedEventArgs.htm)|
Информация о том, какое поле карточки было изменено.  
[CardFile](T_Tessa_Cards_CardFile.htm)|  Общая информация о файле,
прикреплённом к карточке.  
[CardFileContainer](T_Tessa_Cards_CardFileContainer.htm)|  Контейнер,
содержащий информацию по карточке и её файлам.  
[CardFileContentMapping](T_Tessa_Cards_CardFileContentMapping.htm)|
Информация по маппингу контента для сохраняемого файла. Используется для
сохранения виртуальных файлов, которые принадлежат другой карточке.  
[CardFileContentParameter](T_Tessa_Cards_CardFileContentParameter.htm)|
Параметр метода, описывающий обрабатываемый файл и его контент.  
[CardFileContentProvider](T_Tessa_Cards_CardFileContentProvider.htm)|  Объект,
предоставляющий контент сохраняемого файла.  
[CardFileContentResult](T_Tessa_Cards_CardFileContentResult.htm)|  Результат
обращения к методу для получения контента.  
[CardFileContentSource](T_Tessa_Cards_CardFileContentSource.htm)|  Информация
по источнику контента для файла. Используется, например, для того, чтобы файлы
карточки, созданной из шаблона, указывали на файлы шаблона.  
[CardFileManager](T_Tessa_Cards_CardFileManager.htm)|  Объект, который
управляет объектами контейнеров
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm), объединяющих
карточку с её файлами. Объект доступен на клиенте и на сервере.  
[CardFileRequestBase](T_Tessa_Cards_CardFileRequestBase.htm)|  Запрос на
получение информации по файлу, прикреплённому к карточке, от сервиса карточек.  
[CardFileSource](T_Tessa_Cards_CardFileSource.htm)|  Настройки по
местоположению контента файла.  
[CardFileSourceMapping](T_Tessa_Cards_CardFileSourceMapping.htm)|  Отображение
между источниками контента для файлов одной и той же карточки.  
[CardFileSourceOverride](T_Tessa_Cards_CardFileSourceOverride.htm)|  Настройки
по местоположению контента файла
[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm).  
[CardFileSourceOverrideProvider](T_Tessa_Cards_CardFileSourceOverrideProvider.htm)|
Объект, предоставляющий доступ к настройкам, переопределяющих местоположение
контента файлов.  
[CardFileSourceOverrideSettings](T_Tessa_Cards_CardFileSourceOverrideSettings.htm)|
Настройки, переопределяющие местоположение контента файла.  
[CardFileSourceSettings](T_Tessa_Cards_CardFileSourceSettings.htm)|
Потокобезопасный кэш настроек по всем местоположениям контентов.  
[CardFileStateEventArgs](T_Tessa_Cards_CardFileStateEventArgs.htm)|  Аргументы
события, происходящего при изменении свойства
[State](P_Tessa_Cards_CardFile_State.htm) в объекте с информацией о файле в
пакете карточки [CardFile](T_Tessa_Cards_CardFile.htm).  
[CardFileType](T_Tessa_Cards_CardFileType.htm)|  Тип файла в карточке.  
[CardFileVersion](T_Tessa_Cards_CardFileVersion.htm)|  Информация о версии
файла.  
[CardFormSettings](T_Tessa_Cards_CardFormSettings.htm)|  Настройки формы
карточки.  
[CardFunctionRoles](T_Tessa_Cards_CardFunctionRoles.htm)|  Идентификаторы
типовых функциональных ролей. Другую информацию по функциональным ролям можно
получить из [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm):
cardMetadata.Enumerations.FunctionRoles[id]  
[CardGetFileContentRequest](T_Tessa_Cards_CardGetFileContentRequest.htm)|
Запрос на получение контента версии файла, прикреплённого к карточке, от
сервиса карточек.  
[CardGetFileContentResponse](T_Tessa_Cards_CardGetFileContentResponse.htm)|
Ответ на запрос по получению контента версии файла, прикреплённого к карточке,
от сервиса карточек.  
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm)|
Запрос на получение информации по версиям файла, прикреплённого к карточке, от
сервиса карточек.  
[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm)|
Ответ на запрос по получению информации по версиям файла, прикреплённого к
карточке, от сервиса карточек.  
[CardGetFileVersionStorageCompressor](T_Tessa_Cards_CardGetFileVersionStorageCompressor.htm)|
Выполняет упаковку или распаковку списка версий в объекте
[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm).  
[CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)|  Запрос на получение
информации по карточке от сервиса карточек.  
[CardGetResponse](T_Tessa_Cards_CardGetResponse.htm)|  Ответ на запрос на
получение информации по карточке от сервиса карточек. Содержит информацию о
карточке и объект, осуществляющий валидацию.  
[CardGetRestrictionValues](T_Tessa_Cards_CardGetRestrictionValues.htm)|
Константы для флагов
[CardGetRestrictionFlags](T_Tessa_Cards_CardGetRestrictionFlags.htm),
ограничивающих загрузку информации для часто используемых сценариев.  
[CardGlobalReferencesContext](T_Tessa_Cards_CardGlobalReferencesContext.htm)|
Контекст-помощник для регистрации глобальных объектов, наследников от
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm).  
[CardHelper](T_Tessa_Cards_CardHelper.htm)|  Хэлперы и константы для
взаимодействия с карточками и их типами.  
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)|  Базовый
класс для объектов карточек, являющихся декораторами для хранилища, с
поддержкой дополнительной пользовательской информации.  
[CardLibrary](T_Tessa_Cards_CardLibrary.htm)|  Библиотека с карточками.  
[CardLibraryItem](T_Tessa_Cards_CardLibraryItem.htm)|  Запись в библиотеке с
карточками.  
[CardLocalizationLanguageProvider](T_Tessa_Cards_CardLocalizationLanguageProvider.htm)|
Объект, предоставляющий доступ к списку доступных языков по метаинформации
карточек.  
[CardLockingStrategy](T_Tessa_Cards_CardLockingStrategy.htm)|  Стратегия по
управлению блокировками на чтение и запись карточек. Некорректное
использование методов в этом интерфейсе может привести к "повисшим"
блокировкам, используйте с осторожностью.  
[CardManager](T_Tessa_Cards_CardManager.htm)|  Объект, управляющий операциями
с карточками.  
[CardMetadataSchemeInfoProvider](T_Tessa_Cards_CardMetadataSchemeInfoProvider.htm)|
Объект для получения таблиц из метаинформации
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm). Имеет собственный кэш
объектов. Не поддерживает метод
[CreateForCardType(CardType)](M_Tessa_Cards_CardMetadataSchemeInfoProvider_CreateForCardType.htm).  
[CardModelSettings](T_Tessa_Cards_CardModelSettings.htm)|  Настройки модели
представления карточки.  
[CardNewRequest](T_Tessa_Cards_CardNewRequest.htm)|  Запрос на создание
карточки определённого типа посредством сервиса карточек.  
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)|  Ответ на запрос на
получение информации по новой карточке от сервиса карточек. Содержит
информацию о карточке и объект, осуществляющий валидацию.  
[CardOnContentStoringEventArgs](T_Tessa_Cards_CardOnContentStoringEventArgs.htm)|
Аргументы события
[OnContentStoring](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_OnContentStoring.htm),
вызываемого перед сохранением содержимого каждого из файлов.  
[CardPermissionFlagValues](T_Tessa_Cards_CardPermissionFlagValues.htm)|
Константы для флагового перечисления
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm).  
[CardPermissionInfo](T_Tessa_Cards_CardPermissionInfo.htm)|  Содержит права
доступа на карточку и её секции.  
[CardPermissionResolver](T_Tessa_Cards_CardPermissionResolver.htm)|
Осуществляет поиск прав доступа для полей, строк, файлов и карточки.  
[CardPluginTypes](T_Tessa_Cards_CardPluginTypes.htm)|  Стандартные типы
плагинов, выполняющих запросы к сервису карточек с расширениями. Типы
позволяют отработать специфичное поведение при запуске из плагина.  
[CardRepairManager](T_Tessa_Cards_CardRepairManager.htm)|  Объект, управляющий
исправлением структуры карточки, например, вследствие изменения её типа
карточки.  
[CardRepairManagerNames](T_Tessa_Cards_CardRepairManagerNames.htm)|  Имена
объектов [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm), которые
регистрируются в Unity.  
[CardRepository](T_Tessa_Cards_CardRepository.htm)|  Репозиторий для
управления карточками.  
[CardRepositoryNames](T_Tessa_Cards_CardRepositoryNames.htm)|  Имена
репозиториев [ICardRepository](T_Tessa_Cards_ICardRepository.htm), которые
регистрируются в Unity.  
[CardRequest](T_Tessa_Cards_CardRequest.htm)|  Универсальный запрос на
выполнение действий через сервис карточек.  
[CardRequestBase](T_Tessa_Cards_CardRequestBase.htm)|  Запрос на выполнение
действий через сервис карточек по идентификатору карточки с предоставлением
дополнительной информации по идентификатору или имени её типа.  
[CardRequestExtensions](T_Tessa_Cards_CardRequestExtensions.htm)|  Расширения
для запросов и ответов на запросы к сервису карточек, контекста расширений
карточек, а также для дополнительных настроек UI в пакете карточки.  
[CardRequestTypes](T_Tessa_Cards_CardRequestTypes.htm)|  Типы стандартных
запросов к сервису карточек через метод [RequestAsync(CardRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_RequestAsync.htm).  
[CardResponse](T_Tessa_Cards_CardResponse.htm)|  Ответ на универсальный запрос
по выполнению действий через сервис карточек.  
[CardResponseBase](T_Tessa_Cards_CardResponseBase.htm)|  Базовый класс для
ответа на запрос к сервису карточек. Содержит объект, осуществляющий валидацию
результата запроса.  
[CardRow](T_Tessa_Cards_CardRow.htm)|  Строка коллекционной или древовидной
секции.  
[CardRowPermissionInfo](T_Tessa_Cards_CardRowPermissionInfo.htm)|  Содержит
права доступа на отдельные строки коллекционной или древовидной секции.  
[CardRowStateEventArgs](T_Tessa_Cards_CardRowStateEventArgs.htm)|  Аргументы
события, происходящего при изменении свойства
[State](P_Tessa_Cards_CardRow_State.htm) в объекте с информацией о строке
коллекционной или древовидной секции в пакете карточки
[CardRow](T_Tessa_Cards_CardRow.htm).  
[CardSchemeInfoProvider](T_Tessa_Cards_CardSchemeInfoProvider.htm)|  Объект
для получения таблиц из основной схемы и виртуальной схемы карточки. Имеет
собственный кэш объектов.  
[CardSchemeInfoProviderAdapter](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)|
Адаптер объектов
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm) для
использования в качестве [ISchemeService](T_Tessa_Scheme_ISchemeService.htm).
Имеет логику получения таблиц, для остальных методов делегирует получение
объектов для указанного объекта
[SchemeDatabase](T_Tessa_Scheme_SchemeDatabase.htm), а для прочих действий
возвращает валидные значения по умолчанию.
Посредством объекта невозможность изменить схему данных.  
[CardSchemeInfoProviderProxy](T_Tessa_Cards_CardSchemeInfoProviderProxy.htm)|
Объект для получения таблиц из
[ISchemeService](T_Tessa_Scheme_ISchemeService.htm). Является "тонкой"
обёрткой без использования кэширования. Не поддерживает метод
[CreateForCardType(CardType)](M_Tessa_Cards_CardSchemeInfoProviderProxy_CreateForCardType.htm).  
[CardSchemeSerializableObject](T_Tessa_Cards_CardSchemeSerializableObject.htm)|
Базовый объект для типа карточки или метаинформации, который может быть
сериализован в бинарную форму или в XML, а также связан со схемой.  
[CardSection](T_Tessa_Cards_CardSection.htm)|  Содержит данные строковой,
коллекционной или древовидной секции карточки.  
[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)|
Содержит права доступа на строковую секцию карточки и на её поля.  
[CardSerializableContext](T_Tessa_Cards_CardSerializableContext.htm)|
Контекст сериализации и десериализации объекта
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm).  
[CardSerializableEntry](T_Tessa_Cards_CardSerializableEntry.htm)|  Базовый
объект для типа карточки или метаинформации, реализующий интерфейс
[ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm), который
может быть сериализован в бинарную форму или в XML.  
[CardSerializableEntryCollection<T>](T_Tessa_Cards_CardSerializableEntryCollection_1.htm)|
Коллекция, содержащая сериализуемые в бинарную форму и в XML объекты, для
которых определён способ доступа по имени и по идентификатору.  
[CardSerializableEntryWithCaption](T_Tessa_Cards_CardSerializableEntryWithCaption.htm)|
Базовый объект для типа карточки или метаинформации, реализующий интерфейс
[ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm), который
может быть сериализован в бинарную форму или в XML.  
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)|  Базовый
объект для типа карточки или метаинформации, который может быть сериализован в
бинарную форму или в XML.  
[CardSerializableObjectContext](T_Tessa_Cards_CardSerializableObjectContext.htm)|  
[CardServerPermissionsProvider](T_Tessa_Cards_CardServerPermissionsProvider.htm)|
Объект, не предоставляющий прав доступа, но реализующий все методы интерфейса
[ICardServerPermissionsProvider](T_Tessa_Cards_ICardServerPermissionsProvider.htm).
Зарегистрирован по умолчанию, если расширения типового решения отсутствуют.
Наследники объекта могут переопределять методы и добавлять поведения.  
[CardService](T_Tessa_Cards_CardService.htm)|  Сервис для управления
карточками.  
[CardServiceClient](T_Tessa_Cards_CardServiceClient.htm)|  Сервис для
управления карточками, доступный на клиенте.  
[CardServiceNames](T_Tessa_Cards_CardServiceNames.htm)|  Дополнительные имена
сервиса [ICardService](T_Tessa_Cards_ICardService.htm), которые регистрируются
в Unity.  
[CardSignatureHelper](T_Tessa_Cards_CardSignatureHelper.htm)|  Хэлперы и
константы для взаимодействия с подписями файлов, расположенных в карточке.  
[CardStateEventArgs<TState>](T_Tessa_Cards_CardStateEventArgs_1.htm)|  Базовый
класс для аргументов события, происходящего при изменении состояние объекта в
пакете карточки.  
[CardStorageCompressor](T_Tessa_Cards_CardStorageCompressor.htm)|  Выполняет
упаковку или распаковку пакета карточки.  
[CardStorageObject](T_Tessa_Cards_CardStorageObject.htm)|  Базовый класс для
объектов карточек, являющихся декораторами для хранилища.  
[CardStoreAsyncResponse](T_Tessa_Cards_CardStoreAsyncResponse.htm)|  Объект,
предоставляющий доступ к результату асинхронной операции по сохранению
карточки с файлами.  
[CardStoreOperationToken](T_Tessa_Cards_CardStoreOperationToken.htm)|  Объект,
предоставляющий доступ к асинхронной операции по сохранению карточки с файлами
и к её результату.  
[CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)|  Запрос на сохранение
информации по карточке посредством сервиса карточек. Содержит только
изменённую информацию о карточке.  
[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)|  Ответ на запрос на
сохранение информации по карточке посредством сервиса карточек. Содержит
объект, осуществляющий валидацию результата сохранения.  
[CardStreamClientRepository](T_Tessa_Cards_CardStreamClientRepository.htm)|
Репозиторий для потокового управления карточками на клиенте.  
[CardStreamServerRepository](T_Tessa_Cards_CardStreamServerRepository.htm)|
Репозиторий для потокового управления карточками на сервере.  
[CardsWebProxy](T_Tessa_Cards_CardsWebProxy.htm)|  Прокси для обращения к веб-
сервису [ICardService](T_Tessa_Cards_ICardService.htm).  
[CardTableData](T_Tessa_Cards_CardTableData.htm)|  Объект, позволяющий
обратиться напрямую от коллекционной или древовидной секции карточки к
значению поля строки с заданным номером и автоматически устанавливающий
системную информацию об изменённых полях и строках.  
[CardTask](T_Tessa_Cards_CardTask.htm)|  Общая информация о задании, которое
выдано на карточку.  
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)|
Параметры этапа/действия "Диалог".  
[CardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_CardTaskCompletionOptionSettingsBuilder.htm)|
Предоставляет билдер объектов типа
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm).  
[CardTaskDialogActionResult](T_Tessa_Cards_CardTaskDialogActionResult.htm)|
Информация о результате завершении диалога.  
[CardTaskDialogButtonInfo](T_Tessa_Cards_CardTaskDialogButtonInfo.htm)|
Информация о кнопке диалога.  
[CardTaskDialogHelper](T_Tessa_Cards_CardTaskDialogHelper.htm)|  Содержит
вспомогательные методы для работы с диалогами.  
[CardTaskHistoryGroup](T_Tessa_Cards_CardTaskHistoryGroup.htm)|  Информация о
группе завершённых заданий, которые были выданы на карточку.  
[CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm)|  Информация о
завершённом задании, которое было выдано на карточку.  
[CardTaskHistoryManager](T_Tessa_Cards_CardTaskHistoryManager.htm)|  Объект,
управляющий созданием групп в истории заданий на основании типов групп,
определяемых по справочнику. Объект доступен на сервере.  
[CardType](T_Tessa_Cards_CardType.htm)|  Объект, описывающий тип карточки.  
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm)|  Блок типа карточки,
содержащий отображаемые единым образом контролы для полей и секций карточки.  
[CardTypeClientRepository](T_Tessa_Cards_CardTypeClientRepository.htm)|
Репозиторий для управления типами карточек на клиенте.  
[CardTypeCollection](T_Tessa_Cards_CardTypeCollection.htm)|  Коллекция,
содержащая объекты [CardType](T_Tessa_Cards_CardType.htm).  
[CardTypeColumn](T_Tessa_Cards_CardTypeColumn.htm)|  Объект, описывающий
колонку коллекционной или древовидной секции карточки
[CardTypeTableControl](T_Tessa_Cards_CardTypeTableControl.htm).  
[CardTypeCompletionOption](T_Tessa_Cards_CardTypeCompletionOption.htm)|
Вариант завершения типа карточки задания.  
[CardTypeContent](T_Tessa_Cards_CardTypeContent.htm)|  Базовый объект для
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm) и
[CardTypeColumn](T_Tessa_Cards_CardTypeColumn.htm).  
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)|  Базовый объект, который
может включаться в состав блока типа карточки
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm).  
[CardTypeCustomControl](T_Tessa_Cards_CardTypeCustomControl.htm)|  Объект,
описывающий элемент управления на карточке, особым образом привязанный к
данным карточки или не привязан вообще.  
[CardTypeEntryControl](T_Tessa_Cards_CardTypeEntryControl.htm)|  Объект,
описывающий расположение и свойства элемента управления для привязки к полям
строковой секции карточки.  
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)|  Информация о
расширении, используемом в типе карточки.  
[CardTypeExtensionSettings](T_Tessa_Cards_CardTypeExtensionSettings.htm)|
Настройки стандартных расширений для типов карточек.  
[CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm)|  Тип
расширения для типа карточки, используемый в объектах метаинформации по типу
карточки [CardType](T_Tessa_Cards_CardType.htm) для связи с пользовательским
интерфейсом редактирования карточки и с выполнением расширений на типы
карточек.  
[CardTypeExtensionTypeRegistry](T_Tessa_Cards_CardTypeExtensionTypeRegistry.htm)|
Реестр типов расширений
[CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm). Класс
является синглтоном.  
[CardTypeExtensionTypes](T_Tessa_Cards_CardTypeExtensionTypes.htm)|  Типы
расширений на типы карточек
[CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm).  
[CardTypeForm](T_Tessa_Cards_CardTypeForm.htm)|  Объект, описывающий базовую
информацию о форме карточки. Тип карточки
[CardType](T_Tessa_Cards_CardType.htm) \- это частный случай формы.  
[CardTypeInfoResolver](T_Tessa_Cards_CardTypeInfoResolver.htm)|  Объект,
получающий информацию по типу карточки. Реализация получает информацию из
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm).  
[CardTypeNamedForm](T_Tessa_Cards_CardTypeNamedForm.htm)|  Именованный объект,
описывающий пользовательский интерфейс для редактирования карточки.  
[CardTypeParamControl](T_Tessa_Cards_CardTypeParamControl.htm)|  Объект,
описывающий контрол с возможностью привязки в качестве значения кастомного
параметра  
[CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm)|  Объект,
описывающий тип карточки в форме, пригодной для хранения в базе данных.  
[CardTypeSchemeItem](T_Tessa_Cards_CardTypeSchemeItem.htm)|  Метаданные
секции, которая входит в состав типа карточки.  
[CardTypeServerRepository](T_Tessa_Cards_CardTypeServerRepository.htm)|
Репозиторий для управления типами карточек.  
[CardTypeService](T_Tessa_Cards_CardTypeService.htm)|  Сервис для управления
типами карточек.  
[CardTypeServiceClient](T_Tessa_Cards_CardTypeServiceClient.htm)|  Сервис для
управления типами карточек, доступный на клиенте.  
[CardTypesWebProxy](T_Tessa_Cards_CardTypesWebProxy.htm)|  Прокси для
обращения к веб-сервису
[ICardTypeService](T_Tessa_Cards_ICardTypeService.htm).  
[CardTypeTabControl](T_Tessa_Cards_CardTypeTabControl.htm)|  Объект,
описывающий расположение и свойства элемента управления для вывода списка форм
[CardTypeTabControlForm](T_Tessa_Cards_CardTypeTabControlForm.htm) во
вкладках.  
[CardTypeTabControlForm](T_Tessa_Cards_CardTypeTabControlForm.htm)|  Объект,
описывающий пользовательский интерфейс для вкладки карточки, который
используется в элементе управления
[CardTypeTabControl](T_Tessa_Cards_CardTypeTabControl.htm).  
[CardTypeTabForm](T_Tessa_Cards_CardTypeTabForm.htm)|  Объект, описывающий
базовую информацию о форме карточки, которая выводится во вкладке. Тип
карточки [CardType](T_Tessa_Cards_CardType.htm) \- это частный случай формы.  
[CardTypeTableControl](T_Tessa_Cards_CardTypeTableControl.htm)|  Объект,
описывающий расположение и свойства элемента управления для привязки к
колонкам коллекционной или древовидной секции карточки.  
[CardTypeTableForm](T_Tessa_Cards_CardTypeTableForm.htm)|  Объект, описывающий
пользовательский интерфейс для редактирования строки коллекционной или
древовидной секции.  
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)|  Информация о
валидаторе, используемом в типе карточки.  
[CardTypeValueComparer](T_Tessa_Cards_CardTypeValueComparer.htm)|  Сравнивает
типы карточек по всем свойствам.  
[CardTypeVisitor](T_Tessa_Cards_CardTypeVisitor.htm)|  Базовый класс для
объектов, выполняющих посещение объектов типа карточки.  
[CardValidationHelper](T_Tessa_Cards_CardValidationHelper.htm)|
Вспомогательные методы валидации карточек.  
[CardValidationKeys](T_Tessa_Cards_CardValidationKeys.htm)|  Ключи валидации,
используемые в API карточек.  
[CardValidatorType](T_Tessa_Cards_CardValidatorType.htm)|  Тип валидатора,
используемый в объектах метаинформации по типу карточки
[CardType](T_Tessa_Cards_CardType.htm) для связи с пользовательским
интерфейсом редактирования карточки и с валидацией карточки.  
[CardValidatorTypeRegistry](T_Tessa_Cards_CardValidatorTypeRegistry.htm)|
Реестр типов валидаторов
[CardValidatorType](T_Tessa_Cards_CardValidatorType.htm). Класс является
синглтоном.  
[CardValidatorTypes](T_Tessa_Cards_CardValidatorTypes.htm)|  Типы валидаторов
[CardValidatorType](T_Tessa_Cards_CardValidatorType.htm).  
[CardValueResponseBase](T_Tessa_Cards_CardValueResponseBase.htm)|  Базовый
объект для ответа на запрос на получение информации по карточке от сервиса
карточек. Содержит информацию о карточке и объект, осуществляющий валидацию.  
[CardWithoutLockingStrategy](T_Tessa_Cards_CardWithoutLockingStrategy.htm)|
Стратегия по управлению блокировками на чтение и запись карточек, которая не
выполняет взятие блокировок. Некорректное использование методов в этом
интерфейсе может привести к "повисшим" блокировкам, используйте с
осторожностью.  
[FileSourceForCard](T_Tessa_Cards_FileSourceForCard.htm)|  Источник файлов,
обеспечивающий взаимодействие файлов с подсистемой карточек.  
[FileSourceForCardContext](T_Tessa_Cards_FileSourceForCardContext.htm)|
Контекст использования источника файлов
[FileSourceForCard](T_Tessa_Cards_FileSourceForCard.htm).  
[ParsedCard](T_Tessa_Cards_ParsedCard.htm)|  
[TypeExtensionContext](T_Tessa_Cards_TypeExtensionContext.htm)|  Контекст
выполнения расширения на тип карточки
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm).  
[ViewMapColumnTypeExtension](T_Tessa_Cards_ViewMapColumnTypeExtension.htm)|  
## __Структуры
[CardFileSourceType](T_Tessa_Cards_CardFileSourceType.htm)|  Местоположение
контента файла.  
---|---  
## __Интерфейсы
[ICardCachedMetadata](T_Tessa_Cards_ICardCachedMetadata.htm)|  Содержит кэш
метаинформации, которая необходима для использования типов карточек совместно
с пакетом карточек.  
---|---  
[ICardControlAdditionalInfoRegistry](T_Tessa_Cards_ICardControlAdditionalInfoRegistry.htm)|
Реестр дополнительной информации о контролах
[CardControlType](T_Tessa_Cards_CardControlType.htm)  
[ICardControlTypeRegistry](T_Tessa_Cards_ICardControlTypeRegistry.htm)|
Реестр элементов управления
[CardControlType](T_Tessa_Cards_CardControlType.htm).  
[ICardExternalSourceLogic](T_Tessa_Cards_ICardExternalSourceLogic.htm)|
Сущность отвечает за логику чтения и записи карточек с учетом прикрепленных
файлов и внешнего storage-контента.  
[ICardFieldContainer](T_Tessa_Cards_ICardFieldContainer.htm)|  Объект,
являющийся контейнером для полей карточки.  
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm)|  Контейнер,
содержащий информацию по карточке и её файлам.  
[ICardFileContentProvider](T_Tessa_Cards_ICardFileContentProvider.htm)|
Объект, предоставляющий контент сохраняемого файла.  
[ICardFileContentResult](T_Tessa_Cards_ICardFileContentResult.htm)|  Результат
обращения к методу для получения контента.  
[ICardFileContentSource](T_Tessa_Cards_ICardFileContentSource.htm)|
Информация по источнику контента для файла.  
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm)|  Объект, который
управляет объектами контейнеров
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm), объединяющих
карточку с её файлами. Объект доступен на клиенте и на сервере.  
[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm)|  Настройки по
местоположению контента файла.  
[ICardFileSourceMapping](T_Tessa_Cards_ICardFileSourceMapping.htm)|
Отображение между источниками контента для файлов одной и той же карточки.  
[ICardFileSourceOverride](T_Tessa_Cards_ICardFileSourceOverride.htm)|
Настройки по местоположению контента файла
[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm).  
[ICardFileSourceOverrideProvider](T_Tessa_Cards_ICardFileSourceOverrideProvider.htm)|
Объект, предоставляющий доступ к настройкам, переопределяющих местоположение
контента файлов.  
[ICardFileSourceOverrideSettings](T_Tessa_Cards_ICardFileSourceOverrideSettings.htm)|
Настройки, переопределяющие местоположение контента файла.  
[ICardFileSourceSettings](T_Tessa_Cards_ICardFileSourceSettings.htm)|
Потокобезопасный кэш настроек по всем местоположениям файлов.  
[ICardHierarchyOrderable](T_Tessa_Cards_ICardHierarchyOrderable.htm)|  Объект
в карточке, поддерживающий иерархическое упорядочивание.  
[ICardLockingStrategy](T_Tessa_Cards_ICardLockingStrategy.htm)|  Стратегия по
управлению блокировками на чтение и запись карточек. Некорректное
использование методов в этом интерфейсе может привести к "повисшим"
блокировкам, используйте с осторожностью.  
[ICardManager](T_Tessa_Cards_ICardManager.htm)|  Объект, управляющий
операциями с карточками.  
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)|  Содержит метаинформацию,
необходимую для использования типов карточек совместно с пакетом карточек.  
[ICardMetadataOrderable](T_Tessa_Cards_ICardMetadataOrderable.htm)|  Элемент
типа карточки или метаинформации по карточкам, поддерживающий явное указание
порядка, в т.ч. порядка отображения в интерфейсе карточек, если элемент может
быть отображён в интерфейсе.  
[ICardModelSettings](T_Tessa_Cards_ICardModelSettings.htm)|  Настройки модели
представления карточки.  
[ICardOrderable](T_Tessa_Cards_ICardOrderable.htm)|  Объект в карточке,
поддерживающий линейное упорядочивание по номеру.  
[ICardPermissionResolver](T_Tessa_Cards_ICardPermissionResolver.htm)|
Осуществляет поиск прав доступа для полей, строк, файлов и карточки.  
[ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)|  Объект,
управляющий исправлением структуры карточки, например, вследствие изменения её
типа карточки.  
[ICardRepository](T_Tessa_Cards_ICardRepository.htm)|  Репозиторий для
управления карточками.  
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)|  Объект
для получения таблиц из основной схемы и виртуальной схемы карточки.  
[ICardSerializableContext](T_Tessa_Cards_ICardSerializableContext.htm)|
Контекст сериализации и десериализации объекта
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm).  
[ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm)|
Именованный объект с идентификатором, описывающий тип карточки.  
[ICardSerializableObjectContext](T_Tessa_Cards_ICardSerializableObjectContext.htm)|
Интерфейс для контекста сериализации/десериализации метаинформации со ссылками
на глобальные объекты [CardTypeForm](T_Tessa_Cards_CardTypeForm.htm),
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm),
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm),
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm),
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm).  
[ICardServerPermissionsProvider](T_Tessa_Cards_ICardServerPermissionsProvider.htm)|
Объект, предоставляющий права доступа в соответствии с активной системой прав.
Например, для типового решения предоставляет токен KrToken с полным набором
прав.  
[ICardService](T_Tessa_Cards_ICardService.htm)|  Сервис для управления
карточками.  
[ICardStoreAsyncResponse](T_Tessa_Cards_ICardStoreAsyncResponse.htm)|  Объект,
предоставляющий доступ к результату асинхронной операции по сохранению
карточки с файлами.  
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)|
Репозиторий для потокового управления карточками на клиенте. Репозиторий
доступен также на сервере в вариантах без расширений.  
[ICardStreamServerRepository](T_Tessa_Cards_ICardStreamServerRepository.htm)|
Репозиторий для потокового управления карточками на сервере.  
[ICardTaskCompletionOptionSettingsBuilder](T_Tessa_Cards_ICardTaskCompletionOptionSettingsBuilder.htm)|
Описывает билдер объектов типа
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)  
[ICardTaskHistoryManager](T_Tessa_Cards_ICardTaskHistoryManager.htm)|  Объект,
управляющий созданием групп в истории заданий на основании типов групп,
определяемых по справочнику. Объект доступен на сервере.  
[ICardTypeClientRepository](T_Tessa_Cards_ICardTypeClientRepository.htm)|
Репозиторий для управления типами карточек на клиенте.  
[ICardTypeExtensionTypeRegistry](T_Tessa_Cards_ICardTypeExtensionTypeRegistry.htm)|
Реестр типов расширений
[CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm).  
[ICardTypeServerRepository](T_Tessa_Cards_ICardTypeServerRepository.htm)|
Репозиторий для управления типами карточек на сервере.  
[ICardTypeService](T_Tessa_Cards_ICardTypeService.htm)|  Сервис для управления
типами карточек.  
[ICardTypeVisitor](T_Tessa_Cards_ICardTypeVisitor.htm)|  Выполняет посещение
объектов типа карточки.  
[ICardValidatorTypeRegistry](T_Tessa_Cards_ICardValidatorTypeRegistry.htm)|
Реестр валидаторов [CardValidatorType](T_Tessa_Cards_CardValidatorType.htm).  
[ITypeExtensionContext](T_Tessa_Cards_ITypeExtensionContext.htm)|  Контекст
выполнения расширения на тип карточки
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm).  
## __Делегаты
[CardControlSourceInfoDelegate](T_Tessa_Cards_CardControlSourceInfoDelegate.htm)|  
---|---  
[CreateFileSourceForCardFuncAsync](T_Tessa_Cards_CreateFileSourceForCardFuncAsync.htm)|
Создаёт источник файлов для заданной карточки.  
[FileSourceForCardContextExecutorAsync](T_Tessa_Cards_FileSourceForCardContextExecutorAsync.htm)|
Выполняет действие в контексте карточки с указанием имени карточки.  
[StoreCardFuncAsync](T_Tessa_Cards_StoreCardFuncAsync.htm)|  Функция, которая
выполняет асинхронное сохранение карточки с файлами по заданным параметрам.
При этом сохраняется контент добавленных или изменённых файлов и опционально
выводится информация по прогрессу сохранения.  
## __Перечисления
[CardButtonType](T_Tessa_Cards_CardButtonType.htm)|  Виды кнопок в карточке.  
---|---  
[CardCompressionMode](T_Tessa_Cards_CardCompressionMode.htm)|  Способ сжатия
возвращаемого объекта карточки.  
[CardControlTypeFlags](T_Tessa_Cards_CardControlTypeFlags.htm)|  Флаги
элемента управления, описывающие его поведение.  
[CardControlTypeUsageMode](T_Tessa_Cards_CardControlTypeUsageMode.htm)|
Способ использования для элемента управления
[CardControlType](T_Tessa_Cards_CardControlType.htm).  
[CardDeleteMethod](T_Tessa_Cards_CardDeleteMethod.htm)|  Способ удаления
карточки.  
[CardDeletionMode](T_Tessa_Cards_CardDeletionMode.htm)|  Способ удаления
карточки.  
[CardFileFlags](T_Tessa_Cards_CardFileFlags.htm)|  Флаги файла.  
[CardFileFormat](T_Tessa_Cards_CardFileFormat.htm)|  Формат файла для
экспорта/импорта карточек.  
[CardFilePreviewPosition](T_Tessa_Cards_CardFilePreviewPosition.htm)|
Местоположение для области предпросмотра файлов на форме карточки.  
[CardFileReplacementResult](T_Tessa_Cards_CardFileReplacementResult.htm)|
Результат изменения состояния файла методом
[SetReplacedState()](M_Tessa_Cards_CardFile_SetReplacedState.htm).  
[CardFileState](T_Tessa_Cards_CardFileState.htm)|  Состояние файла
[CardFile](T_Tessa_Cards_CardFile.htm) в карточке
[Card](T_Tessa_Cards_Card.htm).  
[CardFileVersionState](T_Tessa_Cards_CardFileVersionState.htm)|  Состояние
версии файла.  
[CardFlags](T_Tessa_Cards_CardFlags.htm)|  Флаги карточки.  
[CardGetFileContentMethod](T_Tessa_Cards_CardGetFileContentMethod.htm)|
Способ загрузки контента файла.  
[CardGetFileVersionsMethod](T_Tessa_Cards_CardGetFileVersionsMethod.htm)|
Способ загрузки списка версий файла.  
[CardGetMethod](T_Tessa_Cards_CardGetMethod.htm)|  Способ загрузки карточки.  
[CardGetMode](T_Tessa_Cards_CardGetMode.htm)|  Способ открытия карточки.  
[CardGetRestrictionFlags](T_Tessa_Cards_CardGetRestrictionFlags.htm)|  Флаги,
ограничивающие загружаемую по карточке информацию.  
[CardGetTaskMode](T_Tessa_Cards_CardGetTaskMode.htm)|  Способ загрузки заданий
в карточке.  
[CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)|  Тип экземпляра
карточки.  
[CardNewMethod](T_Tessa_Cards_CardNewMethod.htm)|  Способ создания карточки.  
[CardNewMode](T_Tessa_Cards_CardNewMode.htm)|  Способ создания карточки.  
[CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)|  Права доступа
на карточку, секцию, строку или поле.  
[CardRemoveChangesDeletedHandling](T_Tessa_Cards_CardRemoveChangesDeletedHandling.htm)|
Способ обработки удалённых строк, файлов и заданий при вызове метода карточки
[RemoveChanges(CardRemoveChangesDeletedHandling)](M_Tessa_Cards_Card_RemoveChanges.htm).  
[CardRowSortingType](T_Tessa_Cards_CardRowSortingType.htm)|  Тип сортировки
строк для коллекционной или древовидной секции, которая используется при
вставке и удалении строк в процессе сохранения карточки.  
[CardRowState](T_Tessa_Cards_CardRowState.htm)|  Состояние строки
[CardRow](T_Tessa_Cards_CardRow.htm) в карточке
[Card](T_Tessa_Cards_Card.htm).  
[CardSectionType](T_Tessa_Cards_CardSectionType.htm)|  Тип секции карточки.  
[CardServiceType](T_Tessa_Cards_CardServiceType.htm)|  Тип сервиса, от
которого был получен текущий объект запроса. Значение используется для
определения безопасности в проверке данных, заданных в запросе. Если при
выполнении расширений был создан внутренний запрос, то его типа сервиса будет
равен [Default](T_Tessa_Cards_CardServiceType.htm).  
[CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm)|  Способ сохранения
карточки.  
[CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)|  Способ сохранения карточки.  
[CardStoreOperationMode](T_Tessa_Cards_CardStoreOperationMode.htm)|  Режим
выполнения операции по сохранению карточки с файлами.  
[CardTableType](T_Tessa_Cards_CardTableType.htm)|  Тип коллекционной или
древовидной секции карточки.  
[CardTaskAction](T_Tessa_Cards_CardTaskAction.htm)|  Действие, выполняемое с
заданием.  
[CardTaskDialogNewMethod](T_Tessa_Cards_CardTaskDialogNewMethod.htm)|  Способ
создания карточки диалога.  
[CardTaskDialogOpenMode](T_Tessa_Cards_CardTaskDialogOpenMode.htm)|  Режим
открытия диалогового окна, связанного с заданием.  
[CardTaskDialogStoreMode](T_Tessa_Cards_CardTaskDialogStoreMode.htm)|  Режим
сохранения карточки диалога.  
[CardTaskFlags](T_Tessa_Cards_CardTaskFlags.htm)|  Флаги задания.  
[CardTaskHistoryState](T_Tessa_Cards_CardTaskHistoryState.htm)|  Состояние
записи в истории заданий
[CardTaskHistoryItem](T_Tessa_Cards_CardTaskHistoryItem.htm) в карточке
[Card](T_Tessa_Cards_Card.htm).  
[CardTaskPlannedType](T_Tessa_Cards_CardTaskPlannedType.htm)|  Тип
запланированного времени исполнения для задания.  
[CardTaskState](T_Tessa_Cards_CardTaskState.htm)|  Состояние задания.  
[CardTypeColumnAlignment](T_Tessa_Cards_CardTypeColumnAlignment.htm)|
Выравнивание содержимого, отображаемого в колонке коллекционной или
древовидной секции [CardTypeColumn](T_Tessa_Cards_CardTypeColumn.htm).  
[CardTypeColumnFlags](T_Tessa_Cards_CardTypeColumnFlags.htm)|  Флаги,
определяющие дополнительные атрибуты колонки
[CardTypeColumn](T_Tessa_Cards_CardTypeColumn.htm) коллекционной или
древовидной секции карточки.  
[CardTypeCompletionOptionFlags](T_Tessa_Cards_CardTypeCompletionOptionFlags.htm)|
Флаги варианта завершения в типе карточки задания.  
[CardTypeCustomControlFlags](T_Tessa_Cards_CardTypeCustomControlFlags.htm)|
Флаги, определяющие дополнительные атрибуты элемента управления
[CardTypeCustomControl](T_Tessa_Cards_CardTypeCustomControl.htm).  
[CardTypeEntryControlFlags](T_Tessa_Cards_CardTypeEntryControlFlags.htm)|
Флаги, определяющие дополнительные атрибуты элемента управления
[CardTypeEntryControl](T_Tessa_Cards_CardTypeEntryControl.htm).  
[CardTypeFlags](T_Tessa_Cards_CardTypeFlags.htm)|  Флаги типа карточки.  
[CardTypeTabControlFlags](T_Tessa_Cards_CardTypeTabControlFlags.htm)|  Флаги,
определяющие дополнительные атрибуты элемента управления
[CardTypeTabControl](T_Tessa_Cards_CardTypeTabControl.htm).  
[CardTypeTableControlFlags](T_Tessa_Cards_CardTypeTableControlFlags.htm)|
Флаги, определяющие дополнительные атрибуты элемента управления
[CardTypeTableControl](T_Tessa_Cards_CardTypeTableControl.htm).  
[SerializationMode](T_Tessa_Cards_SerializationMode.htm)|  Способ
десериализации, указываемый в методах
[!:CardSerializableObject.OnDeserializingAsync] и
[!:CardSerializableObject.OnDeserializedAsync].  
[ViewMapColumnType](T_Tessa_Cards_ViewMapColumnType.htm)|  Тип колонки в
маппинге представления
