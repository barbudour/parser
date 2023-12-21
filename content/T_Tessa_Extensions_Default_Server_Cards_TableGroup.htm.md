# TableGroup - класс
Класс для работы с именнованными группами в Excel, определяющими таблицы
внутри шаблона Excel.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TableGroup : CellsGroup<DefinedName>
VB __Копировать
     Public NotInheritable Class TableGroup
    	Inherits CellsGroup(Of DefinedName)
C++ __Копировать
     public ref class TableGroup sealed : public CellsGroup<DefinedName^>
F# __Копировать
     [<SealedAttribute>]
    type TableGroup = 
        class
            inherit CellsGroup<DefinedName>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ElementBase](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm)<DefinedName> __[WorksheetBase](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm)<DefinedName> __[CellsGroup](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm)<DefinedName> __ TableGroup
##  __Конструкторы
[TableGroup](M_Tessa_Extensions_Default_Server_Cards_TableGroup__ctor.htm)|
Инициализирует новый экземпляр класса TableGroup  
---|---  
##  __Свойства
[Anchors](P_Tessa_Extensions_Default_Server_Cards_TableGroup_Anchors.htm)|
Список объектов якорей (надписей), входящих в данную таблицу  
---|---  
[Bottom](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Bottom.htm)|
Определяет нижнюю границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Element](P_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Element.htm)|
Хранимый элемент Excel  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[ErrorText](P_Tessa_Extensions_Default_Server_Cards_TableGroup_ErrorText.htm)|
Текст ошибки при ошибке валидации  
[ExpandableSources](P_Tessa_Extensions_Default_Server_Cards_TableGroup_ExpandableSources.htm)|
Список источников данных формул, которые должны расширяться вместе с таблицей.  
[HasParent](P_Tessa_Extensions_Default_Server_Cards_TableGroup_HasParent.htm)|
Обозначает, что группа имеет родительскую группу  
[Height](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Height.htm)|
Определяет высоту (количество строк) диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Hyperlinks](P_Tessa_Extensions_Default_Server_Cards_TableGroup_Hyperlinks.htm)|
Список объектов гиперссылок, входящих в данную таблицу  
[InnerGroups](P_Tessa_Extensions_Default_Server_Cards_TableGroup_InnerGroups.htm)|
Подчиненная группа таблицы  
[IsSingleCell](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsSingleCell.htm)|
Свойство, определяющее, состоит ли объект из одной ячейки  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[IsValid](P_Tessa_Extensions_Default_Server_Cards_TableGroup_IsValid.htm)|
Определяет, является ли данная таблица валидной  
[Left](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Left.htm)|
Определяет левую границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[MergeCells](P_Tessa_Extensions_Default_Server_Cards_TableGroup_MergeCells.htm)|
Список объектов смерженных ячеек, входящих в данную группу  
[MoveBy](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_MoveBy.htm)|
Параметр, определяющий на какое число нужно переместить элемент при обновлении  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Name](P_Tessa_Extensions_Default_Server_Cards_TableGroup_Name.htm)|  Название
именованной области  
[Reference](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Reference.htm)|
Возвращает строковый вариант диапозона (например 'B2' для одной ячейки или
'B2:D4' для группы ячеек)  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Right](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Right.htm)|
Определяет правую границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Rows](P_Tessa_Extensions_Default_Server_Cards_TableGroup_Rows.htm)|  Список
объектов строк, входящих в данную таблицу  
[Top](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Top.htm)|
Определяет верхнюю границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Type](P_Tessa_Extensions_Default_Server_Cards_TableGroup_Type.htm)|  Тип
таблицы  
[Worksheet](P_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1_Worksheet.htm)|
Объект Worksheet, на базе которого хранится текущий объект  
(Унаследован от
[WorksheetBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm))  
[WorksheetName](P_Tessa_Extensions_Default_Server_Cards_TableGroup_WorksheetName.htm)|
Имя элемента Worksheet, к которому относится данная именованная область  
## __Методы
[AddAnchorPlaceholder](M_Tessa_Extensions_Default_Server_Cards_TableGroup_AddAnchorPlaceholder.htm)|
Метод для добавления плейсхолдера, связанного с объектом якоря (надписи)  
---|---  
[AddHyperlinkPlaceholder](M_Tessa_Extensions_Default_Server_Cards_TableGroup_AddHyperlinkPlaceholder.htm)|
Метод для добавления плейсхолдера, связанного с объектом гиперссылки  
[AddRowPlaceholder](M_Tessa_Extensions_Default_Server_Cards_TableGroup_AddRowPlaceholder.htm)|
Метод для добавления плейсхолдера, связанного с объектом строки.  
[Clear](M_Tessa_Extensions_Default_Server_Cards_TableGroup_Clear.htm)|
Производит очистку таблицы от старых объектов  
[Clone](M_Tessa_Extensions_Default_Server_Cards_TableGroup_Clone.htm)|  Данный
метод недоступен для текущего типа  
(Переопределяет
[ElementBase<TElement>.Clone()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Clone.htm))  
[CloneElement](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_CloneElement.htm)|
Метод для клонирования хранимого элемента  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
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
[GetAllPlaceholders](M_Tessa_Extensions_Default_Server_Cards_TableGroup_GetAllPlaceholders.htm)|
Метод для получения всех плейсхолдеров текущей таблицы  
[GetAnchorPlaceholders](M_Tessa_Extensions_Default_Server_Cards_TableGroup_GetAnchorPlaceholders.htm)|
Получает список плейсхолдеров, относящихся к переданному якорю (надписи)  
[GetDisplayString](M_Tessa_Extensions_Default_Server_Cards_TableGroup_GetDisplayString.htm)|  
(Переопределяет
[CellsGroup<TElement>.GetDisplayString()](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_GetDisplayString.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHyperlinkPlaceholders](M_Tessa_Extensions_Default_Server_Cards_TableGroup_GetHyperlinkPlaceholders.htm)|
Получает список плейсхолдеров, относящихся к переданной гиперссылке  
[GetRowPlaceholders](M_Tessa_Extensions_Default_Server_Cards_TableGroup_GetRowPlaceholders.htm)|
Получает список плейсхолдеров, относящихся к переданной строке  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasChildElement<T>](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_HasChildElement__1.htm)|
Возвращает признак того, что среди наследников текущего элемента присутствует
указанный элемент.  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Initialize](M_Tessa_Extensions_Default_Server_Cards_TableGroup_Initialize.htm)|
Производит инициализацию группы. Инициализация производится сверху вниз от
болших групп к малым.  
[Insert](M_Tessa_Extensions_Default_Server_Cards_TableGroup_Insert.htm)|
Данный метод недоступен для текущего типа  
(Переопределяет
[ElementBase<TElement>.Insert()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Insert.htm))  
[IsCrossed(ICellsGroup)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsCrossed_1.htm)|
Метод проверяет, есть ли пересечения между текущей и передаваемой группами  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[IsCrossed(String, String, Int32,
Int32)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsCrossed.htm)|
Метод проверяет, есть ли пересечения между текущей и передаваемой группами  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[IsInclude(ICellsGroup)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsInclude_1.htm)|
Проверяет, включает ли данная группа в себя передаваемую группу  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[IsInclude(String)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsInclude.htm)|
Проверяет, включает ли данная группа в себя передаваемую ссылку.  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[IsIncludeCell](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsIncludeCell.htm)|
Метод проверяет, входит ли передаваеммая ячейка в текущую группу  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[IsIncludeGroup(String)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsIncludeGroup.htm)|
Метод проверяет, входит ли передаваеммая группа ячеек в текущую группу  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[IsIncludeGroup(String, String, Int32,
Int32)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsIncludeGroup_1.htm)|
Метод проверяет, входит ли передаваеммая группа ячеек в текущую группу  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Move.htm)|  Метод
для перемещения элемента внутри документа Excel на заданное число. Фактическое
обновление позиции элемента в документе производится методом Update  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[ParseElement](M_Tessa_Extensions_Default_Server_Cards_TableGroup_ParseElement.htm)|
Метод для получения основных данных из хранимого элемента  
(Переопределяет
[ElementBase<TElement>.ParseElement()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_ParseElement.htm))  
[Remove](M_Tessa_Extensions_Default_Server_Cards_TableGroup_Remove.htm)|
Удаление элемента из документа. Если есть дочерняя группа, она также удаляется
из документа  
(Переопределяет
[ElementBase<TElement>.Remove()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Remove.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Update](M_Tessa_Extensions_Default_Server_Cards_TableGroup_Update.htm)|
Данный метод недоступен для текущего типа  
(Переопределяет
[ElementBase<TElement>.Update()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Update.htm))  
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
