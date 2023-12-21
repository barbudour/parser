# CellsGroup<TElement> \- класс
Класс для объектов, являющихся хранилищем для одной или нескольких ячеек,
включающий в себя общие методы для работы с группой ячеек
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class CellsGroup<TElement> : WorksheetBase<TElement>, 
    	ICellsGroup
    where TElement : OpenXmlElement
VB __Копировать
     Public MustInherit Class CellsGroup(Of TElement As OpenXmlElement)
    	Inherits WorksheetBase(Of TElement)
    	Implements ICellsGroup
C++ __Копировать
    generic<typename TElement>
    where TElement : OpenXmlElement
    public ref class CellsGroup abstract : public WorksheetBase<TElement>, 
    	ICellsGroup
F# __Копировать
     [<AbstractClassAttribute>]
    type CellsGroup<'TElement when 'TElement : OpenXmlElement> = 
        class
            inherit WorksheetBase<'TElement>
            interface ICellsGroup
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ElementBase](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm)<TElement> __[WorksheetBase](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm)<TElement> __ CellsGroup<TElement>
Derived
[Tessa.Extensions.Default.Server.Cards.AnchorCellGroup](T_Tessa_Extensions_Default_Server_Cards_AnchorCellGroup.htm)
[Tessa.Extensions.Default.Server.Cards.FormulaSourceGroup](T_Tessa_Extensions_Default_Server_Cards_FormulaSourceGroup.htm)
[Tessa.Extensions.Default.Server.Cards.HyperlinkCellGroup](T_Tessa_Extensions_Default_Server_Cards_HyperlinkCellGroup.htm)
[Tessa.Extensions.Default.Server.Cards.MergeCellGroup](T_Tessa_Extensions_Default_Server_Cards_MergeCellGroup.htm)
[Tessa.Extensions.Default.Server.Cards.RowCellGroup](T_Tessa_Extensions_Default_Server_Cards_RowCellGroup.htm)
[Tessa.Extensions.Default.Server.Cards.TableGroup](T_Tessa_Extensions_Default_Server_Cards_TableGroup.htm)
Подробнее __Less __
Implements
    [ICellsGroup](T_Tessa_Extensions_Default_Server_Cards_ICellsGroup.htm)
#### Параметры типа
TElement
##  __Конструкторы
[CellsGroup<TElement>(TElement)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1__ctor.htm)|
Инициализирует новый экземпляр класса CellsGroup<TElement>  
---|---  
[CellsGroup<TElement>(TElement,
WorksheetElement)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1__ctor_1.htm)|
Инициализирует новый экземпляр класса CellsGroup<TElement>  
##  __Свойства
[Bottom](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Bottom.htm)|
Определяет нижнюю границу диапозона  
---|---  
[Element](P_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Element.htm)|
Хранимый элемент Excel  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[Height](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Height.htm)|
Определяет высоту (количество строк) диапозона  
[IsSingleCell](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsSingleCell.htm)|
Свойство, определяющее, состоит ли объект из одной ячейки  
[Left](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Left.htm)|
Определяет левую границу диапозона  
[MoveBy](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_MoveBy.htm)|
Параметр, определяющий на какое число нужно переместить элемент при обновлении  
[Reference](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Reference.htm)|
Возвращает строковый вариант диапозона (например 'B2' для одной ячейки или
'B2:D4' для группы ячеек)  
[Right](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Right.htm)|
Определяет правую границу диапозона  
[Top](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Top.htm)|
Определяет верхнюю границу диапозона  
[Worksheet](P_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1_Worksheet.htm)|
Объект Worksheet, на базе которого хранится текущий объект  
(Унаследован от
[WorksheetBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm))  
##  __Методы
[Clone](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Clone.htm)|
Метод для клонирования хранимого элемента.  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
---|---  
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
[GetDisplayString](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_GetDisplayString.htm)|
Метод для получения отображаемого значения элемента. Обычно это
[Reference](P_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Reference.htm)  
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
[Insert](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Insert.htm)|
Метод для вставки элемента.  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[IsCrossed(ICellsGroup)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsCrossed_1.htm)|
Метод проверяет, есть ли пересечения между текущей и передаваемой группами  
[IsCrossed(String, String, Int32,
Int32)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsCrossed.htm)|
Метод проверяет, есть ли пересечения между текущей и передаваемой группами  
[IsInclude(ICellsGroup)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsInclude_1.htm)|
Проверяет, включает ли данная группа в себя передаваемую группу  
[IsInclude(String)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsInclude.htm)|
Проверяет, включает ли данная группа в себя передаваемую ссылку.  
[IsIncludeCell](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsIncludeCell.htm)|
Метод проверяет, входит ли передаваеммая ячейка в текущую группу  
[IsIncludeGroup(String)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsIncludeGroup.htm)|
Метод проверяет, входит ли передаваеммая группа ячеек в текущую группу  
[IsIncludeGroup(String, String, Int32,
Int32)](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_IsIncludeGroup_1.htm)|
Метод проверяет, входит ли передаваеммая группа ячеек в текущую группу  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](M_Tessa_Extensions_Default_Server_Cards_CellsGroup_1_Move.htm)|  Метод
для перемещения элемента внутри документа Excel на заданное число. Фактическое
обновление позиции элемента в документе производится методом Update  
[ParseElement](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_ParseElement.htm)|
Метод для получения основных данных из хранимого элемента  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[Remove](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Remove.htm)|
Метод для удаления объекта и его элемента  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Update](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Update.htm)|
Метод для обновления позиции элемента в документе Excel  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
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
