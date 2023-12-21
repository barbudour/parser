# ApplicationLaunchingStrategy - конструктор
Инициализирует новый экземпляр класса
[ApplicationLaunchingStrategy](T_Tessa_Applications_ApplicationLaunchingStrategy.htm)
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationLaunchingStrategy(
    	[NotNullAttribute] IApplicationModel application,
    	[NotNullAttribute] GetTessaSpecialFolderDelegate getSpecialFolderFunc,
    	[NotNullAttribute] IApplicationUpdateChecker updateChecker,
    	[NotNullAttribute] IApplicationEnvironmentManager environmentManager,
    	[NotNullAttribute] IMessageProvider messageProvider,
    	[NotNullAttribute] IApplicationSynchronizer synchronizer,
    	[NotNullAttribute] ISessionController sessionController,
    	[NotNullAttribute] ISessionManager sessionManager,
    	[NotNullAttribute] Func<IStreamSynchronizationSource> streamSourceFunc,
    	[NotNullAttribute] Func<IFileSystemSynchronizationTarget> targetFunc,
    	[NotNullAttribute] IApplicationCollection applicationCollection,
    	[NotNullAttribute] ApplicationPackageBuilder packageBuilder
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> application As IApplicationModel,
    	<NotNullAttribute> getSpecialFolderFunc As GetTessaSpecialFolderDelegate,
    	<NotNullAttribute> updateChecker As IApplicationUpdateChecker,
    	<NotNullAttribute> environmentManager As IApplicationEnvironmentManager,
    	<NotNullAttribute> messageProvider As IMessageProvider,
    	<NotNullAttribute> synchronizer As IApplicationSynchronizer,
    	<NotNullAttribute> sessionController As ISessionController,
    	<NotNullAttribute> sessionManager As ISessionManager,
    	<NotNullAttribute> streamSourceFunc As Func(Of IStreamSynchronizationSource),
    	<NotNullAttribute> targetFunc As Func(Of IFileSystemSynchronizationTarget),
    	<NotNullAttribute> applicationCollection As IApplicationCollection,
    	<NotNullAttribute> packageBuilder As ApplicationPackageBuilder
    )
C++ __Копировать
     public:
    ApplicationLaunchingStrategy(
    	[NotNullAttribute] IApplicationModel^ application, 
    	[NotNullAttribute] GetTessaSpecialFolderDelegate^ getSpecialFolderFunc, 
    	[NotNullAttribute] IApplicationUpdateChecker^ updateChecker, 
    	[NotNullAttribute] IApplicationEnvironmentManager^ environmentManager, 
    	[NotNullAttribute] IMessageProvider^ messageProvider, 
    	[NotNullAttribute] IApplicationSynchronizer^ synchronizer, 
    	[NotNullAttribute] ISessionController^ sessionController, 
    	[NotNullAttribute] ISessionManager^ sessionManager, 
    	[NotNullAttribute] Func<IStreamSynchronizationSource^>^ streamSourceFunc, 
    	[NotNullAttribute] Func<IFileSystemSynchronizationTarget^>^ targetFunc, 
    	[NotNullAttribute] IApplicationCollection^ applicationCollection, 
    	[NotNullAttribute] ApplicationPackageBuilder^ packageBuilder
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] application : IApplicationModel * 
            [<NotNullAttribute>] getSpecialFolderFunc : GetTessaSpecialFolderDelegate * 
            [<NotNullAttribute>] updateChecker : IApplicationUpdateChecker * 
            [<NotNullAttribute>] environmentManager : IApplicationEnvironmentManager * 
            [<NotNullAttribute>] messageProvider : IMessageProvider * 
            [<NotNullAttribute>] synchronizer : IApplicationSynchronizer * 
            [<NotNullAttribute>] sessionController : ISessionController * 
            [<NotNullAttribute>] sessionManager : ISessionManager * 
            [<NotNullAttribute>] streamSourceFunc : Func<IStreamSynchronizationSource> * 
            [<NotNullAttribute>] targetFunc : Func<IFileSystemSynchronizationTarget> * 
            [<NotNullAttribute>] applicationCollection : IApplicationCollection * 
            [<NotNullAttribute>] packageBuilder : ApplicationPackageBuilder -> ApplicationLaunchingStrategy
#### Параметры
application [IApplicationModel](T_Tessa_Applications_IApplicationModel.htm)
getSpecialFolderFunc
[GetTessaSpecialFolderDelegate](T_Tessa_Applications_GetTessaSpecialFolderDelegate.htm)
updateChecker
[IApplicationUpdateChecker](T_Tessa_Applications_Synchronization_IApplicationUpdateChecker.htm)
environmentManager
[IApplicationEnvironmentManager](T_Tessa_Platform_Runtime_IApplicationEnvironmentManager.htm)
messageProvider
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)
synchronizer
[IApplicationSynchronizer](T_Tessa_Applications_Synchronization_IApplicationSynchronizer.htm)
sessionController
[ISessionController](T_Tessa_Applications_ISessionController.htm)
sessionManager [ISessionManager](T_Tessa_Platform_Runtime_ISessionManager.htm)
streamSourceFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IStreamSynchronizationSource](T_Tessa_Applications_Synchronization_IStreamSynchronizationSource.htm)>
targetFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IFileSystemSynchronizationTarget](T_Tessa_Applications_Synchronization_IFileSystemSynchronizationTarget.htm)>
applicationCollection
[IApplicationCollection](T_Tessa_Applications_Containers_IApplicationCollection.htm)
packageBuilder
[ApplicationPackageBuilder](T_Tessa_Applications_Package_ApplicationPackageBuilder.htm)
## __См. также
#### Ссылки
[ApplicationLaunchingStrategy -
](T_Tessa_Applications_ApplicationLaunchingStrategy.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
