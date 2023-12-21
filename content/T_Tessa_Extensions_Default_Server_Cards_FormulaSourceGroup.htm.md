# FormulaSourceGroup - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class FormulaSourceGroup : CellsGroup<CellFormula>
VB __Копировать
     Public NotInheritable Class FormulaSourceGroup
    	Inherits CellsGroup(Of CellFormula)
C++ __Копировать
     public ref class FormulaSourceGroup sealed : public CellsGroup<CellFormula^>
F# __Копировать
     [<SealedAttribute>]
    type FormulaSourceGroup = 
        class
            inherit CellsGroup<CellFormula>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ElementBase](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm)<CellFormula> __[WorksheetBase](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm)<CellFormula> __[CellsGroup](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm)<CellFormula> __ FormulaSourceGroup
##  __Конструкторы
[FormulaSourceGroup](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup__ctor.htm)|
Инициализирует новый экземпляр класса FormulaSourceGroup  
---|---  
##  __Свойства
[Bottom](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Bottom.htm)|
Определяет нижнюю границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
---|---  
[Element](P_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Element.htm)|
Хранимый элемент Excel  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[Height](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Height.htm)|
Определяет высоту (количество строк) диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[InFormulaTableGroup](P_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_InFormulaTableGroup.htm)|
Флаг определяет, что источник данных находится в той же группе (или ее
подгруппе), что и сама формула.  
[InFormulaWorksheet](P_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_InFormulaWorksheet.htm)|
Определяет, находится ли источник данных для формулы в той же группе, что и
сама формула.  
[IsExpandable](P_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_IsExpandable.htm)|
Флаг определяет, что данный источник данных расширяется вместе со своей
таблицей.  
[IsSingleCell](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsSingleCell.htm)|
Свойство, определяющее, состоит ли объект из одной ячейки  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Left](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Left.htm)|
Определяет левую границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[MoveBy](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_MoveBy.htm)|
Параметр, определяющий на какое число нужно переместить элемент при обновлении  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Reference](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Reference.htm)|
Возвращает строковый вариант диапозона (например 'B2' для одной ячейки или
'B2:D4' для группы ячеек)  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Right](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Right.htm)|
Определяет правую границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Row](P_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_Row.htm)|
Строка, к которой относится данная группа.  
[TableGroup](P_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_TableGroup.htm)|
Определяет таблицу, к которой относится источник данных.  
[Top](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Top.htm)|
Определяет верхнюю границу диапозона  
(Унаследован от
[CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm))  
[Worksheet](P_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1_Worksheet.htm)|
Объект Worksheet, на базе которого хранится текущий объект  
(Унаследован от
[WorksheetBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm))  
##  __Методы
[Check](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_Check.htm)|
Метод для проверки валидности источника данных для формул. Источник данных
может стать не валидным, например, если ссылался на таблицу, которая была
удалена полностью.  
---|---  
[Clone](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_Clone.htm)|
Метод не предусмотрен для данного класса  
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
[ExpandBy](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_ExpandBy.htm)|
Метод для расширения области, которую занимает данный источник данных на
заданное число.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetDisplayString](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_GetDisplayString.htm)|
Метод для получения отображаемого значения элемента. Обычно это
[Reference](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Reference.htm)  
(Переопределяет
[CellsGroup<TElement>.GetDisplayString()](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_GetDisplayString.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Insert](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_Insert.htm)|
Метод не предусмотрен для данного класса  
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
[ParseElement](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_ParseElement.htm)|  
(Переопределяет
[ElementBase<TElement>.ParseElement()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_ParseElement.htm))  
[Remove](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Remove.htm)|
Метод для удаления объекта и его элемента  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Update](M_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup_Update.htm)|
Метод не предусмотрен для данного класса  
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
