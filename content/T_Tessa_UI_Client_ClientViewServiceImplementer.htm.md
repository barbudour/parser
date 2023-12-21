# ClientViewServiceImplementer - класс
Клиентская реализация сервиса представлений
## __Definition
 **Пространство имён:** [Tessa.UI.Client](N_Tessa_UI_Client.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ClientViewServiceImplementer : IViewServiceImplementer, 
    	IViewServiceInitializer
VB __Копировать
     Public NotInheritable Class ClientViewServiceImplementer
    	Implements IViewServiceImplementer, IViewServiceInitializer
C++ __Копировать
     public ref class ClientViewServiceImplementer sealed : IViewServiceImplementer, 
    	IViewServiceInitializer
F# __Копировать
     [<SealedAttribute>]
    type ClientViewServiceImplementer = 
        class
            interface IViewServiceImplementer
            interface IViewServiceInitializer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ClientViewServiceImplementer
Implements
    [IViewServiceImplementer](T_Tessa_Views_IViewServiceImplementer.htm), [IViewServiceInitializer](T_Tessa_Views_IViewServiceInitializer.htm)
##  __Конструкторы
[ClientViewServiceImplementer](M_Tessa_UI_Client_ClientViewServiceImplementer__ctor.htm)|
Initializes a new instance of the ClientViewServiceImplementer class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
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
[GetAllViewsAsync](M_Tessa_UI_Client_ClientViewServiceImplementer_GetAllViewsAsync.htm)|
Возвращает список представлений [ITessaView](T_Tessa_Views_ITessaView.htm).  
[GetByNameAsync](M_Tessa_UI_Client_ClientViewServiceImplementer_GetByNameAsync.htm)|
Возвращает представление заданное по имени viewName  
[GetByNamesAsync](M_Tessa_UI_Client_ClientViewServiceImplementer_GetByNamesAsync.htm)|
Возвращает список представлений заданных именами в списке viewsNames  
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
[Tessa.UI.Client - пространство имён](N_Tessa_UI_Client.htm)
