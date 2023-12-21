# IApplicationModel.LaunchAsync - метод
Вызывает запуск приложения
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task LaunchAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function LaunchAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ LaunchAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract LaunchAsync : 
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
[IApplicationModel - ](T_Tessa_Applications_IApplicationModel.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
