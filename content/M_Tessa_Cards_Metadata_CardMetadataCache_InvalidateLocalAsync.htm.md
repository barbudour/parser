# CardMetadataCache.InvalidateLocalAsync - метод
Сбрасывает локальный кэш с метаинформацией по карточкам без сброса глобального
кэша. Этот метод следует использовать в случае, если очистка производится
внутри сброса другого глобального кэша, например, глобального кэша схемы.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InvalidateLocalAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InvalidateLocalAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ InvalidateLocalAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member InvalidateLocalAsync : 
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
##  __См. также
#### Ссылки
[CardMetadataCache - ](T_Tessa_Cards_Metadata_CardMetadataCache.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
