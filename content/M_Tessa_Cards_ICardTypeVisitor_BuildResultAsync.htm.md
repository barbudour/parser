# ICardTypeVisitor.BuildResultAsync - метод
Возвращает результат валидации, полученный посредством посещения объектов типа
карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<ValidationResult> BuildResultAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function BuildResultAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ValidationResult)
C++ __Копировать
     ValueTask<ValidationResult^> BuildResultAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract BuildResultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат валидации, полученный посредством посещения объектов типа карточки.
##  __См. также
#### Ссылки
[ICardTypeVisitor - ](T_Tessa_Cards_ICardTypeVisitor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
