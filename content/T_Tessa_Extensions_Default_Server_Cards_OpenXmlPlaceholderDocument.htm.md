# OpenXmlPlaceholderDocument - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class OpenXmlPlaceholderDocument : PlaceholderDocument
VB __Копировать
     Public MustInherit Class OpenXmlPlaceholderDocument
    	Inherits PlaceholderDocument
C++ __Копировать
     public ref class OpenXmlPlaceholderDocument abstract : public PlaceholderDocument
F# __Копировать
     [<AbstractClassAttribute>]
    type OpenXmlPlaceholderDocument = 
        class
            inherit PlaceholderDocument
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm) __ OpenXmlPlaceholderDocument
Derived
[Tessa.Extensions.Default.Server.Cards.ExcelPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderDocument.htm)
[Tessa.Extensions.Default.Server.Cards.WordPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument.htm)
##  __Конструкторы
[OpenXmlPlaceholderDocument](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument__ctor.htm)|
Создаёт экземпляр класс с указанием потока файла документа, в котором должны
быть заменены плейсхолдеры.  
---|---  
## __Свойства
[ExtensionContext](P_Tessa_Platform_Placeholders_PlaceholderDocument_ExtensionContext.htm)|
Контекст расширений. Равен null до вызова метода Replace или если в контексте
замены не задан ExtensionExecutor  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
---|---  
[HasChanges](P_Tessa_Platform_Placeholders_PlaceholderDocument_HasChanges.htm)|
Признак того, что в документ были внесены изменения при выполнении операции
замены.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[Stream](P_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_Stream.htm)|
Поток файла документа, в которой должны быть или уже были заменены
плейсхолдеры.  
[WithExtensions](P_Tessa_Platform_Placeholders_PlaceholderDocument_WithExtensions.htm)|
Признак того, что замена плейсхолдеров выполняется с расширениями
[IPlaceholderReplaceExtension](T_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension.htm).  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
##  __Методы
[AfterDocumentReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_AfterDocumentReplaceAsync.htm)|
Выполняет расширения после замены всех плейсхолдеров в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
---|---  
[AfterPlaceholderReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_AfterPlaceholderReplaceAsync.htm)|
Выполняет расширения после замены каждого плейсхолдера в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[AfterRowReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_AfterRowReplaceAsync.htm)|
Выполняет расширения после замены строки таблицы в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[AfterTableReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_AfterTableReplaceAsync.htm)|
Выполняет расширения после замены таблицы в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[BeforeDocumentReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_BeforeDocumentReplaceAsync.htm)|
Выполняет расширения перед заменой всех плейсхолдеров в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[BeforePlaceholderReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_BeforePlaceholderReplaceAsync.htm)|
Выполняет расширения перед заменой каждого плейсхолдера в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[BeforeRowReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_BeforeRowReplaceAsync.htm)|
Выполняет расширения перед заменой строки таблицы в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[BeforeTableReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_BeforeTableReplaceAsync.htm)|
Выполняет расширения перед заменой таблицы в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[CheckTextElement](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_CheckTextElement.htm)|
Метод производит проверку, что данный текстовый элемент допустим для замены
текста в нем  
[CleanAfterChanges](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_CleanAfterChanges.htm)|
Метод для выполнения постобработки документа после изменений  
[ClearOldRelationships](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ClearOldRelationships.htm)|
Метод для очистки старых ссылок из документа  
[CreateExtensionContext](M_Tessa_Platform_Placeholders_PlaceholderDocument_CreateExtensionContext.htm)|
Метод для создания контекста расширений.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FindAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_FindAsync.htm)|
Выполняет поиск плейсхолдеров в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[FindCoreAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_FindCoreAsync.htm)|  
(Переопределяет
[PlaceholderDocument.FindCoreAsync(IPlaceholderFindingContext)](M_Tessa_Platform_Placeholders_PlaceholderDocument_FindCoreAsync.htm))  
[GetElementByPlaceholder](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetElementByPlaceholder.htm)|
Метод для получаения элемента по плейсхолдеру в документе  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPlaceholdersFromDatabaseAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromDatabaseAsync.htm)|
Метод для получения информации о плейсхолдерах документа из базы данных  
[GetPlaceholdersFromDocument](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromDocument.htm)|
Метод для получения плейсхолдеров из объекта документа  
[GetPlaceholdersFromElement](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromElement.htm)|
Находим во всех дочерних элементах
#### Значение поля
baseElement плейсхолдеры  
[GetPlaceholdersFromElementOverride](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromElementOverride.htm)|
Метод для поиска плейсхолдеров внутри элемента документа  
[GetPlaceholdersFromPart](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromPart.htm)|
Находим во всех частях и элементах basePart плейсхолдеры  
[GetPlaceholdersFromRelationships](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromRelationships.htm)|
Получает список плейсхолдеров из списока Relationships  
[GetRelativeElement<TType>](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetRelativeElement__1.htm)|
Получает дочерний элемент newParent, соответствующий элементу baseChild
относительно baseParent. Элемент newParent должен быть полной копией элемента
baseParent  
[GetTextElement](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetTextElement.htm)|
Возвращает первый дочерний элемент с типом OpenXmlLeafTextElement среди всех
дочерних элементов объейкта baseElement  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitDocument](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_InitDocument.htm)|
Метод для инициализации документа  
[IsRelationship](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_IsRelationship.htm)|
Метод для проверки принадлежности плейсхолдера к Relationship  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnChangedAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_OnChangedAsync.htm)|
Событие, возникающее при каждом изменении документа.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[PrepareDocumentForSave](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_PrepareDocumentForSave.htm)|
Метод для подготовки документа к сохранению  
[RemoveInvalidChars](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_RemoveInvalidChars.htm)|
Метод для удаления их строки всех запрещенных в XML символов  
[ReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_ReplaceAsync.htm)|
Выполняет замену плейсхолдеров в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[ReplaceCoreAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceCoreAsync.htm)|  
(Переопределяет
[PlaceholderDocument.ReplaceCoreAsync(IPlaceholderReplacementContext)](M_Tessa_Platform_Placeholders_PlaceholderDocument_ReplaceCoreAsync.htm))  
[ReplaceElementAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementAsync.htm)|
Производит замену плейсхолдера в baseElement. Если текстовая часть baseElement
содержит только начало плейсхолдера, то возвращаем
ReplacementStatus.PartFound.  
[ReplaceElementsInCompositeElementAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementsInCompositeElementAsync.htm)|
Производит замену Replacement'ов в заданном элементе  
[ReplaceElementsInRelationshipsAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementsInRelationshipsAsync.htm)|
Производит замену плейсхолдеров в гиперссылке  
[ReplaceElementsInRelationshipsWithCopyAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementsInRelationshipsWithCopyAsync.htm)|
Производит замену плейсхолдеров в гиперссылке с ее копированием  
[ReplaceFieldPlaceholdersAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceFieldPlaceholdersAsync.htm)|
Метод для замены плейсхолдеров типа Field  
[ReplaceImageAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceImageAsync.htm)|
Метод, определяющий правила замены изображения в элементе документа.
Возвращает признак того, что замена выполнена успешно.  
[ReplaceTablePlaceholdersAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceTablePlaceholdersAsync.htm)|
Метод для замены плейсхолдеров типа Table  
[ReplaceTextAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceTextAsync.htm)|
Метод, определяющий правила замены текста в элементе документа  
[SaveDocument](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_SaveDocument.htm)|
Метод для сохранения инициализированного документа  
[SavePlaceholdersInDatabaseAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_SavePlaceholdersInDatabaseAsync.htm)|
Метод для сохранения информации о плейсхолдерах документа в базу данных  
[TextPosition](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_TextPosition.htm)|
Метод переводит позицию объекта в документе в строку  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[Changed](E_Tessa_Platform_Placeholders_PlaceholderDocument_Changed.htm)|
Событие, вызываемое в том случае, если в документ были внесены изменения при
выполнении операции замены.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
---|---  
##  __Поля
[Hyperlink](F_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_Hyperlink.htm)|
Значение определяет принадлежность данного плейсхолдера к гиперссылке  
---|---  
[HyperlinkRemoveHead](F_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_HyperlinkRemoveHead.htm)|  
[HyperlinkRemoveHeadLength](F_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_HyperlinkRemoveHeadLength.htm)|  
[TemplateID](F_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_TemplateID.htm)|
ID карточки шаблона файла.  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Cards - пространство
имён](N_Tessa_Extensions_Default_Server_Cards.htm)
