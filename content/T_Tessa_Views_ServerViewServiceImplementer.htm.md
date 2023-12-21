# ServerViewServiceImplementer - класс
Реализатор серверной части [IViewService](T_Tessa_Views_IViewService.htm)
сервиса представлений.
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ServerViewServiceImplementer : IViewServiceImplementer
VB __Копировать
     Public NotInheritable Class ServerViewServiceImplementer
    	Implements IViewServiceImplementer
C++ __Копировать
     public ref class ServerViewServiceImplementer sealed : IViewServiceImplementer
F# __Копировать
     [<SealedAttribute>]
    type ServerViewServiceImplementer = 
        class
            interface IViewServiceImplementer
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ServerViewServiceImplementer
Implements
    [IViewServiceImplementer](T_Tessa_Views_IViewServiceImplementer.htm)
##  __Конструкторы
[ServerViewServiceImplementer](M_Tessa_Views_ServerViewServiceImplementer__ctor.htm)|
Initializes a new instance of the ServerViewServiceImplementer class.  
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
[GetAllViewsAsync](M_Tessa_Views_ServerViewServiceImplementer_GetAllViewsAsync.htm)|
Возвращает список представлений [ITessaView](T_Tessa_Views_ITessaView.htm).  
[GetByNameAsync](M_Tessa_Views_ServerViewServiceImplementer_GetByNameAsync.htm)|
Возвращает представление заданное по имени viewName  
[GetByNamesAsync](M_Tessa_Views_ServerViewServiceImplementer_GetByNamesAsync.htm)|
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
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
