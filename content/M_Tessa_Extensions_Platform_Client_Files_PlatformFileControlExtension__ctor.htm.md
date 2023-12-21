# PlatformFileControlExtension - конструктор
Инициализирует новый экземпляр класса
[PlatformFileControlExtension](T_Tessa_Extensions_Platform_Client_Files_PlatformFileControlExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Files](N_Tessa_Extensions_Platform_Client_Files.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public PlatformFileControlExtension(
    	ICardStreamClientRepository cardStreamRepository,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IScanFileDialogSettingsFactory settingsFactory,
    	IProcessNameResolver processNameResolver
    )
VB __Копировать
     Public Sub New ( 
    	cardStreamRepository As ICardStreamClientRepository,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	settingsFactory As IScanFileDialogSettingsFactory,
    	processNameResolver As IProcessNameResolver
    )
C++ __Копировать
     public:
    PlatformFileControlExtension(
    	ICardStreamClientRepository^ cardStreamRepository, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IScanFileDialogSettingsFactory^ settingsFactory, 
    	IProcessNameResolver^ processNameResolver
    )
F# __Копировать
     new : 
            cardStreamRepository : ICardStreamClientRepository * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            settingsFactory : IScanFileDialogSettingsFactory * 
            processNameResolver : IProcessNameResolver -> PlatformFileControlExtension
#### Параметры
cardStreamRepository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
settingsFactory
[IScanFileDialogSettingsFactory](T_Tessa_Extensions_Platform_Client_Scanning_IScanFileDialogSettingsFactory.htm)
processNameResolver
[IProcessNameResolver](T_Tessa_Platform_IProcessNameResolver.htm)
## __См. также
#### Ссылки
[PlatformFileControlExtension -
](T_Tessa_Extensions_Platform_Client_Files_PlatformFileControlExtension.htm)
[Tessa.Extensions.Platform.Client.Files - пространство
имён](N_Tessa_Extensions_Platform_Client_Files.htm)
