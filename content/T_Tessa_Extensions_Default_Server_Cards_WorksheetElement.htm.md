# WorksheetElement - класс
Класс-хранилище для упрощенной работы с элементои типа Worksheet
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Cards](N_Tessa_Extensions_Default_Server_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WorksheetElement : ElementBase<Worksheet>
VB __Копировать
     Public NotInheritable Class WorksheetElement
    	Inherits ElementBase(Of Worksheet)
C++ __Копировать
     public ref class WorksheetElement sealed : public ElementBase<Worksheet^>
F# __Копировать
     [<SealedAttribute>]
    type WorksheetElement = 
        class
            inherit ElementBase<Worksheet>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ElementBase](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm)<Worksheet> __ WorksheetElement
##  __Конструкторы
[WorksheetElement](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement__ctor.htm)|
Инициализирует новый экземпляр класса WorksheetElement  
---|---  
##  __Свойства
[Anchors](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Anchors.htm)|
Список объектов-якорей, используемых для привязки надписей и картинок к
данному элементу  
---|---  
[Element](P_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Element.htm)|
Хранимый элемент Excel  
(Унаследован от
[ElementBase<TElement>](T_Tessa_Extensions_Default_Server_Cards_ElementBase_1.htm))  
[HasFormulas](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_HasFormulas.htm)|
Флаг определяет, есть ли в данном листе формула или источник данных для
формулы.  
[Hyperlinks](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Hyperlinks.htm)|
Список объектов гиперссылок, хранимых в данном элементе  
[MergeCells](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_MergeCells.htm)|
Список объектов смерженных ячеек, хранимых в данном элементе  
[Name](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Name.htm)|
Имя элемента  
[Rows](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Rows.htm)|
Список объектов строк, хранимых в данном элементе  
[SharedFormulas](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_SharedFormulas.htm)|
Расшаренные формулы.  
[Tables](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Tables.htm)|
Список всех таблиц верхнего уровня в текущем элементе, отсортированных сверху
вниз.  
[WorksheetHash](P_Tessa_Extensions_Default_Server_Cards_WorksheetElement_WorksheetHash.htm)|
Хеш страниц Excel по имени.  
## __Методы
[Clone](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Clone.htm)|
Клонирование элемента типа Worksheet недоступно  
(Переопределяет
[ElementBase<TElement>.Clone()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Clone.htm))  
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
[GetRow](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement_GetRow.htm)|
Метод для получения строки по ее номеру  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Insert](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Insert.htm)|
Данный метод недоступен для текущего типа  
(Переопределяет
[ElementBase<TElement>.Insert()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Insert.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Move.htm)|
Производит перемещение всех элементов данного Worksheet, начиная с moveFrom
строки (не включая ее) на moveBy  
[ParseElement](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement_ParseElement.htm)|
Метод для получения основных данных из элемента Worksheet  
(Переопределяет
[ElementBase<TElement>.ParseElement()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_ParseElement.htm))  
[Remove](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Remove.htm)|
Удаление элемента типа Worksheet недоступно  
(Переопределяет
[ElementBase<TElement>.Remove()](M_Tessa_Extensions_Default_Server_Cards_ElementBase_1_Remove.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Update](M_Tessa_Extensions_Default_Server_Cards_WorksheetElement_Update.htm)|
Производит обновление позиций всех строк, объединенных ячеек и гиперссылок в
текущем Worksheet  
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
