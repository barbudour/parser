# PlatformFileControlExtension.GenerateFileTemplateActions - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Files](N_Tessa_Extensions_Platform_Client_Files.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static IEnumerable<IMenuAction> GenerateFileTemplateActions(
    	IFileExtensionContextBase context,
    	ICardMetadata cardMetadata,
    	ISession session,
    	ICardStreamClientRepository cardStreamRepository,
    	IFile fileToReplace = null
    )
VB __Копировать
     Public Shared Function GenerateFileTemplateActions ( 
    	context As IFileExtensionContextBase,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	cardStreamRepository As ICardStreamClientRepository,
    	Optional fileToReplace As IFile = Nothing
    ) As IEnumerable(Of IMenuAction)
C++ __Копировать
     public:
    static IEnumerable<IMenuAction^>^ GenerateFileTemplateActions(
    	IFileExtensionContextBase^ context, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	ICardStreamClientRepository^ cardStreamRepository, 
    	IFile^ fileToReplace = nullptr
    )
F# __Копировать
     static member GenerateFileTemplateActions : 
            context : IFileExtensionContextBase * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            cardStreamRepository : ICardStreamClientRepository * 
            ?fileToReplace : IFile 
    (* Defaults:
            let _fileToReplace = defaultArg fileToReplace null
    *)
    -> IEnumerable<IMenuAction> 
#### Параметры
context
[IFileExtensionContextBase](T_Tessa_UI_Files_IFileExtensionContextBase.htm)
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
cardStreamRepository
[ICardStreamClientRepository](T_Tessa_Cards_ICardStreamClientRepository.htm)
fileToReplace [IFile](T_Tessa_Files_IFile.htm) (Optional)
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IMenuAction](T_Tessa_UI_Menu_IMenuAction.htm)>
##  __См. также
#### Ссылки
[PlatformFileControlExtension -
](T_Tessa_Extensions_Platform_Client_Files_PlatformFileControlExtension.htm)
[Tessa.Extensions.Platform.Client.Files - пространство
имён](N_Tessa_Extensions_Platform_Client_Files.htm)
