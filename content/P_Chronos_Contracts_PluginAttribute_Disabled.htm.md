# PluginAttribute.Disabled - свойство
Признак того, что плагин не будет использоваться.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public bool Disabled { get; set; }
VB __Копировать
     Public Property Disabled As Boolean
    	Get
    	Set
C++ __Копировать
     public:
    virtual property bool Disabled {
    	bool get () sealed;
    	void set (bool value) sealed;
    }
F# __Копировать
     abstract Disabled : bool with get, set
    override Disabled : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
#### Реализации
[IPluginMetadata.Disabled](P_Chronos_Contracts_IPluginMetadata_Disabled.htm)  
##  __Заметки
Если значение установлено равным true, то хост не будет планировать запуск
плагина или запускать его.
Свойство полезно использовать для отладки или для того, чтобы отключить или
включить плагин с помощью конфигурационных файлов.
##  __См. также
#### Ссылки
[PluginAttribute - ](T_Chronos_Contracts_PluginAttribute.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
