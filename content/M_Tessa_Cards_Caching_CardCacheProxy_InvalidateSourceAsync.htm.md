# CardCacheProxy.InvalidateSourceAsync - метод
Сбрасывает локальный кэш.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Caching](N_Tessa_Cards_Caching.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvalidateSourceAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvalidateSourceAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ InvalidateSourceAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member InvalidateSourceAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __Заметки
Метод выполняет сброс кэша для декорируемого объекта.
## __См. также
#### Ссылки
[CardCacheProxy - ](T_Tessa_Cards_Caching_CardCacheProxy.htm)
[Tessa.Cards.Caching - пространство имён](N_Tessa_Cards_Caching.htm)
