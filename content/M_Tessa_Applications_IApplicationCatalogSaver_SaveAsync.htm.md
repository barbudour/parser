# IApplicationCatalogSaver.SaveAsync - метод
Осуществляет сохранение каталога приложений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task SaveAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SaveAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ SaveAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SaveAsync : 
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
[IApplicationCatalogSaver -
](T_Tessa_Applications_IApplicationCatalogSaver.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
