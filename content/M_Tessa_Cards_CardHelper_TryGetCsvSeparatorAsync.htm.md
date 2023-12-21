# CardHelper.TryGetCsvSeparatorAsync - метод
Возвращает разделитель для формирования файлов csv. В случае если символ не
задан или при конвертации символа произошла ошибка возвращает ';' в качестве
разделителя по умолчанию
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<char> TryGetCsvSeparatorAsync(
    	ICardCache cardCache,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetCsvSeparatorAsync ( 
    	cardCache As ICardCache,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Char)
C++ __Копировать
     public:
    static ValueTask<wchar_t> TryGetCsvSeparatorAsync(
    	ICardCache^ cardCache, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetCsvSeparatorAsync : 
            cardCache : ICardCache * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<char> 
#### Параметры
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Кэш с карточками настроек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Char](https://learn.microsoft.com/dotnet/api/system.char)>  
Разделитель для файлов csv или null, если разделитель не удалось получить.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
