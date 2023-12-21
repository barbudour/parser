# MakeViewTaskHistoryExtensionType.CreateEditorCoreAsync - метод
Создаёт модель представления редактора метаинформации о типе расширения в типе
карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI.TaskHistory](N_Tessa_Extensions_Platform_Client_UI_TaskHistory.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask<IEditorViewModel> CreateEditorCoreAsync(
    	CardTypeExtension extension,
    	CardType type,
    	ICardUIResolver cardUIResolver,
    	ICardSchemeInfoProvider cardSchemeInfoProvider,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function CreateEditorCoreAsync ( 
    	extension As CardTypeExtension,
    	type As CardType,
    	cardUIResolver As ICardUIResolver,
    	cardSchemeInfoProvider As ICardSchemeInfoProvider,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IEditorViewModel)
C++ __Копировать
     public:
    virtual ValueTask<IEditorViewModel^> CreateEditorCoreAsync(
    	CardTypeExtension^ extension, 
    	CardType^ type, 
    	ICardUIResolver^ cardUIResolver, 
    	ICardSchemeInfoProvider^ cardSchemeInfoProvider, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract CreateEditorCoreAsync : 
            extension : CardTypeExtension * 
            type : CardType * 
            cardUIResolver : ICardUIResolver * 
            cardSchemeInfoProvider : ICardSchemeInfoProvider * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEditorViewModel> 
    override CreateEditorCoreAsync : 
            extension : CardTypeExtension * 
            type : CardType * 
            cardUIResolver : ICardUIResolver * 
            cardSchemeInfoProvider : ICardSchemeInfoProvider * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IEditorViewModel> 
#### Параметры
extension [CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)
    Редактируемая метаинформация о типе расширения в типе карточки.
type [CardType](T_Tessa_Cards_CardType.htm)
    Метаинформация о редактируемом типе карточки.
cardUIResolver [ICardUIResolver](T_Tessa_UI_Cards_ICardUIResolver.htm)
    Объект, используемый для получения объектов, используемых в автоматическом UI карточки.
cardSchemeInfoProvider
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IEditorViewModel](T_Tessa_UI_Cards_IEditorViewModel.htm)>  
Созданная модель представления редактора метаинформации о расширении в типе
карточки.
##  __См. также
#### Ссылки
[MakeViewTaskHistoryExtensionType -
](T_Tessa_Extensions_Platform_Client_UI_TaskHistory_MakeViewTaskHistoryExtensionType.htm)
[Tessa.Extensions.Platform.Client.UI.TaskHistory - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TaskHistory.htm)
