# PluginAttribute.DisallowConcurrency - свойство
Признак запрета параллельного выполнения плагина. Если признак установлен, то,
пока процесс плагина выполняется, другой процесс не будет запущен.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public bool DisallowConcurrency { get; set; }
VB __Копировать
     Public Property DisallowConcurrency As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool DisallowConcurrency {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract DisallowConcurrency : bool with get, set
    override DisallowConcurrency : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IPluginMetadata.DisallowConcurrency](P_Chronos_Contracts_IPluginMetadata_DisallowConcurrency.htm)  
##  __Заметки
Не имеет смысл устанавливать свойство равным true, если плагин запускается
ровно один раз.
## __См. также
#### Ссылки
[PluginAttribute - ](T_Chronos_Contracts_PluginAttribute.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
