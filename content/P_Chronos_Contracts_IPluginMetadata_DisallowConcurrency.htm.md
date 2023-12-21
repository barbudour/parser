# IPluginMetadata.DisallowConcurrency - свойство
Признак запрета параллельного выполнения плагина. Если признак установлен, то,
пока процесс плагина выполняется, другой процесс того же плагина не будет
запущен, а планировщик будет дожидаться следующего срабатывания одного из
триггеров.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(false)]
    bool DisallowConcurrency { get; }
VB __Копировать
    <DefaultValueAttribute(false)>
    ReadOnly Property DisallowConcurrency As Boolean
    	Get
C++ __Копировать
    [DefaultValueAttribute(false)]
    property bool DisallowConcurrency {
    	bool get ();
    }
F# __Копировать
     [<DefaultValueAttribute(false)>]
    abstract DisallowConcurrency : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __Заметки
Не имеет смысла устанавливать свойство равным true, если плагин запускается
ровно один раз. Это приводит к снижению производительностью без положительного
эффекта.
## __См. также
#### Ссылки
[IPluginMetadata - ](T_Chronos_Contracts_IPluginMetadata.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
