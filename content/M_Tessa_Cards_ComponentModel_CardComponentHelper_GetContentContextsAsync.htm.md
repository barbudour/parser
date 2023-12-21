# CardComponentHelper.GetContentContextsAsync - метод
Возвращает список контекстов, описывающий все версии для заданного списка
файлов.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<List<CardContentContext>> GetContentContextsAsync(
    	ICollection<Guid> fileIDs,
    	Guid cardID,
    	IValidationResultBuilder validationResult,
    	ICardFileVersionStrategy versionStrategy,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetContentContextsAsync ( 
    	fileIDs As ICollection(Of Guid),
    	cardID As Guid,
    	validationResult As IValidationResultBuilder,
    	versionStrategy As ICardFileVersionStrategy,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of CardContentContext))
C++ __Копировать
     public:
    static Task<List<CardContentContext^>^>^ GetContentContextsAsync(
    	ICollection<Guid>^ fileIDs, 
    	Guid cardID, 
    	IValidationResultBuilder^ validationResult, 
    	ICardFileVersionStrategy^ versionStrategy, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetContentContextsAsync : 
            fileIDs : ICollection<Guid> * 
            cardID : Guid * 
            validationResult : IValidationResultBuilder * 
            versionStrategy : ICardFileVersionStrategy * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<CardContentContext>> 
#### Параметры
fileIDs
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Список идентификаторов файлов, список контекстов которых требуется получить.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор карточки, к которой относятся все файлы из списка fileIDs. 
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Объект, выполняющий построение результата валидации.
versionStrategy
[ICardFileVersionStrategy](T_Tessa_Cards_ComponentModel_ICardFileVersionStrategy.htm)
    Стратегия, используемая для загрузки информации по версиям файлов.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[CardContentContext](T_Tessa_Cards_ComponentModel_CardContentContext.htm)>>  
Список контекстов, описывающий все версии для заданного списка файлов.
##  __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
