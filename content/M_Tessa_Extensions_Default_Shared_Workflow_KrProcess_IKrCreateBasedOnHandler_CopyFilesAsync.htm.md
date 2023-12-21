# IKrCreateBasedOnHandler.CopyFilesAsync - метод
Выполняет копирование невиртуальных файлов из карточки baseCard в карточку
newCard.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<ValidationResult> CopyFilesAsync(
    	Card baseCard,
    	Card newCard,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function CopyFilesAsync ( 
    	baseCard As Card,
    	newCard As Card,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ValidationResult)
C++ __Копировать
     ValueTask<ValidationResult^> CopyFilesAsync(
    	Card^ baseCard, 
    	Card^ newCard, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract CopyFilesAsync : 
            baseCard : Card * 
            newCard : Card * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
#### Параметры
baseCard [Card](T_Tessa_Cards_Card.htm)
    Карточка, из которой копируются файлы.
newCard [Card](T_Tessa_Cards_Card.htm)
    Карточка, в которую копируются файлы.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Асинхронная задача.
##  __См. также
#### Ссылки
[IKrCreateBasedOnHandler -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrCreateBasedOnHandler.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
