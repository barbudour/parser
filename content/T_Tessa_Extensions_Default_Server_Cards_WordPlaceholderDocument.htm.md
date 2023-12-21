# WordPlaceholderDocument - класс
Объект, определяющий способы хранения и изменения текста с заменяемыми
плейсхолдерами для документа Word.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WordPlaceholderDocument : OpenXmlPlaceholderDocument
VB __Копировать
     Public NotInheritable Class WordPlaceholderDocument
    	Inherits OpenXmlPlaceholderDocument
C++ __Копировать
     public ref class WordPlaceholderDocument sealed : public OpenXmlPlaceholderDocument
F# __Копировать
     [<SealedAttribute>]
    type WordPlaceholderDocument = 
        class
            inherit OpenXmlPlaceholderDocument
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm) __[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm) __ WordPlaceholderDocument
##  __Конструкторы
[WordPlaceholderDocument](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument__ctor.htm)|
Создаёт экземпляр класс с указанием потока файла документа, в котором должны
быть заменены плейсхолдеры.  
---|---  
## __Свойства
[ExtensionContext](P_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_ExtensionContext.htm)|  
(Переопределяет
[PlaceholderDocument.ExtensionContext](P_Tessa_Platform_Placeholders_PlaceholderDocument_ExtensionContext.htm))  
---|---  
[HasChanges](P_Tessa_Platform_Placeholders_PlaceholderDocument_HasChanges.htm)|
Признак того, что в документ были внесены изменения при выполнении операции
замены.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[Stream](P_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_Stream.htm)|
Поток файла документа, в которой должны быть или уже были заменены
плейсхолдеры.  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
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
[CheckTextElement](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_CheckTextElement.htm)|  
(Переопределяет
[OpenXmlPlaceholderDocument.CheckTextElement(OpenXmlLeafTextElement)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_CheckTextElement.htm))  
[CleanAfterChanges](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_CleanAfterChanges.htm)|  
(Переопределяет
[OpenXmlPlaceholderDocument.CleanAfterChanges()](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_CleanAfterChanges.htm))  
[CreateExtensionContext](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_CreateExtensionContext.htm)|  
(Переопределяет
[PlaceholderDocument.CreateExtensionContext(IPlaceholderReplacementContext)](M_Tessa_Platform_Placeholders_PlaceholderDocument_CreateExtensionContext.htm))  
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
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPlaceholdersFromDatabaseAsync](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_GetPlaceholdersFromDatabaseAsync.htm)|
Метод для получения информации о плейсхолдерах документа из базы данных  
(Переопределяет
[OpenXmlPlaceholderDocument.GetPlaceholdersFromDatabaseAsync(IDbScope,
CancellationToken)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromDatabaseAsync.htm))  
[GetPlaceholdersFromDocument](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_GetPlaceholdersFromDocument.htm)|
Метод для получения плейсхолдеров из объекта документа  
(Переопределяет
[OpenXmlPlaceholderDocument.GetPlaceholdersFromDocument()](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromDocument.htm))  
[GetPlaceholdersFromElement](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromElement.htm)|
Находим во всех дочерних элементах
#### Значение поля
baseElement плейсхолдеры  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[GetPlaceholdersFromElementOverride](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_GetPlaceholdersFromElementOverride.htm)|
Метод для поиска плейсхолдеров внутри элемента документа  
(Переопределяет
[OpenXmlPlaceholderDocument.GetPlaceholdersFromElementOverride(OpenXmlElement,
IList)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromElementOverride.htm))  
[GetPlaceholdersFromPart](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_GetPlaceholdersFromPart.htm)|
Находим во всех частях и элементах basePart плейсхолдеры  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[InitDocument](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_InitDocument.htm)|
Метод для инициализации документа  
(Переопределяет
[OpenXmlPlaceholderDocument.InitDocument()](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_InitDocument.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnChangedAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_OnChangedAsync.htm)|
Событие, возникающее при каждом изменении документа.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[PrepareDocumentForSave](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_PrepareDocumentForSave.htm)|
Метод для подготовки документа к сохранению  
(Переопределяет
[OpenXmlPlaceholderDocument.PrepareDocumentForSave()](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_PrepareDocumentForSave.htm))  
[RemoveInvalidChars](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_RemoveInvalidChars.htm)|
Метод для удаления их строки всех запрещенных в XML символов  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[ReplaceAsync](M_Tessa_Platform_Placeholders_PlaceholderDocument_ReplaceAsync.htm)|
Выполняет замену плейсхолдеров в документе.  
(Унаследован от
[PlaceholderDocument](T_Tessa_Platform_Placeholders_PlaceholderDocument.htm))  
[ReplaceCoreAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceCoreAsync.htm)|  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[ReplaceElementAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementAsync.htm)|
Производит замену плейсхолдера в baseElement. Если текстовая часть baseElement
содержит только начало плейсхолдера, то возвращаем
ReplacementStatus.PartFound.  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[ReplaceElementsInCompositeElementAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementsInCompositeElementAsync.htm)|
Производит замену Replacement'ов в заданном элементе  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[ReplaceElementsInRelationshipsAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementsInRelationshipsAsync.htm)|
Производит замену плейсхолдеров в гиперссылке  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[ReplaceElementsInRelationshipsWithCopyAsync](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceElementsInRelationshipsWithCopyAsync.htm)|
Производит замену плейсхолдеров в гиперссылке с ее копированием  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
[ReplaceFieldPlaceholdersAsync](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_ReplaceFieldPlaceholdersAsync.htm)|
Производит замену плейсхолдеров типа Field в Word документе  
(Переопределяет
[OpenXmlPlaceholderDocument.ReplaceFieldPlaceholdersAsync(IPlaceholderReplacementContext)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceFieldPlaceholdersAsync.htm))  
[ReplaceImageAsync](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_ReplaceImageAsync.htm)|
Метод, определяющий правила замены изображения в элементе документа.
Возвращает признак того, что замена выполнена успешно.  
(Переопределяет [OpenXmlPlaceholderDocument.ReplaceImageAsync(OpenXmlElement,
IPlaceholderReplacement,
CancellationToken)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceImageAsync.htm))  
[ReplaceTablePlaceholdersAsync](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_ReplaceTablePlaceholdersAsync.htm)|
Производит замену плейсхолдеров типа Table в Word документе  
(Переопределяет
[OpenXmlPlaceholderDocument.ReplaceTablePlaceholdersAsync(IPlaceholderReplacementContext)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceTablePlaceholdersAsync.htm))  
[ReplaceTextAsync](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_ReplaceTextAsync.htm)|
Метод, определяющий правила замены текста в элементе документа  
(Переопределяет [OpenXmlPlaceholderDocument.ReplaceTextAsync(OpenXmlElement,
OpenXmlLeafTextElement, OpenXmlElement, OpenXmlLeafTextElement, String,
CancellationToken)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_ReplaceTextAsync.htm))  
[SaveDocument](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_SaveDocument.htm)|
Метод для сохранения инициализированного документа  
(Переопределяет
[OpenXmlPlaceholderDocument.SaveDocument()](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_SaveDocument.htm))  
[SavePlaceholdersInDatabaseAsync](M_Tessa_Extensions_Default_Server_Cards_WordPlaceholderDocument_SavePlaceholdersInDatabaseAsync.htm)|
Метод для сохранения информации о плейсхолдерах документа в базу данных  
(Переопределяет
[OpenXmlPlaceholderDocument.SavePlaceholdersInDatabaseAsync(IDbScope,
List<IPlaceholderText>,
CancellationToken)](M_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_SavePlaceholdersInDatabaseAsync.htm))  
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
[TemplateID](F_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument_TemplateID.htm)|
ID карточки шаблона файла.  
(Унаследован от
[OpenXmlPlaceholderDocument](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderDocument.htm))  
---|---  
##  __Методы расширения
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
