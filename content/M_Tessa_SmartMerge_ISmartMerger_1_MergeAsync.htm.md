# ISmartMerger<TMergeObject>.MergeAsync - метод
Логика умного слияния
## __Definition
 **Пространство имён:** [Tessa.SmartMerge](N_Tessa_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<IMergeResult<TMergeObject>> MergeAsync(
    	TMergeObject source,
    	TMergeObject destination,
    	IMergeOptions options = null,
    	ILogger logger = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function MergeAsync ( 
    	source As TMergeObject,
    	destination As TMergeObject,
    	Optional options As IMergeOptions = Nothing,
    	Optional logger As ILogger = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IMergeResult(Of TMergeObject))
C++ __Копировать
    ValueTask<IMergeResult<TMergeObject>^> MergeAsync(
    	TMergeObject source, 
    	TMergeObject destination, 
    	IMergeOptions^ options = nullptr, 
    	ILogger^ logger = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract MergeAsync : 
            source : 'TMergeObject * 
            destination : 'TMergeObject * 
            ?options : IMergeOptions * 
            ?logger : ILogger * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _options = defaultArg options null
            let _logger = defaultArg logger null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IMergeResult<'TMergeObject>> 
#### Параметры
source [TMergeObject](T_Tessa_SmartMerge_ISmartMerger_1.htm)
    Объект-источник слияния
destination [TMergeObject](T_Tessa_SmartMerge_ISmartMerger_1.htm)
    Объект-"приемник" слияния
options [IMergeOptions](T_Tessa_SmartMerge_IMergeOptions.htm) (Optional)
    Параметры слияния
logger ILogger (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IMergeResult](T_Tessa_SmartMerge_IMergeResult_1.htm)<[TMergeObject](T_Tessa_SmartMerge_ISmartMerger_1.htm)>>  
Результат слияния двух объектов
##  __См. также
#### Ссылки
[ISmartMerger<TMergeObject> \- ](T_Tessa_SmartMerge_ISmartMerger_1.htm)
[Tessa.SmartMerge - пространство имён](N_Tessa_SmartMerge.htm)
