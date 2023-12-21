# DeletedUIExtension - конструктор
Инициализирует новый экземпляр класса
[DeletedUIExtension](T_Tessa_Extensions_Platform_Client_UI_DeletedUIExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public DeletedUIExtension(
    	ICardRepository cardRepository,
    	ICardRepairManager cardRepairManager,
    	ISession session,
    	IUIHost uiHost,
    	INotificationUIManager notificationUIManager,
    	Func<ICardEditorModel> createEditorFunc
    )
VB __Копировать
     Public Sub New ( 
    	cardRepository As ICardRepository,
    	cardRepairManager As ICardRepairManager,
    	session As ISession,
    	uiHost As IUIHost,
    	notificationUIManager As INotificationUIManager,
    	createEditorFunc As Func(Of ICardEditorModel)
    )
C++ __Копировать
     public:
    DeletedUIExtension(
    	ICardRepository^ cardRepository, 
    	ICardRepairManager^ cardRepairManager, 
    	ISession^ session, 
    	IUIHost^ uiHost, 
    	INotificationUIManager^ notificationUIManager, 
    	Func<ICardEditorModel^>^ createEditorFunc
    )
F# __Копировать
     new : 
            cardRepository : ICardRepository * 
            cardRepairManager : ICardRepairManager * 
            session : ISession * 
            uiHost : IUIHost * 
            notificationUIManager : INotificationUIManager * 
            createEditorFunc : Func<ICardEditorModel> -> DeletedUIExtension
#### Параметры
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
createEditorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)>
## __См. также
#### Ссылки
[DeletedUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_DeletedUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
