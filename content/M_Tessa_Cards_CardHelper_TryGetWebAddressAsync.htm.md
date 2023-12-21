# CardHelper.TryGetWebAddressAsync - метод
Возвращает базовый адрес веб-клиента или null, если адрес не удалось получить.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<string> TryGetWebAddressAsync(
    	ICardCache cardCache,
    	bool normalize = true,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetWebAddressAsync ( 
    	cardCache As ICardCache,
    	Optional normalize As Boolean = true,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    static ValueTask<String^> TryGetWebAddressAsync(
    	ICardCache^ cardCache, 
    	bool normalize = true, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetWebAddressAsync : 
            cardCache : ICardCache * 
            ?normalize : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _normalize = defaultArg normalize true
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Кэш с карточками настроек.
normalize [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что возвращаемый адрес веб-клиента нормализуется.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Базовый адрес веб-клиента или null, если адрес не удалось получить.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
