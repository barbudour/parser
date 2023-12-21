# IPluginMetadataTrigger.ConfigFile - свойство
Имя или путь к конфигурационному файлу, описывающему плагин, относительно
папки со сборкой плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(null)]
    string ConfigFile { get; }
VB __Копировать
    <DefaultValueAttribute(Nothing)>
    ReadOnly Property ConfigFile As String
    	Get
C++ __Копировать
    [DefaultValueAttribute(nullptr)]
    property String^ ConfigFile {
    	String^ get ();
    }
F# __Копировать
     [<DefaultValueAttribute(null)>]
    abstract ConfigFile : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Полное описание плагина составляют все его триггеры с параметрами
[Cron](P_Chronos_Contracts_IPluginMetadataTrigger_Cron.htm) и
[RepeatSecondInterval](P_Chronos_Contracts_IPluginMetadataTrigger_RepeatSecondInterval.htm),
а также содержимое всех конфигурационных файлов, на которые ссылаются
параметры ConfigFile.
## __Пример
XML __Копировать
     <?xml version="1.0" encoding="UTF-8"?>
    <plugin xmlns="http://syntellect.ru/chronos"
            name="My plugin"
            version="2">
        <trigger cron="0 0 12 ? * WED" />
        <trigger repeatSeconds="120" />
    </plugin>
##  __См. также
#### Ссылки
[IPluginMetadataTrigger - ](T_Chronos_Contracts_IPluginMetadataTrigger.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
