# CalendarView - класс
Represents a date range view of appointments in calendar folder search
operations.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CalendarView : ViewBase
VB __Копировать
     Public NotInheritable Class CalendarView
    	Inherits ViewBase
C++ __Копировать
     public ref class CalendarView sealed : public ViewBase
F# __Копировать
     [<SealedAttribute>]
    type CalendarView = 
        class
            inherit ViewBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ViewBase](T_Tessa_Exchange_WebServices_Data_ViewBase.htm) __ CalendarView
##  __Конструкторы
[CalendarView(DateTime,
DateTime)](M_Tessa_Exchange_WebServices_Data_CalendarView__ctor.htm)|
Initializes a new instance of CalendarView.  
---|---  
[CalendarView(DateTime, DateTime,
Int32)](M_Tessa_Exchange_WebServices_Data_CalendarView__ctor_1.htm)|
Initializes a new instance of CalendarView.  
## __Свойства
[EndDate](P_Tessa_Exchange_WebServices_Data_CalendarView_EndDate.htm)|  Gets
or sets the end date.  
---|---  
[MaxItemsReturned](P_Tessa_Exchange_WebServices_Data_CalendarView_MaxItemsReturned.htm)|
The maximum number of items the search operation should return.  
[PropertySet](P_Tessa_Exchange_WebServices_Data_ViewBase_PropertySet.htm)|
Gets or sets the property set. PropertySet determines which properties will be
loaded on found items. If PropertySet is null, all first class properties are
loaded on found items.  
(Унаследован от [ViewBase](T_Tessa_Exchange_WebServices_Data_ViewBase.htm))  
[StartDate](P_Tessa_Exchange_WebServices_Data_CalendarView_StartDate.htm)|
Gets or sets the start date.  
[Traversal](P_Tessa_Exchange_WebServices_Data_CalendarView_Traversal.htm)|
Gets or sets the search traversal mode. Defaults to ItemTraversal.Shallow.  
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
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
