# ApplicationServiceBinaryClient - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationServiceBinaryClient(
    	IWebProxyFactory proxies,
    	[DependencyAttribute("AvailableApplicationsQueryFromViewService")] IAvailableApplicationsQuery availableApplications
    )
VB __Копировать
     Public Sub New ( 
    	proxies As IWebProxyFactory,
    	<DependencyAttribute("AvailableApplicationsQueryFromViewService")> availableApplications As IAvailableApplicationsQuery
    )
C++ __Копировать
     public:
    ApplicationServiceBinaryClient(
    	IWebProxyFactory^ proxies, 
    	[DependencyAttribute(L"AvailableApplicationsQueryFromViewService")] IAvailableApplicationsQuery^ availableApplications
    )
F# __Копировать
     new : 
            proxies : IWebProxyFactory * 
            [<DependencyAttribute("AvailableApplicationsQueryFromViewService")>] availableApplications : IAvailableApplicationsQuery -> ApplicationServiceBinaryClient
#### Параметры
proxies [IWebProxyFactory](T_Tessa_Platform_Runtime_IWebProxyFactory.htm)
    Фабрики прокси-объектов для обращения к веб-сервису.
availableApplications
[IAvailableApplicationsQuery](T_Tessa_Applications_Synchronization_IAvailableApplicationsQuery.htm)
    Объект, обеспечивающий доступ к представлению с доступными приложениями.
##  __См. также
#### Ссылки
[ApplicationServiceBinaryClient -
](T_Tessa_Applications_Services_TessaServer_ApplicationServiceBinaryClient.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
