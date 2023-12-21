# CardSmartMerger.MergeAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override ValueTask<IMergeResult<Card>> MergeAsync(
    	Card sourceCard,
    	Card destinationCard,
    	IMergeOptions options = null,
    	ILogger logger = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overrides Function MergeAsync ( 
    	sourceCard As Card,
    	destinationCard As Card,
    	Optional options As IMergeOptions = Nothing,
    	Optional logger As ILogger = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IMergeResult(Of Card))
C++ __Копировать
     public:
    virtual ValueTask<IMergeResult<Card^>^> MergeAsync(
    	Card^ sourceCard, 
    	Card^ destinationCard, 
    	IMergeOptions^ options = nullptr, 
    	ILogger^ logger = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract MergeAsync : 
            sourceCard : Card * 
            destinationCard : Card * 
            ?options : IMergeOptions * 
            ?logger : ILogger * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _options = defaultArg options null
            let _logger = defaultArg logger null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IMergeResult<Card>> 
    override MergeAsync : 
            sourceCard : Card * 
            destinationCard : Card * 
            ?options : IMergeOptions * 
            ?logger : ILogger * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _options = defaultArg options null
            let _logger = defaultArg logger null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IMergeResult<Card>> 
#### Параметры
sourceCard [Card](T_Tessa_Cards_Card.htm)
destinationCard [Card](T_Tessa_Cards_Card.htm)
options [IMergeOptions](T_Tessa_SmartMerge_IMergeOptions.htm) (Optional)
logger ILogger (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IMergeResult](T_Tessa_SmartMerge_IMergeResult_1.htm)<[Card](T_Tessa_Cards_Card.htm)>>
#### Реализации
[ISmartMerger<TMergeObject>.MergeAsync(TMergeObject, TMergeObject,
IMergeOptions, ILogger,
CancellationToken)](M_Tessa_SmartMerge_ISmartMerger_1_MergeAsync.htm)  
##  __См. также
#### Ссылки
[CardSmartMerger - ](T_Tessa_Cards_SmartMerge_CardSmartMerger.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
