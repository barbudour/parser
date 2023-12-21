# ScanFileDialogSettings - конструктор
Инициализирует новый экземпляр класса
[ScanFileDialogSettings](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ScanFileDialogSettings(
    	IFileExtensionContextBase context,
    	string menuActionName,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDialogService dialogService,
    	INotificationUIManager notificationUIManager,
    	Func<IScanProvider> createScanProviderFunc,
    	IUnityContainer unityContainer,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	context As IFileExtensionContextBase,
    	menuActionName As String,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	dialogService As IDialogService,
    	notificationUIManager As INotificationUIManager,
    	createScanProviderFunc As Func(Of IScanProvider),
    	unityContainer As IUnityContainer,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    ScanFileDialogSettings(
    	IFileExtensionContextBase^ context, 
    	String^ menuActionName, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDialogService^ dialogService, 
    	INotificationUIManager^ notificationUIManager, 
    	Func<IScanProvider^>^ createScanProviderFunc, 
    	IUnityContainer^ unityContainer, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            context : IFileExtensionContextBase * 
            menuActionName : string * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            dialogService : IDialogService * 
            notificationUIManager : INotificationUIManager * 
            createScanProviderFunc : Func<IScanProvider> * 
            unityContainer : IUnityContainer * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ScanFileDialogSettings
#### Параметры
context
[IFileExtensionContextBase](T_Tessa_UI_Files_IFileExtensionContextBase.htm)
menuActionName [String](https://learn.microsoft.com/dotnet/api/system.string)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
dialogService [IDialogService](T_Tessa_UI_Controls_IDialogService.htm)
notificationUIManager
[INotificationUIManager](T_Tessa_UI_Notifications_INotificationUIManager.htm)
createScanProviderFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IScanProvider](T_Tessa_Extensions_Platform_Client_Scanning_IScanProvider.htm)>
unityContainer IUnityContainer
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
## __См. также
#### Ссылки
[ScanFileDialogSettings -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
