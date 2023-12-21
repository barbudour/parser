# IApplicationManagerServiceHost.StartServiceAsync - метод
Осуществляет создание и запуск сервиса
[IApplicationManagerService](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerService.htm),
если сервис не был ранее запущен.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.ApplicationManager](N_Tessa_Applications_Services_ApplicationManager.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask StartServiceAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function StartServiceAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask StartServiceAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract StartServiceAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IApplicationManagerServiceHost -
](T_Tessa_Applications_Services_ApplicationManager_IApplicationManagerServiceHost.htm)
[Tessa.Applications.Services.ApplicationManager - пространство
имён](N_Tessa_Applications_Services_ApplicationManager.htm)
