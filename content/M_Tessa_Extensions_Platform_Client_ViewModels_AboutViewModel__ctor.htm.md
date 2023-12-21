# AboutViewModel - конструктор
Инициализирует новый экземпляр класса
[AboutViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_AboutViewModel.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public AboutViewModel(
    	IApplicationDescriptor applicationDescriptor,
    	IConnectionSettings connectionSettings,
    	ISession session,
    	IExtensionAssemblyInfo assemblyInfo,
    	IConfigurationInfoProvider configurationInfoProvider,
    	INotificationUIManager notificationUIManager,
    	IApplicationParameters applicationParameters = null
    )
VB __Копировать
     Public Sub New ( 
    	applicationDescriptor As IApplicationDescriptor,
    	connectionSettings As IConnectionSettings,
    	session As ISession,
    	assemblyInfo As IExtensionAssemblyInfo,
    	configurationInfoProvider As IConfigurationInfoProvider,
    	notificationUIManager As INotificationUIManager,
    	Optional applicationParameters As IApplicationParameters = Nothing
    )
C++ __Копировать
     public:
    AboutViewModel(
    	IApplicationDescriptor^ applicationDescriptor, 
    	IConnectionSettings^ connectionSettings, 
    	ISession^ session, 
    	IExtensionAssemblyInfo^ assemblyInfo, 
    	IConfigurationInfoProvider^ configurationInfoProvider, 
    	INotificationUIManager^ notificationUIManager, 
    	IApplicationParameters^ applicationParameters = nullptr
    )
F# __Копировать
     new : 
            applicationDescriptor : IApplicationDescriptor * 
            connectionSettings : IConnectionSettings * 
            session : ISession * 
            assemblyInfo : IExtensionAssemblyInfo * 
            configurationInfoProvider : IConfigurationInfoProvider * 
            notificationUIManager : INotificationUIManager * 
            ?applicationParameters : IApplicationParameters 
    (* Defaults:
            let _applicationParameters = defaultArg applicationParameters null
    *)
    -> AboutViewModel
#### Параметры
applicationDescriptor
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
connectionSettings
[IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
assemblyInfo
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
applicationParameters
[IApplicationParameters](T_Tessa_Platform_Runtime_IApplicationParameters.htm)
(Optional)
## __См. также
#### Ссылки
[AboutViewModel -
](T_Tessa_Extensions_Platform_Client_ViewModels_AboutViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
