# ExcelPlaceholderReplaceExtensionContext - класс
Контекст обработки расширений
[IPlaceholderReplaceExtension](T_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension.htm)
в Excel документах
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ExcelPlaceholderReplaceExtensionContext : OpenXmlPlaceholderReplaceExtensionContext
VB __Копировать
     Public NotInheritable Class ExcelPlaceholderReplaceExtensionContext
    	Inherits OpenXmlPlaceholderReplaceExtensionContext
C++ __Копировать
     public ref class ExcelPlaceholderReplaceExtensionContext sealed : public OpenXmlPlaceholderReplaceExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type ExcelPlaceholderReplaceExtensionContext = 
        class
            inherit OpenXmlPlaceholderReplaceExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm) __[OpenXmlPlaceholderReplaceExtensionContext](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderReplaceExtensionContext.htm) __ ExcelPlaceholderReplaceExtensionContext
##  __Конструкторы
[ExcelPlaceholderReplaceExtensionContext](M_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext__ctor.htm)|
Инициализирует новый экземпляр класса ExcelPlaceholderReplaceExtensionContext  
---|---  
##  __Свойства
[CancellationToken](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
---|---  
[Cell](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_Cell.htm)|
Текущая обрабатываеммая ячейка. Доступна в методах обработки плейсхолдеров.  
[CurrentRowElement](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_CurrentRowElement.htm)|
Текущая обрабатываемая строка. Доступна в методах обработки плейсхолдера.  
[Document](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_Document.htm)|
Текущий документ. Доступен в любом расширении, но структуру документа
рекомендуется изменять только в
[AfterDocumentReplace(IPlaceholderReplaceExtensionContext)](M_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension_AfterDocumentReplace.htm)  
[FindingContext](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_FindingContext.htm)|  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[GroupLevel](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GroupLevel.htm)|
Флаг определяет текущий уровень вложенности группы.  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Info](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Info.htm)|
Инфо контекста  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[IsGroup](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_IsGroup.htm)|
Флаг показывает, относится ли текущая обработка строки к обработке строки
группировки.  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Placeholder](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Placeholder.htm)|
Текущий плейсхолдер  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[PlaceholderElement](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_PlaceholderElement.htm)|
Элемент, в котором фактически производится замена плейсхолдера. Может
отличаться от
[Cell](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_Cell.htm),
т.к. значение ячейки в Excel может быть записано, например, в SharedStringItem  
[PlaceholderText](P_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderReplaceExtensionContext_PlaceholderText.htm)|  
(Унаследован от
[OpenXmlPlaceholderReplaceExtensionContext](T_Tessa_Extensions_Default_Server_Cards_OpenXmlPlaceholderReplaceExtensionContext.htm))  
[PlaceholderTextElement](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_PlaceholderTextElement.htm)|
Элемент, хранящий замененный текст. Может быть CellValue, Text или Text  
[PlaceholderValue](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_PlaceholderValue.htm)|
Текущее значение для замены в плейсхолдере  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[ReplacementContext](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_ReplacementContext.htm)|
Контекст замены плейсхолдеров  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Row](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Row.htm)|
Текущая строка  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[RowElements](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_RowElements.htm)|
Набор всех строк, определяющих строку с плейсхолдерами. Заполняется по мере
генерации строки. Полностью заполнен только в методе
[AfterRowReplace(IPlaceholderReplaceExtensionContext)](M_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension_AfterRowReplace.htm)  
[Table](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_Table.htm)|
Текущая таблица  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[TableElements](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_TableElements.htm)|
Набор всех строк, добавленных в таблицу. Заполняется по мере генерации этих
строк. Полностью заполнен только в методе
[AfterTableReplace(IPlaceholderReplaceExtensionContext)](M_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtension_AfterTableReplace.htm)  
[ValidationResult](P_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_ValidationResult.htm)|
Результат валидации  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[Worksheet](P_Tessa_Extensions_Default_Server_Cards_ExcelPlaceholderReplaceExtensionContext_Worksheet.htm)|
Текущий лист в Excel, в котором производится замена плейсхолдеров. Доступен во
всех методах обработки таблиц, строк и плейсхолдеров, если замена значения
производится в листе.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPlaceholderValueAsync](M_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GetPlaceholderValueAsync.htm)|
Метод для получения значения плейсхолдера в виде
[PlaceholderValue](P_Tessa_Platform_Placeholders_Extensions_IPlaceholderReplaceExtensionContext_PlaceholderValue.htm)  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[GetTextFromPlaceholderAsync](M_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GetTextFromPlaceholderAsync.htm)|
Метод для получения текста по плейсхолдеру  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValueFromPlaceholderAsync<T>](M_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext_GetValueFromPlaceholderAsync__1.htm)|
Метод для получения значения плейсхолдера  
(Унаследован от
[PlaceholderReplaceExtensionContext](T_Tessa_Platform_Placeholders_Extensions_PlaceholderReplaceExtensionContext.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
