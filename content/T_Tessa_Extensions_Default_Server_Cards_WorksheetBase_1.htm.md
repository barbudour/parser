# WorksheetBase<TElement> \- класс
Класс, определяющий общие свойства объектов, хранимых на базе Worksheet
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class WorksheetBase<TElement> : ElementBase<TElement>
    where TElement : OpenXmlElement
VB __Копировать
     Public MustInherit Class WorksheetBase(Of TElement As OpenXmlElement)
    	Inherits ElementBase(Of TElement)
C++ __Копировать
    generic<typename TElement>
    where TElement : OpenXmlElement
    public ref class WorksheetBase abstract : public ElementBase<TElement>
F# __Копировать
     [<AbstractClassAttribute>]
    type WorksheetBase<'TElement when 'TElement : OpenXmlElement> = 
        class
            inherit ElementBase<'TElement>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ElementBase](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm)<TElement> __ WorksheetBase<TElement>
Derived
[Tessa.Extensions.Default.Server.Cards.CellsGroup<TElement>](T_Tessa_Extensions_Default_Server_Cards_CellsGroup_1.htm)
[Tessa.Extensions.Default.Server.Cards.FormulaElement](T_Tessa_Extensions_Default_Server_Cards_FormulaElement.htm)
#### Параметры типа
TElement
    Тип хранимого элемента Excel
##  __Конструкторы
[WorksheetBase<TElement>(TElement)](M_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1__ctor.htm)|
Инициализирует новый экземпляр класса WorksheetBase<TElement>  
---|---  
[WorksheetBase<TElement>(TElement,
WorksheetElement)](M_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1__ctor_1.htm)|
Инициализирует новый экземпляр класса WorksheetBase<TElement>  
##  __Свойства
[Element](P_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Element.htm)|
Хранимый элемент Excel  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
---|---  
[Worksheet](P_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1_Worksheet.htm)|
Объект Worksheet, на базе которого хранится текущий объект  
## __Методы
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
[Insert](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Insert.htm)|
Метод для вставки элемента.  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
