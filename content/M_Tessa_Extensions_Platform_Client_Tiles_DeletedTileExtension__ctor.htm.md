# DeletedTileExtension - конструктор
Инициализирует новый экземпляр класса
[DeletedTileExtension](T_Tessa_Extensions_Platform_Client_Tiles_DeletedTileExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public DeletedTileExtension(
    	Func<ICardEditorModel> createEditorFunc,
    	ICardRepository cardRepository,
    	ICardRepairManager cardRepairManager,
    	INotificationUIManager notificationUIManager,
    	ISession session,
    	IUIHost uiHost
    )
VB __Копировать
     Public Sub New ( 
    	createEditorFunc As Func(Of ICardEditorModel),
    	cardRepository As ICardRepository,
    	cardRepairManager As ICardRepairManager,
    	notificationUIManager As INotificationUIManager,
    	session As ISession,
    	uiHost As IUIHost
    )
C++ __Копировать
     public:
    DeletedTileExtension(
    	Func<ICardEditorModel^>^ createEditorFunc, 
    	ICardRepository^ cardRepository, 
    	ICardRepairManager^ cardRepairManager, 
    	INotificationUIManager^ notificationUIManager, 
    	ISession^ session, 
    	IUIHost^ uiHost
    )
F# __Копировать
     new : 
            createEditorFunc : Func<ICardEditorModel> * 
            cardRepository : ICardRepository * 
            cardRepairManager : ICardRepairManager * 
            notificationUIManager : INotificationUIManager * 
            session : ISession * 
            uiHost : IUIHost -> DeletedTileExtension
#### Параметры
createEditorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)>
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardRepairManager [ICardRepairManager](T_Tessa_Cards_ICardRepairManager.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
## __См. также
#### Ссылки
[DeletedTileExtension -
](T_Tessa_Extensions_Platform_Client_Tiles_DeletedTileExtension.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
