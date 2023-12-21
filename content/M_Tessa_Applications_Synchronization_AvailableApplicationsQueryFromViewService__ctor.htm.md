# AvailableApplicationsQueryFromViewService - конструктор
Initializes a new instance of the
[AvailableApplicationsQueryFromViewService](T_Tessa_Applications_Synchronization_AvailableApplicationsQueryFromViewService.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public AvailableApplicationsQueryFromViewService(
    	[NotNullAttribute] IViewService viewService,
    	[NotNullAttribute] ISessionController sessionController,
    	[NotNullAttribute] ApplicationPackageBuilder packageBuilder
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> viewService As IViewService,
    	<NotNullAttribute> sessionController As ISessionController,
    	<NotNullAttribute> packageBuilder As ApplicationPackageBuilder
    )
C++ __Копировать
     public:
    AvailableApplicationsQueryFromViewService(
    	[NotNullAttribute] IViewService^ viewService, 
    	[NotNullAttribute] ISessionController^ sessionController, 
    	[NotNullAttribute] ApplicationPackageBuilder^ packageBuilder
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] viewService : IViewService * 
            [<NotNullAttribute>] sessionController : ISessionController * 
            [<NotNullAttribute>] packageBuilder : ApplicationPackageBuilder -> AvailableApplicationsQueryFromViewService
#### Параметры
viewService [IViewService](T_Tessa_Views_IViewService.htm)
     Сервис представлений 
sessionController
[ISessionController](T_Tessa_Applications_ISessionController.htm)
     Управление состоянием сессии 
packageBuilder
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
##  __См. также
#### Ссылки
[AvailableApplicationsQueryFromViewService -
](T_Tessa_Applications_Synchronization_AvailableApplicationsQueryFromViewService.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
