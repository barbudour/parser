# HandlerTypes - класс
Виды обработчиков
## __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class HandlerTypes
VB __Копировать
     Public NotInheritable Class HandlerTypes
C++ __Копировать
     public ref class HandlerTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type HandlerTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ HandlerTypes
##  __Поля
[ApplicationServiceClient](F_Tessa_Host_HandlerTypes_ApplicationServiceClient.htm)|
Хостинг WCF-клиента IApplicationServiceLegacy, который поднимается по
инициативе менеджера приложений.  
---|---  
[AppManagerServiceClient](F_Tessa_Host_HandlerTypes_AppManagerServiceClient.htm)|
Хостинг WCF-клиента IApplicationManagerService, который поднимается по
инициативе менеджера приложений.  
[AppManagerServiceHost](F_Tessa_Host_HandlerTypes_AppManagerServiceHost.htm)|
Хостинг WCF-сервиса IApplicationManagerService, который поднимается по
инициативе клиентского приложения.  
[ClientAppServiceClient](F_Tessa_Host_HandlerTypes_ClientAppServiceClient.htm)|
Хостинг WCF-клиента ITessaApplicationService, который поднимается по
инициативе клиентского приложения.  
[ClientAppServiceHost](F_Tessa_Host_HandlerTypes_ClientAppServiceHost.htm)|
Хостинг WCF-сервиса ITessaApplicationService, который поднимается по
инициативе менеджера приложений.  
[Eds](F_Tessa_Host_HandlerTypes_Eds.htm)|  Тип обработчика для подписания и
проверки подписи ЭП.  
[Preview](F_Tessa_Host_HandlerTypes_Preview.htm)|  Тип обработчика для
предварительного просмотра.  
[Scan](F_Tessa_Host_HandlerTypes_Scan.htm)|  Тип обработчика для сканирования
файлов.  
## __См. также
#### Ссылки
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
