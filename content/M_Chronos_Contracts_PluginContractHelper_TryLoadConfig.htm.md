# PluginContractHelper.TryLoadConfig - метод
Загружает конфигурационный файл плагина из файла, расположенного по заданному
пути, и возвращает загруженный XML-документ или null, если файл отсутствовал
по заданному пути.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static XElement TryLoadConfig(
    	string filename
    )
VB __Копировать
     Public Shared Function TryLoadConfig ( 
    	filename As String
    ) As XElement
C++ __Копировать
     public:
    static XElement^ TryLoadConfig(
    	String^ filename
    )
F# __Копировать
     static member TryLoadConfig : 
            filename : string -> XElement 
#### Параметры
filename [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к конфигурационному файлу или путь относительно текущей папки.
#### Возвращаемое значение
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement)  
Корневой элемент конфигурационного файла или null, если файл отсутствовал по
заданному пути.
## __См. также
#### Ссылки
[PluginContractHelper - ](T_Chronos_Contracts_PluginContractHelper.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
