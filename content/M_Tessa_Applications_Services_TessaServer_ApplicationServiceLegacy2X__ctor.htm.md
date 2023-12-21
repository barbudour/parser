# ApplicationServiceLegacy2X - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationServiceLegacy2X(
    	[DependencyAttribute("ApplicationServiceLegacy2X")] Func<IApplicationService> createApplicationServiceFunc,
    	[DependencyAttribute("AvailableApplicationsQueryFromViewService")] IAvailableApplicationsQuery availableApplications
    )
VB __Копировать
     Public Sub New ( 
    	<DependencyAttribute("ApplicationServiceLegacy2X")> createApplicationServiceFunc As Func(Of IApplicationService),
    	<DependencyAttribute("AvailableApplicationsQueryFromViewService")> availableApplications As IAvailableApplicationsQuery
    )
C++ __Копировать
     public:
    ApplicationServiceLegacy2X(
    	[DependencyAttribute(L"ApplicationServiceLegacy2X")] Func<IApplicationService^>^ createApplicationServiceFunc, 
    	[DependencyAttribute(L"AvailableApplicationsQueryFromViewService")] IAvailableApplicationsQuery^ availableApplications
    )
F# __Копировать
     new : 
            [<DependencyAttribute("ApplicationServiceLegacy2X")>] createApplicationServiceFunc : Func<IApplicationService> * 
            [<DependencyAttribute("AvailableApplicationsQueryFromViewService")>] availableApplications : IAvailableApplicationsQuery -> ApplicationServiceLegacy2X
#### Параметры
createApplicationServiceFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IApplicationService](T_Tessa_Applications_Services_TessaServer_IApplicationService.htm)>
     Функция, создающая сервис для взаимодействия с сервером 2.х, к которому перенаправляются запросы. Может потребоваться освободить объект после создания. 
availableApplications
[IAvailableApplicationsQuery](T_Tessa_Applications_Synchronization_IAvailableApplicationsQuery.htm)
    Объект, обеспечивающий доступ к представлению с доступными приложениями.
##  __См. также
#### Ссылки
[ApplicationServiceLegacy2X -
](T_Tessa_Applications_Services_TessaServer_ApplicationServiceLegacy2X.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
