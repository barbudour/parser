# IApplicationCatalogStorageLoader.TryGetStorageAsync - метод
Осуществляет попытку загрузки каталога приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<IStorage> TryGetStorageAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function TryGetStorageAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IStorage)
C++ __Копировать
     ValueTask<IStorage^> TryGetStorageAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetStorageAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IStorage> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)>  
Каталога приложений или null, если загрузка не удалась
##  __См. также
#### Ссылки
[IApplicationCatalogStorageLoader -
](T_Tessa_Applications_IApplicationCatalogStorageLoader.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
