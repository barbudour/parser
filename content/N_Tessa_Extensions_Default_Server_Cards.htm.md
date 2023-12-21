# Tessa.Extensions.Default.Server.Cards - пространство имён
Расширения типового решения на сервере, связанные с типовыми карточками.
##  __Классы
[AnchorCellGroup](T_Tessa_Extensions_Default_Server_Cards_AnchorCellGroup.htm)|
Якорь, используемый для привязки надписи или картинки к Worksheet  
---|---  
[CardExtensionHelper](T_Tessa_Extensions_Default_Server_Cards_CardExtensionHelper.htm)|
Вспомогательные методы и константы для управления карточками, доступными в
типовом решении.  
[CardNumberStoreExtension](T_Tessa_Extensions_Default_Server_Cards_CardNumberStoreExtension.htm)|
Переносит поля с Primary-номером в поля с Secondary-номером при изменении
полей с Primary-номером (или при первом сохранении), если в типе карточки есть
секция DocumentCommonInfo с Secondary-номерами. Это сделано расширением на
карточку, а не в DocumentNumberDirector, т.к. есть ручное редактирование
номера через контрол, которое тоже должно переносить данные из Primary-полей в
Secondary-поля.  
[CardPermissionsDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_CardPermissionsDeleteExtension.htm)|  
[CardPermissionsGetExtension](T_Tessa_Extensions_Default_Server_Cards_CardPermissionsGetExtension.htm)|  
[CardPermissionsNewExtension](T_Tessa_Extensions_Default_Server_Cards_CardPermissionsNewExtension.htm)|  
[CardPermissionsStoreExtension](T_Tessa_Extensions_Default_Server_Cards_CardPermissionsStoreExtension.htm)|  
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm)|
Класс для объектов, являющихся хранилищем для одной или нескольких ячеек,
включающий в себя общие методы для работы с группой ячеек  
[ContractStoreExtension](T_Tessa_Extensions_Default_Server_Cards_ContractStoreExtension.htm)|
Расширение, проверяющее корректность сохраняемой карточки договора.  
[CreateOrAddPartnerCardStoreExtension](T_Tessa_Extensions_Default_Server_Cards_CreateOrAddPartnerCardStoreExtension.htm)|  
[DefaultAdExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultAdExtension.htm)|  
[DefaultConfigurationVersionDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionDeleteExtension.htm)|
Увеличивает версию конфигурации при удалении карточек, связанных с типовым
решением. Также проверяет, что конфигурация не находится в режиме защиты от
изменений [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm). Должно
быть зарегистрировано для только определённых карточек .WhenCardTypes(...), а
также для всех видов удаления карточки .WhenAnyDeleteMethod().  
[DefaultConfigurationVersionNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionNewGetExtension.htm)|
Проверяет, что конфигурация не находится в режиме защиты от изменений
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm). Должно быть
зарегистрировано для только определённых карточек .WhenCardTypes(...).  
[DefaultConfigurationVersionStoreExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultConfigurationVersionStoreExtension.htm)|
Увеличивает версию конфигурации при изменении карточек, связанных с типовым
решением. Также проверяет, что конфигурация не находится в режиме защиты от
изменений [Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm). Должно
быть зарегистрировано для только определённых карточек .WhenCardTypes(...), а
также для всех видов сохранения карточки .WhenAnyStoreMethod().  
[DefaultDocLoadExtension](T_Tessa_Extensions_Default_Server_Cards_DefaultDocLoadExtension.htm)|
Расширение для модуля потокового ввода, используемое платформой по умолчанию.  
[DocLoadBarcodeStoreExtension](T_Tessa_Extensions_Default_Server_Cards_DocLoadBarcodeStoreExtension.htm)|  
[DocLoadBarcodeTemplateNewExtension](T_Tessa_Extensions_Default_Server_Cards_DocLoadBarcodeTemplateNewExtension.htm)|  
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm)|
Класс, описывающий общие свойства хранилищ элементов Excel  
[ExcelDocumentParser](T_Tessa_Extensions_Default_Server_Cards_ExcelDocumentParser.htm)|
Парсер документов Excel.  
[ExcelHelper](T_Tessa_Extensions_Default_Server_Cards_ExcelHelper.htm)|  Класс
с вспомогательными методами для обработки Excel  
[ExcelPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderDocument.htm)|
Объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами для документа Excel.  
[ExcelPlaceholderDocumentBuilder](T_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderDocumentBuilder.htm)|  
[ExcelPlaceholderReplaceExtensionContext](T_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext.htm)|
Контекст обработки расширений
[IPlaceholderReplaceExtension](T_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension.htm)
в Excel документах  
[FileTemplateInvalidateCacheDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_FileTemplateInvalidateCacheDeleteExtension.htm)|  
[FileTemplateInvalidateCacheStoreExtension](T_Tessa_Extensions_Default_Server_Cards_FileTemplateInvalidateCacheStoreExtension.htm)|  
[FormulaElement](T_Tessa_Extensions_Default_Server_Cards_FormulaElement.htm)|  
[FormulaSourceGroup](T_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup.htm)|  
[GetDocTypeInfoRequestExtension](T_Tessa_Extensions_Default_Server_Cards_GetDocTypeInfoRequestExtension.htm)|
Для клиентских расширений возвращаем по идентификатору карточки информацию по
её типу карточки и типу документа (если он есть). Мы не выполняем никаких
проверок безопасности, т.к. карточка ещё не открывается, а только готовится
Request к её открытию. Т.о. любой пользователь, зная идентификатор карточки,
сможет узнать, существует ли она и какого она типа. Никакой другой информации
пользователь не получит, поэтому не считаем это уязвимостью.  
[HyperlinkCellGroup](T_Tessa_Extensions_Default_Server_Cards_HyperlinkCellGroup.htm)|
Класс для работы с элементом гиперссылки в Excel  
[KrAddCycleFileInfoGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrAddCycleFileInfoGetExtension.htm)|  
[KrAddCycleFilesCardGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrAddCycleFilesCardGetExtension.htm)|  
[KrAddVirtualFilesGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrAddVirtualFilesGetExtension.htm)|  
[KrCardTaskCompletionOptionSettingsBuilder](T_Tessa_Extensions_Default_Server_Cards_KrCardTaskCompletionOptionSettingsBuilder.htm)|
Предоставляет билдер объектов типа
[CardTaskCompletionOptionSettings](T_Tessa_Cards_CardTaskCompletionOptionSettings.htm)
реализующий функционал специфичный для параметров используемых в маршрутах.  
[KrDocStateDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_KrDocStateDeleteExtension.htm)|
Расширение на удаление виртуальной карточки состояния документа.  
[KrDocStateGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrDocStateGetExtension.htm)|
Расширение на получение виртуальной карточки состояния документа.  
[KrDocStateNewExtension](T_Tessa_Extensions_Default_Server_Cards_KrDocStateNewExtension.htm)|
Расширение на создание виртуальной карточки состояния документа.  
[KrDocStateStoreExtension](T_Tessa_Extensions_Default_Server_Cards_KrDocStateStoreExtension.htm)|
Расширение на сохранение виртуальной карточки состояния документа.  
[KrPermissionRuleDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_KrPermissionRuleDeleteExtension.htm)|  
[KrPermissionRuleNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrPermissionRuleNewGetExtension.htm)|  
[KrPersonalRolesNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrPersonalRolesNewGetExtension.htm)|
Расширение для предоставления доступа сотрудникам загружать карточку
сотрудника для настроек.  
[KrPersonalRolesStoreExtension](T_Tessa_Extensions_Default_Server_Cards_KrPersonalRolesStoreExtension.htm)|
Расширение для предоставления доступа сотрудникам редактировать свои настройки
и для установки прав на редактирование некоторых полей сотрудника, заполняемых
в расширениях
[PersonalRoleStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_PersonalRoleStoreExtension.htm)
и
[FixPersonalRolesStoreExtension](T_Tessa_Extensions_Platform_Server_Roles_FixPersonalRolesStoreExtension.htm)  
[KrResetUserSettingsRequestExtension](T_Tessa_Extensions_Default_Server_Cards_KrResetUserSettingsRequestExtension.htm)|  
[KrSettingsForumLicenseGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrSettingsForumLicenseGetExtension.htm)|  
[KrVirtualFileDeleteExtension](T_Tessa_Extensions_Default_Server_Cards_KrVirtualFileDeleteExtension.htm)|
Сбрасывание кешей при удалении виртуального файла  
[KrVirtualFileNewGetExtension](T_Tessa_Extensions_Default_Server_Cards_KrVirtualFileNewGetExtension.htm)|
Расширение на создание карточки виртуального файла Генерирует FileID и
FileVersionID  
[KrVirtualFileStoreExtension](T_Tessa_Extensions_Default_Server_Cards_KrVirtualFileStoreExtension.htm)|
Расширение для сброса кеша виртуальных файлов при сохранении виртуального
файла  
[KrVirtualFileStrictSecurity](T_Tessa_Extensions_Default_Server_Cards_KrVirtualFileStrictSecurity.htm)|
Объект для установки и проверки доступа к карточке "Виртуальный файл" при
наличии ограничений в конфигурации.  
[MergeCellGroup](T_Tessa_Extensions_Default_Server_Cards_MergeCellGroup.htm)|
Класс для работы с элементом смерженные ячейкм в Excel  
[MoveFileRequestExtension](T_Tessa_Extensions_Default_Server_Cards_MoveFileRequestExtension.htm)|
Запрос на перенос контента файла на файловую систему.  
[OpenXmlExtensions](T_Tessa_Extensions_Default_Server_Cards_OpenXmlExtensions.htm)|  
[OpenXmlHelper](T_Tessa_Extensions_Default_Server_Cards_OpenXmlHelper.htm)|
Вспомогательные методы для работы с документами формата OpenXml: .docx, .xlsx.  
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm)|  
[OpenXmlPlaceholderReplaceExtensionContext](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderReplaceExtensionContext.htm)|
Базовый класс контекста обработки расширений
[IPlaceholderReplaceExtension](T_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension.htm)
в документах OpenXML  
[PartnerContractStoreExtension](T_Tessa_Extensions_Default_Server_Cards_PartnerContractStoreExtension.htm)|  
[Registrator](T_Tessa_Extensions_Default_Server_Cards_Registrator.htm)|  
[RowCellGroup](T_Tessa_Extensions_Default_Server_Cards_RowCellGroup.htm)|
Класс для работы с элементом строки Excel  
[SatelliteRemoveCardNewExtension](T_Tessa_Extensions_Default_Server_Cards_SatelliteRemoveCardNewExtension.htm)|
Расширение удаляющее из карточки шаблона информацию о ненужных сателлитах.  
[SaveFileTemplateOnCardStoreExtension](T_Tessa_Extensions_Default_Server_Cards_SaveFileTemplateOnCardStoreExtension.htm)|
Расширение добавляет выбранный пользователем шаблон файла в карточку  
[SharedStringTableContainer](T_Tessa_Extensions_Default_Server_Cards_SharedStringTableContainer.htm)|  
[TableGroup](T_Tessa_Extensions_Default_Server_Cards_TableGroup.htm)|  Класс
для работы с именнованными группами в Excel, определяющими таблицы внутри
шаблона Excel.  
[TableGroupInstance](T_Tessa_Extensions_Default_Server_Cards_TableGroupInstance.htm)|
Экземпляр таблицы со строками для замены.  
[TaskFilesExampleGetExtension](T_Tessa_Extensions_Default_Server_Cards_TaskFilesExampleGetExtension.htm)|
Пример расширения, которое переносит файлы из карточки - файлового сателлита в
карточки задач.  
[TaskFilesExampleStoreExtension](T_Tessa_Extensions_Default_Server_Cards_TaskFilesExampleStoreExtension.htm)|
Пример расширения, которое сохраняет файлы из задач карточки в карточку -
файловый сателлит.  
[WordDocumentTableGroup](T_Tessa_Extensions_Default_Server_Cards_WordDocumentTableGroup.htm)|  
[WordDocumentTableGroupParser](T_Tessa_Extensions_Default_Server_Cards_WordDocumentTableGroupParser.htm)|
Объект для парсинга документа Word на группы по закладкам документа Word.  
[WordPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument.htm)|
Объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами для документа Word.  
[WordPlaceholderDocumentBuilder](T_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocumentBuilder.htm)|  
[WordPlaceholderReplaceExtensionContext](T_Tessa_Extensions_Default_Server_Cards_WordPlaceholderReplaceExtensionContext.htm)|
Контекст обработки расширений
[IPlaceholderReplaceExtension](T_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension.htm)
в Word документах  
[WorksheetBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm)|
Класс, определяющий общие свойства объектов, хранимых на базе Worksheet  
[WorksheetElement](T_Tessa_Extensions_Default_Server_Cards_WorksheetElement.htm)|
Класс-хранилище для упрощенной работы с элементои типа Worksheet  
## __Интерфейсы
[ICellsGroup](T_Tessa_Extensions_Default_Server_Cards_ICellsGroup.htm)|
Интерфейс для объектов, являющихся хранилищем для одной или нескольких ячеек  
---|---  
[IExcelDocumentParser](T_Tessa_Extensions_Default_Server_Cards_IExcelDocumentParser.htm)|
Парсер документов Excel.  
[IWordDocumentTableGroupParser](T_Tessa_Extensions_Default_Server_Cards_IWordDocumentTableGroupParser.htm)|
Объект для парсинга документа Word на группы.  
## __Перечисления
[OpenXmlPlaceholderDocument.ReplacementStatus](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplacementStatus.htm)|
Перечислимый тип, обозначающий статус замены плейсхолдера в документе.  
---|---  
[TableGroupType](T_Tessa_Extensions_Default_Server_Cards_TableGroupType.htm)|
Список типов таблиц в Excel  
[WordDocumentTableGroupType](T_Tessa_Extensions_Default_Server_Cards_WordDocumentTableGroupType.htm)|
