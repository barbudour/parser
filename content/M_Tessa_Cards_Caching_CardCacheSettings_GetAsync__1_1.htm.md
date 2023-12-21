# CardCacheSettings.GetAsync<T>(String, Func<String, CancellationToken,
Task<T>>, CancellationToken) - метод
Возвращает настройку из кэша, или добавляет настройку в кэш, возвращённую
заданной функцией при отсутствии там настройки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<T> GetAsync<T>(
    	string key,
    	Func<string, CancellationToken, Task<T>> getValueFuncAsync,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetAsync(Of T) ( 
    	key As String,
    	getValueFuncAsync As Func(Of String, CancellationToken, Task(Of T)),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of T)
C++ __Копировать
     public:
    generic<typename T>
    virtual ValueTask<T> GetAsync(
    	String^ key, 
    	Func<String^, CancellationToken, Task<T>^>^ getValueFuncAsync, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetAsync : 
            key : string * 
            getValueFuncAsync : Func<string, CancellationToken, Task<'T>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
    override GetAsync : 
            key : string * 
            getValueFuncAsync : Func<string, CancellationToken, Task<'T>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<'T> 
#### Параметры
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, по которому требуется получить настройку из кэша.
getValueFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<T>>
     Функция, получающая ключ и создающая настройку. Выполняется асинхронно. Функция используется в случае, если настройка отсутствует в кэше, причём результат функции добавляется в кэш. 
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
#### Реализации
[ICardCacheSettings.GetAsync<T>(String, Func<String, CancellationToken,
Task<T>>,
CancellationToken)](M_Tessa_Cards_Caching_ICardCacheSettings_GetAsync__1_1.htm)  
##  __Исключения
[System.ArgumentNullException]|  Аргументы key или getValueFuncAsync равны
null.  
---|---  
[System.ArgumentOutOfRangeException]|  Аргумент key содержит строку, имеющую
большую длину, чем максимально допустимая длина
[Tessa.Cards.Caching.CardCacheHelper.MaxKeyLength].  
## __См. также
#### Ссылки
[CardCacheSettings - ](T_Tessa_Cards_Caching_CardCacheSettings.htm)
[GetAsync -
перегрузка](Overload_Tessa_Cards_Caching_CardCacheSettings_GetAsync.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
