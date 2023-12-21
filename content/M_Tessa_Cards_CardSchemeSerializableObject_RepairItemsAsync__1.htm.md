# CardSchemeSerializableObject.RepairItemsAsync<T> \- метод
Метод восстанавливает каждый их объектов, содержащихся в коллекции, к
работоспособному состоянии в соответствии со схемой. Этот процесс включает
удаление данных из таких объектов, которые имеют отношение к схеме, но
фактически в ней отсутствуют. Сами объекты при этом не удаляются.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected static ValueTask RepairItemsAsync<T>(
    	IEnumerable<T> items,
    	ICardSchemeInfoProvider cardSchemeInfoProvider,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
    where T : CardSchemeSerializableObject
VB __Копировать
     Protected Shared Function RepairItemsAsync(Of T As CardSchemeSerializableObject) ( 
    	items As IEnumerable(Of T),
    	cardSchemeInfoProvider As ICardSchemeInfoProvider,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    generic<typename T>
    where T : CardSchemeSerializableObject
    static ValueTask RepairItemsAsync(
    	IEnumerable<T>^ items, 
    	ICardSchemeInfoProvider^ cardSchemeInfoProvider, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member RepairItemsAsync : 
            items : IEnumerable<'T> * 
            cardSchemeInfoProvider : ICardSchemeInfoProvider * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask  when 'T : CardSchemeSerializableObject
#### Параметры
items
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>
     Коллекция, содержащая проверяемые объекты, или null, если объекты для проверки отсутствуют. 
cardSchemeInfoProvider
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
    Объект, предоставляющий информацию об актуальном состоянии схемы.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Объект, выполняющий построение результата валидации, в котором будет отражена информация об отсутствующих в схеме объектах. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
T
    Тип проверяемых объектов.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardSchemeSerializableObject -
](T_Tessa_Cards_CardSchemeSerializableObject.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
