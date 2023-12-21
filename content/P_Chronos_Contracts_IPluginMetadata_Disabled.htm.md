# IPluginMetadata.Disabled - свойство
Признак того, что плагин не будет использоваться.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(false)]
    bool Disabled { get; }
VB __Копировать
    <DefaultValueAttribute(false)>
    ReadOnly Property Disabled As Boolean
    	Get
C++ __Копировать
    [DefaultValueAttribute(false)]
    property bool Disabled {
    	bool get ();
    }
F# __Копировать
     [<DefaultValueAttribute(false)>]
    abstract Disabled : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Если значение установлено равным true, то хост не будет планировать запуск
плагина или запускать его.
Свойство полезно использовать для отладки или для того, чтобы отключить или
включить плагин с помощью конфигурационных файлов.
##  __См. также
#### Ссылки
[IPluginMetadata - ](T_Chronos_Contracts_IPluginMetadata.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
