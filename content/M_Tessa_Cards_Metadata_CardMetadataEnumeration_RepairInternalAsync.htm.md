# CardMetadataEnumeration.RepairInternalAsync - метод
Метод восстанавливает объект к работоспособному состоянии в соответствии со
схемой. Этот процесс включает удаление данных из текущего объекта, которые
имеют отношение к схеме, но фактически в ней отсутствуют.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask RepairInternalAsync(
    	ICardSchemeInfoProvider cardSchemeInfoProvider,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function RepairInternalAsync ( 
    	cardSchemeInfoProvider As ICardSchemeInfoProvider,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask RepairInternalAsync(
    	ICardSchemeInfoProvider^ cardSchemeInfoProvider, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract RepairInternalAsync : 
            cardSchemeInfoProvider : ICardSchemeInfoProvider * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override RepairInternalAsync : 
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
##  __См. также
#### Ссылки
[CardMetadataEnumeration -
](T_Tessa_Cards_Metadata_CardMetadataEnumeration.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
