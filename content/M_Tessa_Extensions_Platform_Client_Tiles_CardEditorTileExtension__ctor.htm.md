# CardEditorTileExtension - конструктор
Инициализирует новый экземпляр класса
[CardEditorTileExtension](T_Tessa_Extensions_Platform_Client_Tiles_CardEditorTileExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public CardEditorTileExtension(
    	IUIHost uiHost,
    	ICardUIManager cardUIManager,
    	ICardManager cardManager,
    	ISession session,
    	IConfigurationInfoProvider configurationInfoProvider,
    	Func<ICardEditorModel> createEditorFunc,
    	[OptionalDependencyAttribute] IApplicationDescriptor applicationDescriptor = null
    )
VB __Копировать
     Public Sub New ( 
    	uiHost As IUIHost,
    	cardUIManager As ICardUIManager,
    	cardManager As ICardManager,
    	session As ISession,
    	configurationInfoProvider As IConfigurationInfoProvider,
    	createEditorFunc As Func(Of ICardEditorModel),
    	<OptionalDependencyAttribute> Optional applicationDescriptor As IApplicationDescriptor = Nothing
    )
C++ __Копировать
     public:
    CardEditorTileExtension(
    	IUIHost^ uiHost, 
    	ICardUIManager^ cardUIManager, 
    	ICardManager^ cardManager, 
    	ISession^ session, 
    	IConfigurationInfoProvider^ configurationInfoProvider, 
    	Func<ICardEditorModel^>^ createEditorFunc, 
    	[OptionalDependencyAttribute] IApplicationDescriptor^ applicationDescriptor = nullptr
    )
F# __Копировать
     new : 
            uiHost : IUIHost * 
            cardUIManager : ICardUIManager * 
            cardManager : ICardManager * 
            session : ISession * 
            configurationInfoProvider : IConfigurationInfoProvider * 
            createEditorFunc : Func<ICardEditorModel> * 
            [<OptionalDependencyAttribute>] ?applicationDescriptor : IApplicationDescriptor 
    (* Defaults:
            let _applicationDescriptor = defaultArg applicationDescriptor null
    *)
    -> CardEditorTileExtension
#### Параметры
uiHost [IUIHost](T_Tessa_UI_IUIHost.htm)
cardUIManager [ICardUIManager](T_Tessa_UI_Cards_ICardUIManager.htm)
cardManager [ICardManager](T_Tessa_Cards_ICardManager.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
createEditorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)>
applicationDescriptor
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
(Optional)
## __См. также
#### Ссылки
[CardEditorTileExtension -
](T_Tessa_Extensions_Platform_Client_Tiles_CardEditorTileExtension.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
