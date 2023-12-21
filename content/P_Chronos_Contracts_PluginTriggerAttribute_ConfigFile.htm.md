# PluginTriggerAttribute.ConfigFile - свойство
Имя или путь к конфигурационному файлу, описывающему плагин, относительно
папки со сборкой плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public string ConfigFile { get; set; }
VB __Копировать
     Public Property ConfigFile As String
    	Get
    	Set
C++ __Копировать
     public:
    virtual property String^ ConfigFile {
    	String^ get () sealed;
    	void set (String^ value) sealed;
    }
F# __Копировать
     abstract ConfigFile : string with get, set
    override ConfigFile : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[IPluginMetadataTrigger.ConfigFile](P_Chronos_Contracts_IPluginMetadataTrigger_ConfigFile.htm)  
##  __См. также
#### Ссылки
[PluginTriggerAttribute - ](T_Chronos_Contracts_PluginTriggerAttribute.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
