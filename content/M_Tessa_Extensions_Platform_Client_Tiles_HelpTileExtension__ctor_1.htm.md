# HelpTileExtension(IExtensionAssemblyInfo, IConfigurationInfoProvider,
IApplicationDescriptor, IConnectionSettings, ISession, INotificationUIManager,
ICardCache, IApplication) - конструктор
Инициализирует новый экземпляр класса
[HelpTileExtension](T_Tessa_Extensions_Platform_Client_Tiles_HelpTileExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public HelpTileExtension(
    	IExtensionAssemblyInfo assemblyInfo,
    	IConfigurationInfoProvider configurationInfoProvider,
    	IApplicationDescriptor applicationDescriptor,
    	IConnectionSettings connectionSettings,
    	ISession session,
    	INotificationUIManager notificationUIManager,
    	ICardCache cardCache,
    	[OptionalDependencyAttribute] IApplication application = null
    )
VB __Копировать
     Public Sub New ( 
    	assemblyInfo As IExtensionAssemblyInfo,
    	configurationInfoProvider As IConfigurationInfoProvider,
    	applicationDescriptor As IApplicationDescriptor,
    	connectionSettings As IConnectionSettings,
    	session As ISession,
    	notificationUIManager As INotificationUIManager,
    	cardCache As ICardCache,
    	<OptionalDependencyAttribute> Optional application As IApplication = Nothing
    )
C++ __Копировать
     public:
    HelpTileExtension(
    	IExtensionAssemblyInfo^ assemblyInfo, 
    	IConfigurationInfoProvider^ configurationInfoProvider, 
    	IApplicationDescriptor^ applicationDescriptor, 
    	IConnectionSettings^ connectionSettings, 
    	ISession^ session, 
    	INotificationUIManager^ notificationUIManager, 
    	ICardCache^ cardCache, 
    	[OptionalDependencyAttribute] IApplication^ application = nullptr
    )
F# __Копировать
     new : 
            assemblyInfo : IExtensionAssemblyInfo * 
            configurationInfoProvider : IConfigurationInfoProvider * 
            applicationDescriptor : IApplicationDescriptor * 
            connectionSettings : IConnectionSettings * 
            session : ISession * 
            notificationUIManager : INotificationUIManager * 
            cardCache : ICardCache * 
            [<OptionalDependencyAttribute>] ?application : IApplication 
    (* Defaults:
            let _application = defaultArg application null
    *)
    -> HelpTileExtension
#### Параметры
assemblyInfo
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
applicationDescriptor
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
connectionSettings
[IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
application [IApplication](T_Tessa_Platform_Runtime_IApplication.htm)
(Optional)
## __См. также
#### Ссылки
[HelpTileExtension -
](T_Tessa_Extensions_Platform_Client_Tiles_HelpTileExtension.htm)
[HelpTileExtension -
перегрузка](Overload_Tessa_Extensions_Platform_Client_Tiles_HelpTileExtension__ctor.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
