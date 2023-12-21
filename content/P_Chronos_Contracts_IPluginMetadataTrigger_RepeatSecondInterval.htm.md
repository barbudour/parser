# IPluginMetadataTrigger.RepeatSecondInterval - свойство
Целочисленный интервал в секундах между вызовами плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(0)]
    int RepeatSecondInterval { get; }
VB __Копировать
    <DefaultValueAttribute(0)>
    ReadOnly Property RepeatSecondInterval As Integer
    	Get
C++ __Копировать
    [DefaultValueAttribute(0)]
    property int RepeatSecondInterval {
    	int get ();
    }
F# __Копировать
     [<DefaultValueAttribute(0)>]
    abstract RepeatSecondInterval : int with get
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __Заметки
Если у плагина отсутствуют триггеры с
[Cron](P_Chronos_Contracts_IPluginMetadataTrigger_Cron.htm) и
RepeatSecondInterval, то он вызывается всего один раз.
## __См. также
#### Ссылки
[IPluginMetadataTrigger - ](T_Chronos_Contracts_IPluginMetadataTrigger.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
