# CardGlobalCache.InvalidateGlobalAsync - метод
Сбрасывает глобальный кэш.
## __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvalidateGlobalAsync(
    	CardCacheInvalidationType invalidationType,
    	string key,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvalidateGlobalAsync ( 
    	invalidationType As CardCacheInvalidationType,
    	key As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ InvalidateGlobalAsync(
    	CardCacheInvalidationType invalidationType, 
    	String^ key, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member InvalidateGlobalAsync : 
            invalidationType : CardCacheInvalidationType * 
            key : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
invalidationType
[CardCacheInvalidationType](T_Tessa_Cards_Caching_CardCacheInvalidationType.htm)
    Тип операции по сбросу кэша.
key [String](https://learn.microsoft.com/dotnet/api/system.string)
    Ключ, соответствующий типу операции. Для типа [Everything](T_Tessa_Cards_Caching_CardCacheInvalidationType.htm) укажите null.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardGlobalCache - ](T_Tessa_Cards_Caching_CardGlobalCache.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
