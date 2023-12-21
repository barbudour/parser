# IApplicationCollection.RunDefaultApplicationAsync - метод
Осуществляет запуск приложения по умолчанию
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task RunDefaultApplicationAsync(
    	[CanBeNullAttribute] IApplicationContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function RunDefaultApplicationAsync ( 
    	<CanBeNullAttribute> context As IApplicationContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ RunDefaultApplicationAsync(
    	[CanBeNullAttribute] IApplicationContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract RunDefaultApplicationAsync : 
            [<CanBeNullAttribute>] context : IApplicationContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
context
[IApplicationContext](T_Tessa_Platform_Runtime_IApplicationContext.htm)
     Контекст запуска приложения 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IApplicationCollection -
](T_Tessa_Applications_Containers_IApplicationCollection.htm)
[Tessa.Applications.Containers - пространство
имён](N_Tessa_Applications_Containers.htm)
