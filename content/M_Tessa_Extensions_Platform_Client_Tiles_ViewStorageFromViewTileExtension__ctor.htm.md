# ViewStorageFromViewTileExtension - конструктор
Инициализирует новый экземпляр класса
[ViewStorageFromViewTileExtension](T_Tessa_Extensions_Platform_Client_Tiles_ViewStorageFromViewTileExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Tiles](N_Tessa_Extensions_Platform_Client_Tiles.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ViewStorageFromViewTileExtension(
    	Func<ICardEditorModel> createEditorFunc,
    	CreateCardModelFuncAsync createModelFuncAsync,
    	ICardRepository cardRepository,
    	ISession session,
    	IConfigurationInfoProvider configurationInfoProvider
    )
VB __Копировать
     Public Sub New ( 
    	createEditorFunc As Func(Of ICardEditorModel),
    	createModelFuncAsync As CreateCardModelFuncAsync,
    	cardRepository As ICardRepository,
    	session As ISession,
    	configurationInfoProvider As IConfigurationInfoProvider
    )
C++ __Копировать
     public:
    ViewStorageFromViewTileExtension(
    	Func<ICardEditorModel^>^ createEditorFunc, 
    	CreateCardModelFuncAsync^ createModelFuncAsync, 
    	ICardRepository^ cardRepository, 
    	ISession^ session, 
    	IConfigurationInfoProvider^ configurationInfoProvider
    )
F# __Копировать
     new : 
            createEditorFunc : Func<ICardEditorModel> * 
            createModelFuncAsync : CreateCardModelFuncAsync * 
            cardRepository : ICardRepository * 
            session : ISession * 
            configurationInfoProvider : IConfigurationInfoProvider -> ViewStorageFromViewTileExtension
#### Параметры
createEditorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)>
createModelFuncAsync
[CreateCardModelFuncAsync](T_Tessa_UI_Cards_CreateCardModelFuncAsync.htm)
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
configurationInfoProvider
[IConfigurationInfoProvider](T_Tessa_Platform_Runtime_IConfigurationInfoProvider.htm)
## __См. также
#### Ссылки
[ViewStorageFromViewTileExtension -
](T_Tessa_Extensions_Platform_Client_Tiles_ViewStorageFromViewTileExtension.htm)
[Tessa.Extensions.Platform.Client.Tiles - пространство
имён](N_Tessa_Extensions_Platform_Client_Tiles.htm)
