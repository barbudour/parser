# PersonalRoleUIExtension - конструктор
Инициализирует новый экземпляр класса
[PersonalRoleUIExtension](T_Tessa_Extensions_Platform_Client_UI_PersonalRoleUIExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public PersonalRoleUIExtension(
    	IUserSettings settings,
    	ICardRepository extendedRepository,
    	ICardMetadata cardMetadata,
    	ICardRepairManager cardRepairManager,
    	INotificationUIManager notificationUIManager,
    	ISession session,
    	IUIHost uiHost,
    	ICardDialogManager cardDialogManager,
    	CreateCardModelFuncAsync createCardModelFuncAsync,
    	IRoleTypePermissionsManager permissionsManager
    )
VB __Копировать
     Public Sub New ( 
    	settings As IUserSettings,
    	extendedRepository As ICardRepository,
    	cardMetadata As ICardMetadata,
    	cardRepairManager As ICardRepairManager,
    	notificationUIManager As INotificationUIManager,
    	session As ISession,
    	uiHost As IUIHost,
    	cardDialogManager As ICardDialogManager,
    	createCardModelFuncAsync As CreateCardModelFuncAsync,
    	permissionsManager As IRoleTypePermissionsManager
    )
C++ __Копировать
     public:
    PersonalRoleUIExtension(
    	IUserSettings^ settings, 
    	ICardRepository^ extendedRepository, 
    	ICardMetadata^ cardMetadata, 
    	ICardRepairManager^ cardRepairManager, 
    	INotificationUIManager^ notificationUIManager, 
    	ISession^ session, 
    	IUIHost^ uiHost, 
    	ICardDialogManager^ cardDialogManager, 
    	CreateCardModelFuncAsync^ createCardModelFuncAsync, 
    	IRoleTypePermissionsManager^ permissionsManager
    )
F# __Копировать
     new : 
            settings : IUserSettings * 
            extendedRepository : ICardRepository * 
            cardMetadata : ICardMetadata * 
            cardRepairManager : ICardRepairManager * 
            notificationUIManager : INotificationUIManager * 
            session : ISession * 
            uiHost : IUIHost * 
            cardDialogManager : ICardDialogManager * 
            createCardModelFuncAsync : CreateCardModelFuncAsync * 
            permissionsManager : IRoleTypePermissionsManager -> PersonalRoleUIExtension
#### Параметры
settings [IUserSettings](T_Tessa_UI_IUserSettings.htm)
extendedRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
cardDialogManager
[ICardDialogManager](T_Tessa_UI_Cards_ICardDialogManager.htm)
createCardModelFuncAsync
[CreateCardModelFuncAsync](T_Tessa_UI_Cards_CreateCardModelFuncAsync.htm)
permissionsManager
[IRoleTypePermissionsManager](T_Tessa_Roles_IRoleTypePermissionsManager.htm)
## __См. также
#### Ссылки
[PersonalRoleUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_PersonalRoleUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
