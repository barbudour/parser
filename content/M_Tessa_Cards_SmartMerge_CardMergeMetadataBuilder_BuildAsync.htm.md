# CardMergeMetadataBuilder.BuildAsync - метод
##  __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IMergeMetadata> BuildAsync(
    	IMergeContext<CardMergeOptions> mergeContext,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function BuildAsync ( 
    	mergeContext As IMergeContext(Of CardMergeOptions),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IMergeMetadata)
C++ __Копировать
     public:
    virtual ValueTask<IMergeMetadata^> BuildAsync(
    	IMergeContext<CardMergeOptions^>^ mergeContext, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract BuildAsync : 
            mergeContext : IMergeContext<CardMergeOptions> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IMergeMetadata> 
    override BuildAsync : 
            mergeContext : IMergeContext<CardMergeOptions> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IMergeMetadata> 
#### Параметры
mergeContext
[IMergeContext](T_Tessa_SmartMerge_IMergeContext_1.htm)<[CardMergeOptions](T_Tessa_Cards_SmartMerge_CardMergeOptions.htm)>
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IMergeMetadata](T_Tessa_SmartMerge_IMergeMetadata.htm)>
#### Реализации
[IMergeMetadataBuilder<TMergeOptions>.BuildAsync(IMergeContext<TMergeOptions>,
CancellationToken)](M_Tessa_SmartMerge_IMergeMetadataBuilder_1_BuildAsync.htm)  
##  __См. также
#### Ссылки
[CardMergeMetadataBuilder -
](T_Tessa_Cards_SmartMerge_CardMergeMetadataBuilder.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
