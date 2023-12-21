# ICardCacheSettings.ContainsAsync - метод
Возвращает признак того, что настройка доступна в кэше по заданному ключу.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<bool> ContainsAsync(
    	string key,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function ContainsAsync ( 
    	key As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     ValueTask<bool> ContainsAsync(
    	String^ key, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ContainsAsync : 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, для которого требуется проверить наличие настройки в кэше.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если настройка доступно в кэше по заданному ключу; false в противном
случае.
## __Исключения
[System.ArgumentNullException]|  Аргумент key равен null.  
---|---  
[System.ArgumentOutOfRangeException]|  Аргумент key содержит строку, имеющую
большую длину, чем максимально допустимая длина
[Tessa.Cards.Caching.CardCacheHelper.MaxKeyLength].  
## __См. также
#### Ссылки
[ICardCacheSettings - ](T_Tessa_Cards_Caching_ICardCacheSettings.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
