# CardCacheProxy - конструктор
Создаёт экземпляр класса с указанием декорируемого объекта и метода,
выполняемого при очистке кэша вызовом метода интерфейса
[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardCacheProxy(
    	Func<CancellationToken, ValueTask<ICardCache>> getSourceAsync,
    	Func<CardCacheInvalidationType, string, CancellationToken, Task> invalidateActionAsync = null
    )
VB __Копировать
     Public Sub New ( 
    	getSourceAsync As Func(Of CancellationToken, ValueTask(Of ICardCache)),
    	Optional invalidateActionAsync As Func(Of CardCacheInvalidationType, String, CancellationToken, Task) = Nothing
    )
C++ __Копировать
     public:
    CardCacheProxy(
    	Func<CancellationToken, ValueTask<ICardCache^>>^ getSourceAsync, 
    	Func<CardCacheInvalidationType, String^, CancellationToken, Task^>^ invalidateActionAsync = nullptr
    )
F# __Копировать
     new : 
            getSourceAsync : Func<CancellationToken, ValueTask<ICardCache>> * 
            ?invalidateActionAsync : Func<CardCacheInvalidationType, string, CancellationToken, Task> 
    (* Defaults:
            let _invalidateActionAsync = defaultArg invalidateActionAsync null
    *)
    -> CardCacheProxy
#### Параметры
getSourceAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)>>
    Функция, асинхронно возвращающая декорируемый объект, для которого создаётся прокси.
invalidateActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[CardCacheInvalidationType](T_Tessa_Cards_Caching_CardCacheInvalidationType.htm),
[String](https://learn.microsoft.com/dotnet/api/system.string),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
(Optional)
     Метод, выполняемый при сбросе кэша с заданным способом сброса и ключом (при его наличии) или null, если не требуется выполнять дополнительных действий при операциях сброса кэша. 
## __См. также
#### Ссылки
[CardCacheProxy - ](T_Tessa_Cards_Caching_CardCacheProxy.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
