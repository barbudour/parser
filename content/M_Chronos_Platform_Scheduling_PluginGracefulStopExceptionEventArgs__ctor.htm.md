# PluginGracefulStopExceptionEventArgs - конструктор
Создаёт экземпляр класса с указанием значений всех его свойств.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginGracefulStopExceptionEventArgs(
    	ISupportGracefulStop gracefulPlugin,
    	IGracefulStopToken token,
    	Exception exception
    )
VB __Копировать
     Public Sub New ( 
    	gracefulPlugin As ISupportGracefulStop,
    	token As IGracefulStopToken,
    	exception As Exception
    )
C++ __Копировать
     public:
    PluginGracefulStopExceptionEventArgs(
    	ISupportGracefulStop^ gracefulPlugin, 
    	IGracefulStopToken^ token, 
    	Exception^ exception
    )
F# __Копировать
     new : 
            gracefulPlugin : ISupportGracefulStop * 
            token : IGracefulStopToken * 
            exception : Exception -> PluginGracefulStopExceptionEventArgs
#### Параметры
gracefulPlugin
[ISupportGracefulStop](T_Chronos_Contracts_ISupportGracefulStop.htm)
    Плагин, вежливая остановка которого производится.
token [IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm)
    Токен, позволяющий определить состояние плагина.
exception [Exception](https://learn.microsoft.com/dotnet/api/system.exception)
     Исключение, возникшее в методе [StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm) объекта [GracefulPlugin](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_GracefulPlugin.htm). 
## __См. также
#### Ссылки
[PluginGracefulStopExceptionEventArgs -
](T_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
