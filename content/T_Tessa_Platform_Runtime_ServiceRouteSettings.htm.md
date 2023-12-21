# ServiceRouteSettings - класс
Настройки маршрута для взаимодействия с веб-сервисами на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ServiceRouteSettings : IServiceRouteSettings
VB __Копировать
     Public NotInheritable Class ServiceRouteSettings
    	Implements IServiceRouteSettings
C++ __Копировать
     public ref class ServiceRouteSettings sealed : IServiceRouteSettings
F# __Копировать
     [<SealedAttribute>]
    type ServiceRouteSettings = 
        class
            interface IServiceRouteSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ServiceRouteSettings
Implements
    [IServiceRouteSettings](T_Tessa_Platform_Runtime_IServiceRouteSettings.htm)
##  __Конструкторы
[ServiceRouteSettings](M_Tessa_Platform_Runtime_ServiceRouteSettings__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[ActiveRoute](P_Tessa_Platform_Runtime_ServiceRouteSettings_ActiveRoute.htm)|
Текущий активный маршрут, по которому клиент подключается к веб-сервисам. По
умолчанию равен [ServiceRoute.Default].  
---|---  
[Info](P_Tessa_Platform_Runtime_ServiceRouteSettings_Info.htm)|
Дополнительная информация для маршрутизации, которая может использоваться в
реализациях интерфейсов сервисов.  
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
[GetSupportedRoutes](M_Tessa_Platform_Runtime_ServiceRouteSettings_GetSupportedRoutes.htm)|
Возвращает коллекцию маршрутов, которые поддерживаются текущей конфигурацией
сервера.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsRouteSupported](M_Tessa_Platform_Runtime_ServiceRouteSettings_IsRouteSupported.htm)|
Возвращает признак того, что заданный маршрут поддерживается текущей
конфигурацией сервера.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetRouteSupported](M_Tessa_Platform_Runtime_ServiceRouteSettings_SetRouteSupported.htm)|
Устанавливает признак того, что заданный маршрут поддерживается текущей
конфигурацией сервера.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
