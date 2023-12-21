# PlatformFileExtension - конструктор
Инициализирует новый экземпляр класса
[PlatformFileExtension](T_Tessa_Extensions_Platform_Client_Files_PlatformFileExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Files](N_Tessa_Extensions_Platform_Client_Files.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public PlatformFileExtension(
    	ICardStreamClientRepository cardStreamRepository,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDialogService dialogService,
    	ICAdESManager edsManager,
    	IEDSCertificateProvider edsCertificateProvider,
    	IScanFileDialogSettingsFactory settingsFactory,
    	ICardCache cardCache,
    	IFileSignatureExporter signatureExporter,
    	IProcessNameResolver processNameResolver
    )
VB __Копировать
     Public Sub New ( 
    	cardStreamRepository As ICardStreamClientRepository,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	dialogService As IDialogService,
    	edsManager As ICAdESManager,
    	edsCertificateProvider As IEDSCertificateProvider,
    	settingsFactory As IScanFileDialogSettingsFactory,
    	cardCache As ICardCache,
    	signatureExporter As IFileSignatureExporter,
    	processNameResolver As IProcessNameResolver
    )
C++ __Копировать
     public:
    PlatformFileExtension(
    	ICardStreamClientRepository^ cardStreamRepository, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDialogService^ dialogService, 
    	ICAdESManager^ edsManager, 
    	IEDSCertificateProvider^ edsCertificateProvider, 
    	IScanFileDialogSettingsFactory^ settingsFactory, 
    	ICardCache^ cardCache, 
    	IFileSignatureExporter^ signatureExporter, 
    	IProcessNameResolver^ processNameResolver
    )
F# __Копировать
     new : 
            cardStreamRepository : ICardStreamClientRepository * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            dialogService : IDialogService * 
            edsManager : ICAdESManager * 
            edsCertificateProvider : IEDSCertificateProvider * 
            settingsFactory : IScanFileDialogSettingsFactory * 
            cardCache : ICardCache * 
            signatureExporter : IFileSignatureExporter * 
            processNameResolver : IProcessNameResolver -> PlatformFileExtension
#### Параметры
cardStreamRepository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
dialogService [IDialogService](T_Tessa_UI_Controls_IDialogService.htm)
edsManager [ICAdESManager](T_Tessa_Platform_EDS_ICAdESManager.htm)
edsCertificateProvider
[IEDSCertificateProvider](T_Tessa_Platform_EDS_IEDSCertificateProvider.htm)
settingsFactory
[IScanFileDialogSettingsFactory](T_Tessa_Extensions_Platform_Client_Scanning_IScanFileDialogSettingsFactory.htm)
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
signatureExporter
[IFileSignatureExporter](T_Tessa_UI_Files_IFileSignatureExporter.htm)
processNameResolver
[IProcessNameResolver](T_Tessa_Platform_IProcessNameResolver.htm)
## __См. также
#### Ссылки
[PlatformFileExtension -
](T_Tessa_Extensions_Platform_Client_Files_PlatformFileExtension.htm)
[Tessa.Extensions.Platform.Client.Files - пространство
имён](N_Tessa_Extensions_Platform_Client_Files.htm)
