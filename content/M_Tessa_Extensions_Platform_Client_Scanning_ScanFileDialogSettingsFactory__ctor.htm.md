# ScanFileDialogSettingsFactory - конструктор
Инициализирует новый экземпляр класса
[ScanFileDialogSettingsFactory](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettingsFactory.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ScanFileDialogSettingsFactory(
    	IExtensionContainer extensionContainer,
    	IUnityContainer unityContainer,
    	IMessageProvider messageProvider,
    	IDialogService dialogService,
    	INotificationUIManager notificationUIManager,
    	ICardMetadata cardMetadata,
    	ISession session,
    	Func<IScanProvider> createScanProviderFunc
    )
VB __Копировать
     Public Sub New ( 
    	extensionContainer As IExtensionContainer,
    	unityContainer As IUnityContainer,
    	messageProvider As IMessageProvider,
    	dialogService As IDialogService,
    	notificationUIManager As INotificationUIManager,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	createScanProviderFunc As Func(Of IScanProvider)
    )
C++ __Копировать
     public:
    ScanFileDialogSettingsFactory(
    	IExtensionContainer^ extensionContainer, 
    	IUnityContainer^ unityContainer, 
    	IMessageProvider^ messageProvider, 
    	IDialogService^ dialogService, 
    	INotificationUIManager^ notificationUIManager, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	Func<IScanProvider^>^ createScanProviderFunc
    )
F# __Копировать
     new : 
            extensionContainer : IExtensionContainer * 
            unityContainer : IUnityContainer * 
            messageProvider : IMessageProvider * 
            dialogService : IDialogService * 
            notificationUIManager : INotificationUIManager * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            createScanProviderFunc : Func<IScanProvider> -> ScanFileDialogSettingsFactory
#### Параметры
extensionContainer
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
unityContainer IUnityContainer
messageProvider
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm)
dialogService [IDialogService](T_Tessa_UI_Controls_IDialogService.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
createScanProviderFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IScanProvider](T_Tessa_Extensions_Platform_Client_Scanning_IScanProvider.htm)>
## __См. также
#### Ссылки
[ScanFileDialogSettingsFactory -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettingsFactory.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
