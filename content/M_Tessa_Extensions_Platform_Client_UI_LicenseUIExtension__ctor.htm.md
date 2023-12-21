# LicenseUIExtension - конструктор
Инициализирует новый экземпляр класса
[LicenseUIExtension](T_Tessa_Extensions_Platform_Client_UI_LicenseUIExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public LicenseUIExtension(
    	ICardRepository extendedRepository,
    	ICardMetadata cardMetadata,
    	ICardDialogManager dialogManager,
    	INotificationUIManager notificationUIManager,
    	IViewService viewService,
    	IUIHost uiHost,
    	ISession session,
    	CreateCardModelFuncAsync createCardModelFuncAsync,
    	Func<bool, RequestParameterBuilder> createParameterBuilderFunc
    )
VB __Копировать
     Public Sub New ( 
    	extendedRepository As ICardRepository,
    	cardMetadata As ICardMetadata,
    	dialogManager As ICardDialogManager,
    	notificationUIManager As INotificationUIManager,
    	viewService As IViewService,
    	uiHost As IUIHost,
    	session As ISession,
    	createCardModelFuncAsync As CreateCardModelFuncAsync,
    	createParameterBuilderFunc As Func(Of Boolean, RequestParameterBuilder)
    )
C++ __Копировать
     public:
    LicenseUIExtension(
    	ICardRepository^ extendedRepository, 
    	ICardMetadata^ cardMetadata, 
    	ICardDialogManager^ dialogManager, 
    	INotificationUIManager^ notificationUIManager, 
    	IViewService^ viewService, 
    	IUIHost^ uiHost, 
    	ISession^ session, 
    	CreateCardModelFuncAsync^ createCardModelFuncAsync, 
    	Func<bool, RequestParameterBuilder^>^ createParameterBuilderFunc
    )
F# __Копировать
     new : 
            extendedRepository : ICardRepository * 
            cardMetadata : ICardMetadata * 
            dialogManager : ICardDialogManager * 
            notificationUIManager : INotificationUIManager * 
            viewService : IViewService * 
            uiHost : IUIHost * 
            session : ISession * 
            createCardModelFuncAsync : CreateCardModelFuncAsync * 
            createParameterBuilderFunc : Func<bool, RequestParameterBuilder> -> LicenseUIExtension
#### Параметры
extendedRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
dialogManager [ICardDialogManager](T_Tessa_UI_Cards_ICardDialogManager.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
viewService [IViewService](T_Tessa_Views_IViewService.htm)
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
createCardModelFuncAsync
[CreateCardModelFuncAsync](T_Tessa_UI_Cards_CreateCardModelFuncAsync.htm)
createParameterBuilderFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean),
[RequestParameterBuilder](T_Tessa_Views_RequestParameterBuilder.htm)>
## __См. также
#### Ссылки
[LicenseUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_LicenseUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
