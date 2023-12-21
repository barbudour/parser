# ElementBase<TElement> \- класс
Класс, описывающий общие свойства хранилищ элементов Excel
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ElementBase<TElement>
    where TElement : OpenXmlElement
VB __Копировать
     Public MustInherit Class ElementBase(Of TElement As OpenXmlElement)
C++ __Копировать
    generic<typename TElement>
    where TElement : OpenXmlElement
    public ref class ElementBase abstract
F# __Копировать
     [<AbstractClassAttribute>]
    type ElementBase<'TElement when 'TElement : OpenXmlElement> = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ElementBase<TElement>
Derived
[Tessa.Extensions.Default.Server.Cards.WorksheetBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_WorksheetBase_1.htm)
[Tessa.Extensions.Default.Server.Cards.WorksheetElement](T_Tessa_Extensions_Default_Server_Cards_WorksheetElement.htm)
#### Параметры типа
TElement
    Тип хранимого элемента Excel
##  __Конструкторы
[ElementBase<TElement>](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1__ctor.htm)|
Инициализирует новый экземпляр класса ElementBase<TElement>  
---|---  
##  __Свойства
[Element](P_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Element.htm)|
Хранимый элемент Excel  
---|---  
## __Методы
[Clone](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Clone.htm)|
Метод для клонирования хранимого элемента.  
---|---  
[CloneElement](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_CloneElement.htm)|
Метод для клонирования хранимого элемента  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ParseElement](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_ParseElement.htm)|
Метод для получения основных данных из хранимого элемента  
[Remove](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Remove.htm)|
Метод для удаления объекта и его элемента  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Update](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Update.htm)|
Метод для обновления позиции элемента в документе Excel  
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
