# CardComponentHelper.CleanCardAsync - метод
Очищает место, отведённое для контента файлов, принадлежащих карточке.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task CleanCardAsync(
    	Object validationObject,
    	Guid cardID,
    	IValidationResultBuilder validationResult,
    	ICardContentStrategy contentStrategy,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CleanCardAsync ( 
    	validationObject As Object,
    	cardID As Guid,
    	validationResult As IValidationResultBuilder,
    	contentStrategy As ICardContentStrategy,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ CleanCardAsync(
    	Object^ validationObject, 
    	Guid cardID, 
    	IValidationResultBuilder^ validationResult, 
    	ICardContentStrategy^ contentStrategy, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CleanCardAsync : 
            validationObject : Object * 
            cardID : Guid * 
            validationResult : IValidationResultBuilder * 
            contentStrategy : ICardContentStrategy * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
validationObject
[Object](https://learn.microsoft.com/dotnet/api/system.object)
    Объект, от имени которого выполняется валидация.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, место для контента файлов которой требуется очистить.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
contentStrategy
[ICardContentStrategy](T_Tessa_Cards_ComponentModel_ICardContentStrategy.htm)
    Стратегия управления контентом файла.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
