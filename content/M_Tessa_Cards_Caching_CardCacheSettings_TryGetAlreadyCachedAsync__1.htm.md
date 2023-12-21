# CardCacheSettings.TryGetAlreadyCachedAsync<T> \- метод
Возвращает настройку из кэша по заданному ключу или null, если настройка
отсутствует в кэше.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<T> TryGetAlreadyCachedAsync<T>(
    	string key,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetAlreadyCachedAsync(Of T) ( 
    	key As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of T)
C++ __Копировать
     public:
    generic<typename T>
    virtual ValueTask<T> TryGetAlreadyCachedAsync(
    	String^ key, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetAlreadyCachedAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
    override TryGetAlreadyCachedAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому требуется вернуть настройку из кэша.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
T
    Тип настройки, возвращаемой из кэша.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<T>  
Настройка из кэша по заданному ключу или null, если настройка отсутствует в
кэше.
#### Реализации
[ICardCacheSettings.TryGetAlreadyCachedAsync<T>(String,
CancellationToken)](M_Tessa_Cards_Caching_ICardCacheSettings_TryGetAlreadyCachedAsync__1.htm)  
##  __Исключения
[System.ArgumentNullException]|  Аргумент key равен null.  
---|---  
[System.ArgumentOutOfRangeException]|  Аргумент key содержит строку, имеющую
большую длину, чем максимально допустимая длина
[Tessa.Cards.Caching.CardCacheHelper.MaxKeyLength].  
## __См. также
#### Ссылки
[CardCacheSettings - ](T_Tessa_Cards_Caching_CardCacheSettings.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
