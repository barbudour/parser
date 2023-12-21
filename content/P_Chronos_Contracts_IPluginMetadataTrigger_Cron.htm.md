# IPluginMetadataTrigger.Cron - свойство
Описание времени вызова плагина в строке формата Cron.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(null)]
    string Cron { get; }
VB __Копировать
    <DefaultValueAttribute(Nothing)>
    ReadOnly Property Cron As String
    	Get
C++ __Копировать
    [DefaultValueAttribute(nullptr)]
    property String^ Cron {
    	String^ get ();
    }
F# __Копировать
     [<DefaultValueAttribute(null)>]
    abstract Cron : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Если у плагина отсутствуют триггеры с Cron и
[RepeatSecondInterval](P_Chronos_Contracts_IPluginMetadataTrigger_RepeatSecondInterval.htm),
то он вызывается всего один раз.
## __См. также
#### Ссылки
[IPluginMetadataTrigger - ](T_Chronos_Contracts_IPluginMetadataTrigger.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
