# CardMetadataSchemeInfoProvider.EnsureCacheResolvedAsync - метод
Заполняет внутренний кэш объекта, если он используется.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask EnsureCacheResolvedAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function EnsureCacheResolvedAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask EnsureCacheResolvedAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract EnsureCacheResolvedAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override EnsureCacheResolvedAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[ICardSchemeInfoProvider.EnsureCacheResolvedAsync(CancellationToken)](M_Tessa_Cards_ICardSchemeInfoProvider_EnsureCacheResolvedAsync.htm)  
##  __См. также
#### Ссылки
[CardMetadataSchemeInfoProvider -
](T_Tessa_Cards_CardMetadataSchemeInfoProvider.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
