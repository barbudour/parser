# PluginGracefulStopEventToken.EntryPointFinished - свойство
Признак того, что метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина был завершён.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public bool EntryPointFinished { get; }
VB __Копировать
     Public ReadOnly Property EntryPointFinished As Boolean
    	Get
C++ __Копировать
     public:
    virtual property bool EntryPointFinished {
    	bool get () sealed;
    }
F# __Копировать
     abstract EntryPointFinished : bool with get
    override EntryPointFinished : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IGracefulStopToken.EntryPointFinished](P_Chronos_Contracts_IGracefulStopToken_EntryPointFinished.htm)  
##  __Заметки
Свойство может быть безопасно использовано после вызова
[Dispose()](M_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_Dispose.htm).
## __См. также
#### Ссылки
[PluginGracefulStopEventToken -
](T_Chronos_Platform_Scheduling_PluginGracefulStopEventToken.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
