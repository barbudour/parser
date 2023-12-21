# IPipeRouteFactory - интерфейс
Фабрика объектов, используемых для маршрутизации и обработки сообщений,
полученных по каналу.
## __Definition
 **Пространство имён:** [Tessa.Platform.Pipes](N_Tessa_Platform_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPipeRouteFactory
VB __Копировать
     Public Interface IPipeRouteFactory
C++ __Копировать
     public interface class IPipeRouteFactory
F# __Копировать
     type IPipeRouteFactory = interface end
##  __Методы
[CreateMethodHandler](M_Tessa_Platform_Pipes_IPipeRouteFactory_CreateMethodHandler.htm)|
Создаёт объект, выполняющий обработку сообщений, полученных по каналу.  
---|---  
[CreateServiceRouter](M_Tessa_Platform_Pipes_IPipeRouteFactory_CreateServiceRouter.htm)|
Создаёт объект, выполняющий маршрутизацию сообщений, полученных по каналу.  
## __Методы расширения
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
##  __См. также
#### Ссылки
[Tessa.Platform.Pipes - пространство имён](N_Tessa_Platform_Pipes.htm)
