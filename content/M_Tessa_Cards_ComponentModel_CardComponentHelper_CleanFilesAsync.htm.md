# CardComponentHelper.CleanFilesAsync - метод
Очищает место, отведённое для контента файла. Метод вызывается перед удалением
файла.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task CleanFilesAsync(
    	Object validationObject,
    	Guid cardID,
    	IEnumerable<Guid> fileIDs,
    	IValidationResultBuilder validationResult,
    	ICardContentStrategy contentStrategy,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function CleanFilesAsync ( 
    	validationObject As Object,
    	cardID As Guid,
    	fileIDs As IEnumerable(Of Guid),
    	validationResult As IValidationResultBuilder,
    	contentStrategy As ICardContentStrategy,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ CleanFilesAsync(
    	Object^ validationObject, 
    	Guid cardID, 
    	IEnumerable<Guid>^ fileIDs, 
    	IValidationResultBuilder^ validationResult, 
    	ICardContentStrategy^ contentStrategy, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member CleanFilesAsync : 
            validationObject : Object * 
            cardID : Guid * 
            fileIDs : IEnumerable<Guid> * 
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
    Идентификатор карточки, место для контента файла которой требуется очистить.
fileIDs
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Идентификатор файла, место для контента которого требуется очистить.
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
