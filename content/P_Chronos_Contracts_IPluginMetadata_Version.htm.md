# IPluginMetadata.Version - свойство
Версия плагина. Используется для логирования и определения уникальности
плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    [DefaultValueAttribute(0)]
    int Version { get; }
VB __Копировать
    <DefaultValueAttribute(0)>
    ReadOnly Property Version As Integer
    	Get
C++ __Копировать
    [DefaultValueAttribute(0)]
    property int Version {
    	int get ();
    }
F# __Копировать
     [<DefaultValueAttribute(0)>]
    abstract Version : int with get
#### Значение свойства
[Int32](https://learn.microsoft.com/dotnet/api/system.int32)
##  __Заметки
При сканировании сборки, в которой поменялся номер версии плагина, считается,
что плагин изменился. Одновременно может быть загружен только один плагин того
же типа из сборки с одним и тем же именем, независимо от параметров сборки
(версии, культуры и т.п.).
## __См. также
#### Ссылки
[IPluginMetadata - ](T_Chronos_Contracts_IPluginMetadata.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
