# NotificationContext - конструктор
Инициализирует новый экземпляр класса
[NotificationContext](T_Tessa_Extensions_Default_Shared_Notices_NotificationContext.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public NotificationContext(
    	Guid cardID,
    	Guid cardTypeID,
    	string cardDigest,
    	string webAddress,
    	IValidationResultBuilder validationResult,
    	IMailService mailService,
    	IDbScope dbScope,
    	ISession session,
    	IUnityContainer unityContainer,
    	ILicenseManager licenseManager
    )
VB __Копировать
     Public Sub New ( 
    	cardID As Guid,
    	cardTypeID As Guid,
    	cardDigest As String,
    	webAddress As String,
    	validationResult As IValidationResultBuilder,
    	mailService As IMailService,
    	dbScope As IDbScope,
    	session As ISession,
    	unityContainer As IUnityContainer,
    	licenseManager As ILicenseManager
    )
C++ __Копировать
     public:
    NotificationContext(
    	Guid cardID, 
    	Guid cardTypeID, 
    	String^ cardDigest, 
    	String^ webAddress, 
    	IValidationResultBuilder^ validationResult, 
    	IMailService^ mailService, 
    	IDbScope^ dbScope, 
    	ISession^ session, 
    	IUnityContainer^ unityContainer, 
    	ILicenseManager^ licenseManager
    )
F# __Копировать
     new : 
            cardID : Guid * 
            cardTypeID : Guid * 
            cardDigest : string * 
            webAddress : string * 
            validationResult : IValidationResultBuilder * 
            mailService : IMailService * 
            dbScope : IDbScope * 
            session : ISession * 
            unityContainer : IUnityContainer * 
            licenseManager : ILicenseManager -> NotificationContext
#### Параметры
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
cardDigest [String](https://learn.microsoft.com/dotnet/api/system.string)
webAddress [String](https://learn.microsoft.com/dotnet/api/system.string)
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
mailService [IMailService](T_Tessa_Notices_IMailService.htm)
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
unityContainer IUnityContainer
licenseManager
[ILicenseManager](T_Tessa_Platform_Licensing_ILicenseManager.htm)
## __См. также
#### Ссылки
[NotificationContext -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationContext.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
