# CardComponentHelper - класс
Вспомогательные методы и константы для компонентов API карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardComponentHelper
VB __Копировать
     Public NotInheritable Class CardComponentHelper
C++ __Копировать
     public ref class CardComponentHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardComponentHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardComponentHelper
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
## __Поля
[ContentFileDataKey](F_Tessa_Cards_ComponentModel_CardComponentHelper_ContentFileDataKey.htm)|
Ключ для содержимого файла, выгруженного в текстовый формат JSON.  
---|---  
[ContentFileIDKey](F_Tessa_Cards_ComponentModel_CardComponentHelper_ContentFileIDKey.htm)|
Ключ для идентификатора файла, который записывается рядом с его содержимым в
карточке, выгруженной в текстовый формат JSON.  
[ContentFileReferenceKey](F_Tessa_Cards_ComponentModel_CardComponentHelper_ContentFileReferenceKey.htm)|
Ключ для содержимого файла, выгруженного в текстовый формат JSON.  
[ContentFileSizeKey](F_Tessa_Cards_ComponentModel_CardComponentHelper_ContentFileSizeKey.htm)|
Ключ для размера файла, который записывается рядом с его содержимым в
карточке, выгруженной в текстовый формат JSON.  
[DoNotCheckVersion](F_Tessa_Cards_ComponentModel_CardComponentHelper_DoNotCheckVersion.htm)|
Значение версии, которое передаётся в метод [ExecuteInWriterLockAsync(Guid,
Int32, IValidationResultBuilder, Func<ICardTransactionParameter, Task>,
Boolean,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardTransactionStrategy_ExecuteInWriterLockAsync.htm)
для того, чтобы обозначить, что проверка версии не требуется. Это имеет смысл
при удалении карточки.  
[FileFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_FileFactory.htm)|
Фабрика, используемая для создания объекта ListStorage<CardFile>, который
содержит файлы карточки.  
[FileMappingFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_FileMappingFactory.htm)|
Фабрика, используемая для создания объекта
ListStorage<CardFileContentMapping>, который содержит объекты маппинга
сохраняемого контента.  
[RowFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_RowFactory.htm)|
Фабрика, используемая для создания объекта ListStorage<CardRow>, который
содержит строки коллекционной и древовидной секции.  
[SectionFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_SectionFactory.htm)|
Фабрика, используемая для создания объекта
StringDictionaryStorage<CardSection>, который содержит секции карточки.  
[SectionRowsFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_SectionRowsFactory.htm)|
Фабрика, используемая для создания объекта StringDictionaryStorage<CardRow>,
который содержит пустые строки коллекционных и древовидных секций.  
[TaskFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_TaskFactory.htm)|
Фабрика, используемая для создания объекта ListStorage<CardTask>, который
содержит задания карточки.  
[TaskHistoryFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_TaskHistoryFactory.htm)|
Фабрика, используемая для создания объекта ListStorage<CardTaskHistoryItem>,
который содержит записи в истории действий карточки.  
[TaskHistoryGroupFactory](F_Tessa_Cards_ComponentModel_CardComponentHelper_TaskHistoryGroupFactory.htm)|
Фабрика, используемая для создания объекта ListStorage<CardTaskHistoryGroup>,
который содержит группы в истории действий карточки.  
[TemporaryTaskRoleTypeIDList](F_Tessa_Cards_ComponentModel_CardComponentHelper_TemporaryTaskRoleTypeIDList.htm)|
Идентификаторы типов ролей, которые являются временными ролями заданий.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
