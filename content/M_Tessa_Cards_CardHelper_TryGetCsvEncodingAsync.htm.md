# CardHelper.TryGetCsvEncodingAsync - метод
Возвращает кодировку для формирования файлов csv
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<string> TryGetCsvEncodingAsync(
    	ICardCache cardCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetCsvEncodingAsync ( 
    	cardCache As ICardCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    static ValueTask<String^> TryGetCsvEncodingAsync(
    	ICardCache^ cardCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetCsvEncodingAsync : 
            cardCache : ICardCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Кэш с карточками настроек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Кодировка для файлов csv или null, если кодировку не удалось получить.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
