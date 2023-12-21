# IPluginMetadata.LaunchImmediately - свойство
Признак гарантированного запуска плагина сразу после старта хоста, независимо
от расписания.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(false)]
    bool LaunchImmediately { get; set; }
VB __Копировать
    <DefaultValueAttribute(false)>
    Property LaunchImmediately As Boolean
    	Get
    	Set
C++ __Копировать
    [DefaultValueAttribute(false)]
    property bool LaunchImmediately {
    	bool get ();
    	void set (bool value);
    }
F# __Копировать
     [<DefaultValueAttribute(false)>]
    abstract LaunchImmediately : bool with get, set
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Не имеет смысл устанавливать свойство равным true, если плагин запускается
ровно один раз или по расписанию с периодом запуска.
## __См. также
#### Ссылки
[IPluginMetadata - ](T_Chronos_Contracts_IPluginMetadata.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
