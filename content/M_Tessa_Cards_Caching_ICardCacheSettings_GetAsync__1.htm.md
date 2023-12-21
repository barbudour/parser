# ICardCacheSettings.GetAsync<T>(String, Func<String, T>, CancellationToken) -
метод
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<T> GetAsync<T>(
    	string key,
    	Func<string, T> getValueFunc,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetAsync(Of T) ( 
    	key As String,
    	getValueFunc As Func(Of String, T),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of T)
C++ __Копировать
     generic<typename T>
    ValueTask<T> GetAsync(
    	String^ key, 
    	Func<String^, T>^ getValueFunc, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetAsync : 
            key : string * 
            getValueFunc : Func<string, 'T> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому требуется получить настройку из кэша.
getValueFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
T>
     Функция, получающая ключ и создающая настройку. Функция используется в случае, если настройка отсутствует в кэше, причём результат функции добавляется в кэш. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Параметры типа
T
    Тип настройки, возвращаемой из кэша.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<T>  
Настройка, полученная из кэша или созданная заданной функцией.
##  __Исключения
[System.ArgumentNullException]|  Аргументы key или getValueFunc равны null.  
---|---  
[System.ArgumentOutOfRangeException]|  Аргумент key содержит строку, имеющую
большую длину, чем максимально допустимая длина
[Tessa.Cards.Caching.CardCacheHelper.MaxKeyLength].  
## __См. также
#### Ссылки
[ICardCacheSettings - ](T_Tessa_Cards_Caching_ICardCacheSettings.htm)
[GetAsync -
перегрузка](Overload_Tessa_Cards_Caching_ICardCacheSettings_GetAsync.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
