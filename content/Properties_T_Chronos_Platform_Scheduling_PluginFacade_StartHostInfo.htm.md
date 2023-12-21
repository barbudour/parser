# StartHostInfo - свойства
##  __Свойства
[AwaitGracefulStopSeconds](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_AwaitGracefulStopSeconds.htm)|
Количество секунд, которые выполняется ожидание вежливого завершения всех
плагинов со стороны хоста.  
---|---  
[HostActivityActionAsync](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_HostActivityActionAsync.htm)|
Метод, который должен осуществлять некоторые действия, по окончании которых
хост завершает свою работу. Если значение не задано или равно null, то в
качестве такого метода используется вызов await Task.Delay(Timeout.Infinite,
cancellationToken). Исключение
[OperationCanceledException](https://learn.microsoft.com/dotnet/api/system.operationcanceledexception),
выбрасываемое этим методом, игнорируется, поэтому его можно не перехватывать
внутри метода при ожидании токена.  
[PluginsFolderPath](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_PluginsFolderPath.htm)|
Папка, в которой осуществляется поиск плагинов. Поиск также выполняется в
подпапках первого уровня.  
[ProcessHost](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_ProcessHost.htm)|
Интерфейс запуска дочерних процессов.  
[ShutdownMode](P_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo_ShutdownMode.htm)|
Способ завершения процесса хоста.  
## __См. также
#### Ссылки
[PluginFacade.StartHostInfo -
](T_Chronos_Platform_Scheduling_PluginFacade_StartHostInfo.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
