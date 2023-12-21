# PluginGracefulStopExceptionEventArgs.Token - свойство
Токен, позволяющий определить состояние плагина. Этот токен был передан в
метод
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm)
объекта
[GracefulPlugin](P_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs_GracefulPlugin.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IGracefulStopToken Token { get; }
VB __Копировать
     Public ReadOnly Property Token As IGracefulStopToken
    	Get
C++ __Копировать
     public:
    property IGracefulStopToken^ Token {
    	IGracefulStopToken^ get ();
    }
F# __Копировать
     member Token : IGracefulStopToken with get
#### Значение свойства
[IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm)
##  __См. также
#### Ссылки
[PluginGracefulStopExceptionEventArgs -
](T_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
