# CardSchemeSerializableObject.RepairAsync(ICardSchemeInfoProvider,
IValidationResultBuilder, CancellationToken) - метод
Метод восстанавливает объект к работоспособному состоянии в соответствии со
схемой. Этот процесс включает удаление данных из текущего объекта, которые
имеют отношение к схеме, но фактически в ней отсутствуют.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask RepairAsync(
    	ICardSchemeInfoProvider cardSchemeInfoProvider,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function RepairAsync ( 
    	cardSchemeInfoProvider As ICardSchemeInfoProvider,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    ValueTask RepairAsync(
    	ICardSchemeInfoProvider^ cardSchemeInfoProvider, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member RepairAsync : 
            cardSchemeInfoProvider : ICardSchemeInfoProvider * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cardSchemeInfoProvider
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
    Объект, предоставляющий информацию об актуальном состоянии схемы. Рекомендуется связать объект со схемой данных ISchemeService.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
     Объект, выполняющий построение результата валидации, в котором будет отражена информация об отсутствующих в схеме объектах. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSchemeSerializableObject -
](T_Tessa_Cards_CardSchemeSerializableObject.htm)
[RepairAsync -
перегрузка](Overload_Tessa_Cards_CardSchemeSerializableObject_RepairAsync.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
