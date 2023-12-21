# ICardCacheCollection<T>.IsAllowedAsync - метод
Возвращает признак того, что заданный ключ допустим для кэша.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<bool> IsAllowedAsync(
    	string key,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function IsAllowedAsync ( 
    	key As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     ValueTask<bool> IsAllowedAsync(
    	String^ key, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract IsAllowedAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, допустимость наличия которого в кэше проверяется.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если заданный ключ допустим для кэша; false в противном случае.
## __Исключения
[System.ArgumentNullException]|  Аргумент key равен null.  
---|---  
[System.ArgumentOutOfRangeException]|  Аргумент key содержит строку, имеющую
большую длину, чем максимально допустимая длина
[Tessa.Cards.Caching.CardCacheHelper.MaxKeyLength].  
## __См. также
#### Ссылки
[ICardCacheCollection<T> \-
](T_Tessa_Cards_Caching_ICardCacheCollection_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
