# PluginAttribute.LaunchImmediately - свойство
Признак гарантированного запуска плагина сразу после старта хоста, независимо
от расписания.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public bool LaunchImmediately { get; set; }
VB __Копировать
     Public Property LaunchImmediately As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool LaunchImmediately {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract LaunchImmediately : bool with get, set
    override LaunchImmediately : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IPluginMetadata.LaunchImmediately](P_Chronos_Contracts_IPluginMetadata_LaunchImmediately.htm)  
##  __Заметки
Не имеет смысл устанавливать свойство равным true, если плагин запускается
ровно один раз или по расписанию с периодом запуска.
## __См. также
#### Ссылки
[PluginAttribute - ](T_Chronos_Contracts_PluginAttribute.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
