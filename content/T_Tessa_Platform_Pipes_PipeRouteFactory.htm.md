# PipeRouteFactory - класс
Фабрика объектов, используемых для маршрутизации и обработки сообщений,
полученных по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class PipeRouteFactory : IPipeRouteFactory
VB __Копировать
     Public Class PipeRouteFactory
    	Implements IPipeRouteFactory
C++ __Копировать
     public ref class PipeRouteFactory : IPipeRouteFactory
F# __Копировать
     type PipeRouteFactory = 
        class
            interface IPipeRouteFactory
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PipeRouteFactory
Implements
    [IPipeRouteFactory](T_Tessa_Platform_Pipes_IPipeRouteFactory.htm)
##  __Заметки
Наследники класса могут переопределить методы создания объектов.
## __Конструкторы
[PipeRouteFactory](M_Tessa_Platform_Pipes_PipeRouteFactory__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[CreateMethodHandlerFunc](P_Tessa_Platform_Pipes_PipeRouteFactory_CreateMethodHandlerFunc.htm)|
Функция, выполняющая создание объекта
[IPipeMethodHandler](T_Tessa_Platform_Pipes_IPipeMethodHandler.htm).  
---|---  
[CreateServiceRouterFunc](P_Tessa_Platform_Pipes_PipeRouteFactory_CreateServiceRouterFunc.htm)|
Функция, выполняющая создание объекта
[IPipeServiceRouter](T_Tessa_Platform_Pipes_IPipeServiceRouter.htm).  
## __Методы
[CreateMethodHandler](M_Tessa_Platform_Pipes_PipeRouteFactory_CreateMethodHandler.htm)|
Создаёт объект, выполняющий обработку сообщений, полученных по каналу.  
---|---  
[CreateServiceRouter](M_Tessa_Platform_Pipes_PipeRouteFactory_CreateServiceRouter.htm)|
Создаёт объект, выполняющий маршрутизацию сообщений, полученных по каналу.  
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
[CreateApplicationsServiceRouter](M_Tessa_Applications_Pipes_ApplicationsPipesExtensions_CreateApplicationsServiceRouter.htm)|  
(Определяется
[ApplicationsPipesExtensions](T_Tessa_Applications_Pipes_ApplicationsPipesExtensions.htm))  
---|---  
[CreateHostEdsServiceRouter](M_Tessa_Host_EDS_HostEdsExtensions_CreateHostEdsServiceRouter.htm)|  
(Определяется [HostEdsExtensions](T_Tessa_Host_EDS_HostEdsExtensions.htm))  
[CreateHostPreviewServiceRouter](M_Tessa_PreviewHandlers_PreviewHandlersExtensions_CreateHostPreviewServiceRouter.htm)|  
(Определяется
[PreviewHandlersExtensions](T_Tessa_PreviewHandlers_PreviewHandlersExtensions.htm))  
[CreateHostScanningServiceRouter](M_Tessa_Host_ScanExtensions_CreateHostScanningServiceRouter.htm)|  
(Определяется [ScanExtensions](T_Tessa_Host_ScanExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
