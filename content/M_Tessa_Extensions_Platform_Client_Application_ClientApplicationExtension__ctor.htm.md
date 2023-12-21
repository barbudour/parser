# ClientApplicationExtension - конструктор
Инициализирует новый экземпляр класса
[ClientApplicationExtension](T_Tessa_Extensions_Platform_Client_Application_ClientApplicationExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Application](N_Tessa_Extensions_Platform_Client_Application.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ClientApplicationExtension(
    	[OptionalDependencyAttribute] ITessaShell shell,
    	IUserSettings userSettings,
    	ICardMetadata cardMetadata,
    	ICardRepairManager cardRepairManager,
    	ICardModelSettings cardModelSettings,
    	ICardModelSettingsManager cardModelSettingsManager,
    	IInitializationContainer initializationContainer,
    	IForumControlSettings forumControlSettings,
    	IForumControlSettingsManager forumControlSettingsManager,
    	ISettingsProvider settingsProvider,
    	IFileContentOptions fileContentOptions,
    	IForumServerSettings forumServerSettings
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> shell As ITessaShell,
    	userSettings As IUserSettings,
    	cardMetadata As ICardMetadata,
    	cardRepairManager As ICardRepairManager,
    	cardModelSettings As ICardModelSettings,
    	cardModelSettingsManager As ICardModelSettingsManager,
    	initializationContainer As IInitializationContainer,
    	forumControlSettings As IForumControlSettings,
    	forumControlSettingsManager As IForumControlSettingsManager,
    	settingsProvider As ISettingsProvider,
    	fileContentOptions As IFileContentOptions,
    	forumServerSettings As IForumServerSettings
    )
C++ __Копировать
     public:
    ClientApplicationExtension(
    	[OptionalDependencyAttribute] ITessaShell^ shell, 
    	IUserSettings^ userSettings, 
    	ICardMetadata^ cardMetadata, 
    	ICardRepairManager^ cardRepairManager, 
    	ICardModelSettings^ cardModelSettings, 
    	ICardModelSettingsManager^ cardModelSettingsManager, 
    	IInitializationContainer^ initializationContainer, 
    	IForumControlSettings^ forumControlSettings, 
    	IForumControlSettingsManager^ forumControlSettingsManager, 
    	ISettingsProvider^ settingsProvider, 
    	IFileContentOptions^ fileContentOptions, 
    	IForumServerSettings^ forumServerSettings
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] shell : ITessaShell * 
            userSettings : IUserSettings * 
            cardMetadata : ICardMetadata * 
            cardRepairManager : ICardRepairManager * 
            cardModelSettings : ICardModelSettings * 
            cardModelSettingsManager : ICardModelSettingsManager * 
            initializationContainer : IInitializationContainer * 
            forumControlSettings : IForumControlSettings * 
            forumControlSettingsManager : IForumControlSettingsManager * 
            settingsProvider : ISettingsProvider * 
            fileContentOptions : IFileContentOptions * 
            forumServerSettings : IForumServerSettings -> ClientApplicationExtension
#### Параметры
shell [ITessaShell](T_Tessa_UI_Windows_ITessaShell.htm)
userSettings [IUserSettings](T_Tessa_UI_IUserSettings.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
cardModelSettings [ICardModelSettings](T_Tessa_Cards_ICardModelSettings.htm)
cardModelSettingsManager
[ICardModelSettingsManager](T_Tessa_UI_Cards_ICardModelSettingsManager.htm)
initializationContainer
[IInitializationContainer](T_Tessa_Platform_Initialization_IInitializationContainer.htm)
forumControlSettings
[IForumControlSettings](T_Tessa_Forums_IForumControlSettings.htm)
forumControlSettingsManager
[IForumControlSettingsManager](T_Tessa_Forums_IForumControlSettingsManager.htm)
settingsProvider
[ISettingsProvider](T_Tessa_Platform_Settings_ISettingsProvider.htm)
fileContentOptions
[IFileContentOptions](T_Tessa_Files_IFileContentOptions.htm)
forumServerSettings
[IForumServerSettings](T_Tessa_Forums_IForumServerSettings.htm)
## __См. также
#### Ссылки
[ClientApplicationExtension -
](T_Tessa_Extensions_Platform_Client_Application_ClientApplicationExtension.htm)
[Tessa.Extensions.Platform.Client.Application - пространство
имён](N_Tessa_Extensions_Platform_Client_Application.htm)
