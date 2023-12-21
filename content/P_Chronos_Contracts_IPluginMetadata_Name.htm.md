# IPluginMetadata.Name - свойство
Имя плагина. Используется для логирования и определения уникальности плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute("Unnamed plugin")]
    string Name { get; }
VB __Копировать
    <DefaultValueAttribute("Unnamed plugin")>
    ReadOnly Property Name As String
    	Get
C++ __Копировать
    [DefaultValueAttribute(L"Unnamed plugin")]
    property String^ Name {
    	String^ get ();
    }
F# __Копировать
     [<DefaultValueAttribute("Unnamed plugin")>]
    abstract Name : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
При сканировании сборки, в которой поменялось имя плагина, считается, что
плагин изменился. Одновременно может быть загружен только один плагин того же
типа из сборки с одним и тем же именем, независимо от параметров сборки
(версии, культуры и т.п.).
## __См. также
#### Ссылки
[IPluginMetadata - ](T_Chronos_Contracts_IPluginMetadata.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
