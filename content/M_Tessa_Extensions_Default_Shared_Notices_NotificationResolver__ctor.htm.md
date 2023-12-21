# NotificationResolver - конструктор
Инициализирует новый экземпляр класса
[NotificationResolver](T_Tessa_Extensions_Default_Shared_Notices_NotificationResolver.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public NotificationResolver(
    	IMailService mailService,
    	IMailService mailServiceWithoutTransaction,
    	IDbScope dbScope,
    	ISession session,
    	ICardCache cardCache,
    	IUnityContainer unityContainer,
    	ILicenseManager licenseManager
    )
VB __Копировать
     Public Sub New ( 
    	mailService As IMailService,
    	mailServiceWithoutTransaction As IMailService,
    	dbScope As IDbScope,
    	session As ISession,
    	cardCache As ICardCache,
    	unityContainer As IUnityContainer,
    	licenseManager As ILicenseManager
    )
C++ __Копировать
     public:
    NotificationResolver(
    	IMailService^ mailService, 
    	IMailService^ mailServiceWithoutTransaction, 
    	IDbScope^ dbScope, 
    	ISession^ session, 
    	ICardCache^ cardCache, 
    	IUnityContainer^ unityContainer, 
    	ILicenseManager^ licenseManager
    )
F# __Копировать
     new : 
            mailService : IMailService * 
            mailServiceWithoutTransaction : IMailService * 
            dbScope : IDbScope * 
            session : ISession * 
            cardCache : ICardCache * 
            unityContainer : IUnityContainer * 
            licenseManager : ILicenseManager -> NotificationResolver
#### Параметры
mailService [IMailService](T_Tessa_Notices_IMailService.htm)
mailServiceWithoutTransaction [IMailService](T_Tessa_Notices_IMailService.htm)
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
unityContainer IUnityContainer
licenseManager
[ILicenseManager](T_Tessa_Platform_Licensing_ILicenseManager.htm)
## __См. также
#### Ссылки
[NotificationResolver -
](T_Tessa_Extensions_Default_Shared_Notices_NotificationResolver.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
