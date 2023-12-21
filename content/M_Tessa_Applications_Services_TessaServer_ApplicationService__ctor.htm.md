# ApplicationService - конструктор
Initializes a new instance of the
[ApplicationService](T_Tessa_Applications_Services_TessaServer_ApplicationService.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationService(
    	IApplicationDownloader applicationDownloader,
    	IAvailableApplicationsQuery availableApplications
    )
VB __Копировать
     Public Sub New ( 
    	applicationDownloader As IApplicationDownloader,
    	availableApplications As IAvailableApplicationsQuery
    )
C++ __Копировать
     public:
    ApplicationService(
    	IApplicationDownloader^ applicationDownloader, 
    	IAvailableApplicationsQuery^ availableApplications
    )
F# __Копировать
     new : 
            applicationDownloader : IApplicationDownloader * 
            availableApplications : IAvailableApplicationsQuery -> ApplicationService
#### Параметры
applicationDownloader
[IApplicationDownloader](T_Tessa_Applications_Services_TessaServer_IApplicationDownloader.htm)
     Загрузчик приложения 
availableApplications
[IAvailableApplicationsQuery](T_Tessa_Applications_Synchronization_IAvailableApplicationsQuery.htm)
##  __См. также
#### Ссылки
[ApplicationService -
](T_Tessa_Applications_Services_TessaServer_ApplicationService.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
