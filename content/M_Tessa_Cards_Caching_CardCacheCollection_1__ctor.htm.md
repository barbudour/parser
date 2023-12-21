# CardCacheCollection<T> \- конструктор
Создаёт экземпляр класса с указанием функции, используемой для получения
значений объектов, отсутствующих в кэше, и функции, проверяющей возможность
наличия объекта в кэше.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardCacheCollection(
    	Func<string, CancellationToken, ValueTask<CardCacheValue<T>>> getValueFuncAsync,
    	Func<string, CancellationToken, ValueTask<bool>> isAllowedFuncAsync
    )
VB __Копировать
     Public Sub New ( 
    	getValueFuncAsync As Func(Of String, CancellationToken, ValueTask(Of CardCacheValue(Of T))),
    	isAllowedFuncAsync As Func(Of String, CancellationToken, ValueTask(Of Boolean))
    )
C++ __Копировать
     public:
    CardCacheCollection(
    	Func<String^, CancellationToken, ValueTask<CardCacheValue<T>>>^ getValueFuncAsync, 
    	Func<String^, CancellationToken, ValueTask<bool>>^ isAllowedFuncAsync
    )
F# __Копировать
     new : 
            getValueFuncAsync : Func<string, CancellationToken, ValueTask<CardCacheValue<'T>>> * 
            isAllowedFuncAsync : Func<string, CancellationToken, ValueTask<bool>> -> CardCacheCollection
#### Параметры
getValueFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardCacheValue](T_Tessa_Cards_Caching_CardCacheValue_1.htm)<[T](T_Tessa_Cards_Caching_CardCacheCollection_1.htm)>>>
     Функция, используемая для получения значений объектов, отсутствующих в кэше. Функция может не проверять возможность наличия объекта в кэше, т.к. такая проверка выполняется перед вызовом функции. 
isAllowedFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>>
     Функция, проверяющая возможность наличия объекта в кэше и возвращающая true, если объект может содержаться в кэше, и false в противном случае. 
## __См. также
#### Ссылки
[CardCacheCollection<T> \- ](T_Tessa_Cards_Caching_CardCacheCollection_1.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
